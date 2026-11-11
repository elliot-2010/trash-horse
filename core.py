#this code is the property of Ilia Bakhshayesh and Mohammadreza Kermani
#while AI has been used in the process of learning. this project is NOT vibe coded
#the model used is made by google and is trained by Ilia Bakhshayesh under the name of TRASH HORSE
#TRASH HORSE stands for "Technology for Recycling and Automated Separation of Household waste Horse"


import cv2
import numpy as np
import tensorflow as tf
from threading import Thread
from time import sleep, perf_counter
from queue import Queue
from gpiozero import Servo



#making a queue
#the queue is a way for both functions to communicate

predictions = Queue()





def maincore(model, cameranumber):
    #Loading AI model
    interpreter = tf.lite.Interpreter(
        model_path=model
    )

    interpreter.allocate_tensors()



    #AI info
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_index = input_details[0]["index"]
    output_index = output_details[0]["index"]

    height, width = input_details[0]["shape"][1], input_details[0]["shape"][2]


    #quantization (in order to run better on raspberry 3)
    input_scale, input_zero = input_details[0]["quantization"]
    output_scale, output_zero = output_details[0]["quantization"]



    #Image processing
    camera = cv2.VideoCapture(cameranumber)

    if not camera.isOpened():
        print("Camera not found!")
        exit()

    last_prediction = perf_counter()

    class_lists = ["NTO", "Metal", "Plastic", "Paper", "Glass"]


    while True:
        start_time = perf_counter()
        ret, frame = camera.read()

        if not ret:
            print("Cannot read camera!")
            break

        current_time = perf_counter()



        if current_time - last_prediction >= 0.5:

            # Update timer BEFORE inference
            last_prediction = current_time

            # Image processing
            frame_transformed_into_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resized = cv2.resize(frame_transformed_into_RGB, (width, height))

            image = np.expand_dims(frame_resized, axis=0)
            image = image.astype(np.float32) / 127.5 - 1.0
            image = np.round(image / input_scale + input_zero)
            image = np.clip(image, 0, 255).astype(np.uint8)

            # waking up the ai
            interpreter.set_tensor(input_index, image)
            interpreter.invoke()

            prediction = interpreter.get_tensor(output_index)
            prediction = (prediction.astype(np.float32) - output_zero) * output_scale
            prediction_highest = np.argmax(prediction[0])

            # Send prediction to queue
            predictions.put(class_lists[prediction_highest])



        
        cv2.imshow("TRASH HORSE - Technology for Recycling and Automated Separation of Household waste Horse", frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    camera.release()
    cv2.destroyAllWindows()
    
def output():
    pass
    current_list = []

    while True:
        output_prediction = predictions.get()
        current_list.append(output_prediction)
        if len(current_list) == 4:
            if current_list[0] == current_list[1] and current_list[1] == current_list[2] and current_list[2] == current_list[3]:
                global final_output

                final_output = current_list[0]

                print(final_output)
                current_list = []
            else:
                current_list = []

def servo_control():
    sleep(2)
    if


#creating threads
servo_control_thread = Thread(target=servo_control)
maincore_thread = Thread(target=maincore, args=("model.tflite", 1))
output_thread =  Thread(target=output)
#starting threads
maincore_thread.start()
output_thread.start()
servo_control_thread.start()