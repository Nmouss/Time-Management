#all imports
from gpiozero import LED, Button
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from board import SCL, SDA
import time
import threading
import RPi.GPIO as GPIO
from object_detection import run_model as rm
from LEDS import LEDS
GPIO.cleanup()
"""setup oLED display"""
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# Clear display
disp.fill(0)
disp.show()
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
b = ""
font = ImageFont.load_default()
draw.rectangle((0, 0, width, height), outline=0, fill=0)

while True:
    #draw.rectangle((0, 0, width, height), outline=0, fill=0) #this clears the box
    counter = 0

    draw.text((30, -2 + 0), b + "Welcome to...", font=font, fill=1) #(30 means right 30 px, -2 means up and down where -2 is all the at the top and change)
    draw.text((15, 8 + 0), b + "The focus session", font=font, fill=1)
    draw.text((15, 20 + 0), b + "Click any button", font=font, fill=1)
    disp.image(image)
    disp.show()
    LEDS.yellow_on()

    while True:
        if Left_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Before you start...", font=font, fill=1)
            draw.text((0, 8 + 0), b + "Bring your phone", font=font, fill=1)
            draw.text((0, 20 + 0), b + "If done click any", font=font, fill=1)
            disp.image(image)
            disp.show()
            break
        if Middle_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Before you start...", font=font, fill=1)
            draw.text((0, 8 + 0), b + "Bring your phone", font=font, fill=1)
            draw.text((0, 20 + 0), b + "If done click any", font=font, fill=1)
            disp.image(image)
            disp.show()
            break
        
        if Right_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Before you start...", font=font, fill=1)
            draw.text((0, 8 + 0), b + "Bring your phone", font=font, fill=1)
            draw.text((0, 20 + 0), b + "If done click any", font=font, fill=1)
            disp.image(image)
            disp.show()
            break
    time.sleep(1)

    while True:
        if Left_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Remember this device", font=font, fill=1)
            draw.text((0, 8 + 0), b + "is for DEEP work", font=font, fill=1)
            draw.text((0, 20 + 0), b + "DONT forget!", font=font, fill=1)
            disp.image(image)
            disp.show()
            break
        if Middle_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Remember this device", font=font, fill=1)
            draw.text((0, 8 + 0), b + "is for DEEP work", font=font, fill=1)
            draw.text((0, 20 + 0), b + "DONT forget!", font=font, fill=1)
            disp.image(image)
            disp.show()
            break
        
        if Right_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Remember this device", font=font, fill=1)
            draw.text((0, 8 + 0), b + "is for DEEP work DONT", font=font, fill=1)
            draw.text((0, 20 + 0), b + "forget! | Click any", font=font, fill=1)
            disp.image(image)
            disp.show()
            break

    time.sleep(1)
    while True:
        if Left_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Right button +15 min", font=font, fill=1)
            draw.text((0, 6 + 0), b + "Left button -15 min", font=font, fill=1)
            draw.text((0, 15 + 0), b + "Middle button to start", font=font, fill=1)
            draw.text((0, 23 + 0), b + f"Total time: {counter} mins" , font=font, fill=1)
            disp.image(image)
            disp.show()
            break
        if Middle_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Right button +15 min", font=font, fill=1)
            draw.text((0, 6 + 0), b + "Left button -15 min", font=font, fill=1)
            draw.text((0, 15 + 0), b + "Middle button to start", font=font, fill=1)
            draw.text((0, 23 + 0), b + f"Total time: {counter} mins" , font=font, fill=1)
            disp.image(image)
            disp.show()
            break        
        if Right_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
            draw.text((0, -2 + 0), b + "Right button +15 min", font=font, fill=1)
            draw.text((0, 6 + 0), b + "Left button -15 min", font=font, fill=1)
            draw.text((0, 15 + 0), b + "Middle button to start", font=font, fill=1)
            draw.text((0, 23 + 0), b + f"Total time: {counter} mins" , font=font, fill=1)
            disp.image(image)
            disp.show()
            break        
    time.sleep(1)
    # issue under this message i think more specifically I need to refresh everything then put it back for the second if statement
    while True:
        if Right_button.is_pressed:
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            time.sleep(0.3)
            counter += 15  # ---------------------------------------------------------------------CHANGE THIS TO 15-----------------------------------------------   

            draw.text((0, -2 + 0), b + "Right button +15 min", font=font, fill=1)
            draw.text((0, 6 + 0), b + "Left button -15 min", font=font, fill=1)
            draw.text((0, 15 + 0), b + "Middle button to start", font=font, fill=1)
            draw.text((0, 23 + 0), b + f"Total time: {counter} mins" , font=font, fill=1)
            disp.image(image)
            disp.show()
        if Left_button.is_pressed: # needs a refresh
            time.sleep(0.3)
            if counter <= 0:
                draw.rectangle((0, 0, width, height), outline=0, fill=0)

                draw.text((0, -2 + 0), b + "Right button +15 min", font=font, fill=1)
                draw.text((0, 6 + 0), b + "Left button -15 min", font=font, fill=1)
                draw.text((0, 15 + 0), b + "Middle button to start", font=font, fill=1)
                draw.text((0, 23 + 0), b + f"Cannot do that" , font=font, fill=1)
                disp.image(image)
                disp.show()
                time.sleep(2)
                draw.rectangle((0, 0, width, height), outline=0, fill=0)

                draw.text((0, -2 + 0), b + "Right button +15 min", font=font, fill=1)
                draw.text((0, 6 + 0), b + "Left button -15 min", font=font, fill=1)
                draw.text((0, 15 + 0), b + "Middle button to start", font=font, fill=1)
                draw.text((0, 23 + 0), b + f"Total time: {counter} mins" , font=font, fill=1)
                disp.image(image)
                disp.show()
                continue
            else:
                counter -= 15
                draw.rectangle((0, 0, width, height), outline=0, fill=0)

                draw.text((0, -2 + 0), b + "Right button +15 min", font=font, fill=1)
                draw.text((0, 6 + 0), b + "Left button -15 min", font=font, fill=1)
                draw.text((0, 15 + 0), b + "Middle button to start", font=font, fill=1)
                draw.text((0, 23 + 0), b + f"Total time: {counter} mins" , font=font, fill=1)
                disp.image(image)
                disp.show()
        if Middle_button.is_pressed:
            break

    time.sleep(0.2)
    detection = False
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    draw.text((0, -2 + 0), b + "Enable Detection?", font=font, fill=1)
    draw.text((0, 6 + 0), b + "Right Button Enables", font=font, fill=1)
    draw.text((0, 15 + 0), b + "Left Button Disables", font=font, fill=1)
    disp.image(image)
    disp.show()

    while True:
        if Right_button.is_pressed:
            detection = True
            break
        if Left_button.is_pressed:
            detection = False
            break

    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    seconds = 60 * counter
    def countdown():
        draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
        draw.text((0, -2 + 0), b + "Before you start...", font=font, fill=1)
        draw.text((0, 8 + 0), b + "Put phone in a drawer", font=font, fill=1)
        draw.text((0, 20 + 0), b + "If done click any", font=font, fill=1)
        disp.image(image)
        disp.show()
        time.sleep(1)
        while True:
            if Left_button.is_pressed:
                draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
                draw.text((0, -2 + 0), b + "Before you start...", font=font, fill=1)
                draw.text((0, 8 + 0), b + "Put phone in a drawer", font=font, fill=1)
                draw.text((0, 20 + 0), b + "If done click any", font=font, fill=1)
                disp.image(image)
                disp.show()
                break
            if Middle_button.is_pressed:
                draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
                draw.text((0, -2 + 0), b + "Before you start...", font=font, fill=1)
                draw.text((0, 8 + 0), b + "Put phone in a drawer", font=font, fill=1)
                draw.text((0, 20 + 0), b + "If done click any", font=font, fill=1)
                disp.image(image)
                disp.show()
                break
            
            if Right_button.is_pressed:
                draw.rectangle((0, 0, width, height), outline=0, fill=0) # clears
                draw.text((0, -2 + 0), b + "Before you start...", font=font, fill=1)
                draw.text((0, 8 + 0), b + "Put phone in a drawer", font=font, fill=1)
                draw.text((0, 20 + 0), b + "If done click any", font=font, fill=1)
                disp.image(image)
                disp.show()
                break

        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        time.sleep(0.3)
        global nopause
        global countdown
        global displayseconds
        global minutes
        global counter
        LEDS.yellow_off()
        seconds = 60 * counter
        nopause = True
        countdown = True
        displayseconds = 0
        minutes = 0
        draw.text((7, -2 + 0), b + "FOCUS SESSION IS ON", font=font, fill=1)
        disp.image(image)
        disp.show()
        while countdown:
            while nopause:
                if seconds == 0:
                    draw.text((7, -2 + 0), b + "FOCUS SESSION IS ON", font=font, fill=0)
                    disp.image(image)
                    disp.show()
                    countdown = False
                    LEDS.red_off()
                    LEDS.green_on()
                    draw.text((7, -2 + 0), b + "FOCUS SESSION IS OFF", font=font, fill=1)
                    disp.image(image)
                    disp.show()
                    break
                else:
                    draw.text((7, -2 + 0), b + "FOCUS SESSION IS ON", font=font, fill=1)
                    LEDS.red_on()
                    draw.text((2, 6 + 0), b + f"Minutes remaining: {minutes}", font=font, fill=0)
                    draw.text((2, 14), b + f"Seconds remaining: {displayseconds}",font=font, fill=0)
                    seconds-= 1
                    minutes = int(seconds / 60)
                    displayseconds = seconds - minutes * 60
                    draw.text((2, 6 + 0), b + f"Minutes remaining: {minutes}", font=font, fill=1)
                    draw.text((2, 14), b + f"Seconds remaining: {displayseconds}",font=font, fill=1)
                    disp.image(image)
                    disp.show()
                    time.sleep(1)

    if detection:
        countdown_thread = threading.Thread(target=countdown)
        camera_inital = threading.Thread(target=rm.camera_inital)
        camera = threading.Thread(target=rm.camera)
        Left_button.close()
        Middle_button.close()
        Right_button.close()
        rm.sec(seconds)
        rm.camera_inital()
        rm.camera()
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        Left_button = Button(17) # need to redefine the buttons otherwise it will throw an error!
        Middle_button = Button(27)
        Right_button = Button(22)
    else:
        countdown()

    # resets everything
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, -2 + 0), b + "FOCUS SESSION IS OFF", font=font, fill=1)
    draw.text((0, 8 + 0), b + "To begin another one", font=font, fill=1)
    draw.text((0, 20 + 0), b + "Click any button", font=font, fill=1)
    disp.image(image)
    disp.show()
    LEDS.red_off()
    LEDS.green_on()
    time.sleep(2)
    while True:
        if Button(22).is_pressed or  Button(27).is_pressed or Button(17).is_pressed:
            break
        time.sleep(0.1)
        
    draw.rectangle((0, 0, width, height), outline=0, fill=0)  
    GPIO.cleanup()
    
    time.sleep(1)
