import cv2, math
import numpy as np
import tensorflow as tf
import time
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from board import SCL, SDA
from gpiozero import Button, LED
import RPi.GPIO as GPIO
from LEDS import LEDS
# FOR OLED DISPLAY
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()


# FOR OBJECT DETECTION
model = tf.lite.Interpreter(model_path="/PATH/TO/YOUR/DIRECTORY/model.tflite") # CHANGE THIS WHERE THE TF.LITE MODEL IS
model.allocate_tensors()  # This loads the model and its tensors

input_details = model.get_input_details()  # Gets data about the tensor
output_details = model.get_output_details()
#print(model.get_output_details()[0])

input_shape = input_details[0]['shape']  # Model input shape
input_height, input_width = input_shape[1], input_shape[2]

class run_model:
    seconds = 0
    count = 0
    break_number = 0
    def sec(seconds):
        run_model.seconds = seconds
        run_model.count = math.floor(seconds / 2700) # CHANGE THIS BACK TO SECONDS / 2700

    def camera():
        vid = cv2.VideoCapture(0)
        if not vid.isOpened():
            print("Error: camera cannot be opened")
            exit()
        while True:
            ret, frame = vid.read()
            if not ret:
                print("Error: cannot read frame")
                break
            
            # Resize the frame to 224x224
            frame_resized = cv2.resize(frame, (224, 224))
            
            cv2.imshow("Camera - 224x224", frame_resized)
            if Button(17).is_pressed or  Button(22).is_pressed or Button(27).is_pressed or (cv2.waitKey(1) & 0xFF == ord('q')):
                break
            if run_model.seconds == 0:
                break

        vid.release()
        cv2.destroyAllWindows()
  
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        run_model.run_model(run_model.seconds)
        return

    def camera_inital():
        Button(17).close()
        Button(27).close()
        Button(22).close()
        LEDS.red_off()
        LEDS.blue_off()
        LEDS.yellow_on()
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((20, -2 + 0), "Phone in frame?", font=font, fill=1) #(30 means right 30 px, -2 means up and down where -2 is all the at the top and change)
        draw.text((8, 8 + 0), "If yes press ANY to", font=font, fill=1)
        draw.text((43, 20 + 0), " START!", font=font, fill=1)
        disp.image(image)
        disp.show()
        
        


    def return_score(boxes, class_scores, threshold=0.8):
        for i in range(len(boxes)):
            score = class_scores[i][1]  # Assuming the second column contains the score
            if score >= threshold:
                result_text = f'Phone ({score:.2f})'
            return score
        
    def run_model(seconds):

        def pause():
            vid.release()
            cv2.destroyAllWindows()
            break_seconds = 600 # CHANGE THIS TO CHANGE THE AMOUNT OF BREAK TIME 600 for 10 minutes
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            disp.image(image)
            disp.show()
            draw.text((-1, -2 + 0), "PHONE NOT DETECTED!", font=font, fill=1) #(30 means right 30 px, -2 means up and down where -2 is all the at the top and change)
            draw.text((0, 8 + 0), "BREAK? CLICK R OR L", font=font, fill=1)
            draw.text((0, 20 + 0), "IF ERROR CLICK MIDDLE", font=font, fill=1)
            disp.image(image)
            disp.show()
            time.sleep(1)
            while run_model.seconds > 0:
                if Button(27).is_pressed:
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    disp.image(image)
                    disp.show()
                    run_model.camera_inital()
                    run_model.camera()
                    break

                if Button(17).is_pressed or Button(22).is_pressed:
                    LEDS.yellow_off()
                    LEDS.blue_on()
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    disp.image(image)
                    disp.show()
                    if run_model.break_number < run_model.count:
                        run_model.break_number += 1
                        while break_seconds != 0:
                            break_seconds -= 1
                            minutes = int(break_seconds / 60)
                            displayseconds = break_seconds - minutes * 60
                            draw.text((7, -2 + 0), "BREAK IN PROGRESS", font=font, fill=1)
                            draw.text((2, 6 + 0), f"Minutes remaining: {minutes}", font=font, fill=1)
                            draw.text((2, 14), f"Seconds remaining: {displayseconds}",font=font, fill=1)
                            disp.image(image)
                            disp.show()
                            time.sleep(1)
                            draw.text((2, 6 + 0), f"Minutes remaining: {minutes}", font=font, fill=0)
                            draw.text((2, 14), f"Seconds remaining: {displayseconds}",font=font, fill=0)

                        draw.rectangle((0, 0, width, height), outline=0, fill=0)

                        vid.release()
                        cv2.destroyAllWindows()
                        LEDS.blue_off()
                        LEDS.yellow_on()
                        run_model.camera_inital()
                        run_model.camera()
                    else:
                        if run_model.break_number == 0:
                            draw.text((2, 6 + 0), f"No breaks avaliable!", font=font, fill=1)
                            disp.image(image)
                            disp.show()
                            time.sleep(4)
                            
                        else:
                            if run_model.break_number == 1:
                                draw.text((2, 6 + 0), f"No breaks avaliable!", font=font, fill=1)
                                draw.text((2, 14), f"Exceeded: {run_model.count} break!",font=font, fill=1)
                                disp.image(image)
                                disp.show()
                                time.sleep(4)
                            else:
                                draw.text((2, 6 + 0), f"No breaks avaliable!", font=font, fill=1)
                                draw.text((2, 14), f"Exceeded: {run_model.count} breaks!",font=font, fill=1)
                                disp.image(image)
                                disp.show()
                                time.sleep(4)


                        LEDS.blue_off()
                        LEDS.green_on()    
                        draw.rectangle((0, 0, width, height), outline=0, fill=0)
                        run_model.seconds = 0
                        vid.release()
                        cv2.destroyAllWindows()
                    
        vid = cv2.VideoCapture(0)
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        while run_model.seconds > 0:
            LEDS.yellow_off()
            LEDS.red_on()
            minutes = int(run_model.seconds / 60)
            displayseconds = run_model.seconds - minutes * 60
            run_model.seconds -= 1
            ret, imag = vid.read()  # Gets the camera frame
            if not ret:
                print("Camera is not working")
            
            image_resized = cv2.resize(imag, (input_width, input_height))  # Resize to model input size
            input_data = np.asarray(image_resized, dtype=np.float32).reshape(1, input_height, input_width, 3)
            input_data = (input_data / 127.5) - 1  # Normalize the image to [-1, 1]

            model.set_tensor(input_details[0]['index'], input_data)
            model.invoke()  # Run the model

            boxes = model.get_tensor(output_details[0]['index'])[0]  # Bounding boxes
            class_scores = model.get_tensor(output_details[1]['index'])[0]  # Class scores

            filtered_indices = np.where(class_scores[:, 1])[0]  # Assuming the second value in each pair is the score
            filtered_boxes = boxes[filtered_indices]
            filtered_scores = class_scores[filtered_indices]

            selected_indices = tf.image.non_max_suppression(
            filtered_boxes,
            filtered_scores[:, 1],  # Assuming the second value in each pair is the confidence score
            max_output_size=1,  # Maximum number of boxes to keep I did one because im only detecting one phone
            iou_threshold=0.5,  # Classifies predicted bounding boxes however I am not using any so default is 0.5
            score_threshold=0.75 # Change the the threashold here 
            )
            selected_boxes = tf.gather(filtered_boxes, selected_indices).numpy()
            selected_scores = tf.gather(filtered_scores, selected_indices).numpy()


            score = run_model.return_score(selected_boxes, selected_scores)  # Visualize bounding boxes

            if seconds == 0:
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                LEDS.red_off()
                LEDS.green_on()
                break

            elif seconds != 0:
                draw.text((7, -2 + 0), "FOCUS SESSION IS ON", font=font, fill=1)
                draw.text((2, 6 + 0), f"Minutes remaining: {minutes}", font=font, fill=0)
                draw.text((2, 14), f"Seconds remaining: {displayseconds}",font=font, fill=0)
                minutes = int(run_model.seconds / 60)
                displayseconds = run_model.seconds - minutes * 60
                draw.text((2, 6 + 0), f"Minutes remaining: {minutes}", font=font, fill=1)
                draw.text((2, 14), f"Seconds remaining: {displayseconds}",font=font, fill=1)
                disp.image(image)
                disp.show()
                time.sleep(1)

            if score == None:
                LEDS.red_off()
                LEDS.yellow_on()
                pause()
        else:
            return


