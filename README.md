# What is this?

This project is designed to enhance focus by preventing phone use during dedicated work sessions through object detection. The user interacts with the system via buttons, allowing them to add time to their focus session or initiate a 10-minute break after every 45 minutes of work.

The idea behind this project was to help me maintain focus by adding a layer of accountability, which is why I built this prototype. The system uses green, red, yellow, and blue lights to indicate different statuses: whether the session is over, the phone is detected, the session is in progress, or the session needs to be initiated. While the current setup is on a breadboard, I plan to upgrade it to a circuit board in the future.

# How can I use it?

Materials needed
- 1x OLED display
- 3x Buttons 
- 1x RGB LED 
- 1x Breadboard
- Minimum 12x male-female jumper cables
- 1x camera (USB or Waveshare IMX219 Camera Module, I personally used a Logitech C920)
- A Raspberry Pi that can operate 64 bits (For tensorflow)

![IMG_8810](https://github.com/user-attachments/assets/ea6aba26-966b-43eb-ac72-860d29def78d)


## Step 1

Open terminal on your raspberry pi (64 bit) and Install packages in terminal. Copy and paste each line. 

```
pip3 install tensorflow
pip3 install Adafruit-SSD1306
pip3 install adafruit-blinka
pip3 install Pillow
```
* Make sure you create a vm before installing packages unless you want them system wide.

## Step 2

Wire the system on a bread board with the following connections

![image](https://github.com/user-attachments/assets/0549f27f-834c-4a5a-afdc-60422ac285a2)




## Step 3 

Create a directory on your computer and download the files and move to the directory. Then run the main.py file.

## Background

When I first began this project it originally started out as a basic feature where you add time and start it, then the countdown begun. However some questions started to rise and I thought what if I added object detection so it makes me even more accountable because just putting your phone in a drawer can still be tempting, so I trained a tensorflow lite model with around 300 pictures of my phone with transfer learning. The model at times has some issues with detecting and confidence scores (Its just a prototype) however in the future I do want to update it and make it more reliable!


