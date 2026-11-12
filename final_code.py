#This code is the property of Ilia Bakhshayesh and Mohammadreza Kermani
# AI has been used in the process of learning. This project is NOT vibe coded.
# The model used is made by Google and trained by Ilia Bakhshayesh
# under the name TRASH HORSE.
#
# TRASH HORSE stands for:
# Technology for Recycling and Automated Separation
# of Household Waste Horse

import cv2
import numpy as np
import tensorflow as tf
from time import sleep, perf_counter
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory



def servo_control(servo, angle):
    servo.angle = angle
    sleep(2)
    servo.angle = 90
    sleep(2)

def maincore(model, cameranumber):
    factory = PiGPIOFactory()
    servo_MG = AngularServo(
        18,
        min_angle=0,
        max_angle=180,
        min_pulse_width=0.0005,
        max_pulse_width=0.0025,
        pin_factory=factory
    )
    servo_PlPa = AngularServo(
        19,
        min_angle=0,
        max_angle=180,
        min_pulse_width=0.0005,
        max_pulse_width=0.0025,
        pin_factory=factory
    )
    sleep(3)
    servo_MG.angle = 90
    sleep(3)
    servo_PlPa.angle = 90
    sleep(3)
   
    interpreter = tf.lite.Interpreter(
        model_path=model
    )
    interpreter.allocate_tensors()
    # AI information
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    input_index = input_details[0]["index"]
    output_index = output_details[0]["index"]
    height = input_details[0]["shape"][1]
    width = input_details[0]["shape"][2]
    # Quantization
    input_scale, input_zero = input_details[0]["quantization"]
    output_scale, output_zero = output_details[0]["quantization"]

    camera = cv2.VideoCapture(cameranumber)
    if not camera.isOpened():
        print("Camera not found!")
        servo_MG.close()
        servo_PlPa.close()
        factory.close()
        return
    last_prediction = perf_counter()
    class_lists = [
        "NTO",
        "Metal",
        "Plastic",
        "Paper",
        "Glass"
    ]
    current_list = []
    try:
        while True:
            ret, frame = camera.read()
            if not ret:
                print("Cannot read camera!")
                break
            current_time = perf_counter()
            if current_time - last_prediction >= 0.5:
                # Update timer BEFORE inference
                last_prediction = current_time
                # Image processing
                frame_transformed_into_RGB = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )
                frame_resized = cv2.resize(
                    frame_transformed_into_RGB,
                    (width, height)
                )
                image = np.expand_dims(frame_resized, axis=0)
                image = image.astype(np.float32) / 127.5 - 1.0
                image = np.round(
                    image / input_scale + input_zero
                )
                image = np.clip(
                    image,
                    0,
                    255
                ).astype(np.uint8)
                # Wake up the AI
                interpreter.set_tensor(input_index, image)
                interpreter.invoke()
                prediction = interpreter.get_tensor(output_index)
                prediction = (
                    prediction.astype(np.float32) - output_zero
                ) * output_scale
                prediction_highest = np.argmax(prediction[0])
                output_prediction = class_lists[prediction_highest]
                current_list.append(output_prediction)

                if len(current_list) == 4:
                    if all(item == current_list[0] for item in current_list):
                        final_output = current_list[0]
                        if final_output == "Metal":
                            print(f"m {final_output}")
                            servo_control(servo_MG, 0)
                        elif final_output == "Plastic":
                            print(f"pl {final_output}")
                            servo_control(servo_PlPa, 0)
                        elif final_output == "Paper":
                            print(f"pa {final_output}")
                            servo_control(servo_PlPa, 180)
                        elif final_output == "Glass":
                            print(f"g {final_output}")
                        else:
                            print(f"n {final_output}")
                    current_list = []
            # Display camera (optional)
            # cv2.imshow("TRASH HORSE", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
        servo_MG.close()
        servo_PlPa.close()
        factory.close()


maincore("model.tflite", 0)
