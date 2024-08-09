# What is this?

This project is designed to enhance focus by preventing phone use during dedicated work sessions through object detection. The user interacts with the system via buttons, allowing them to add time to their focus session or initiate a 10-minute break after every 45 minutes of work.

The idea behind this project was to help me maintain focus by adding a layer of accountability, which is why I built this prototype. The system uses green, red, yellow, and blue lights to indicate different statuses: whether the session is over, the phone is detected, the session is in progress, or the session needs to be initiated. While the current setup is on a breadboard, I plan to upgrade it to a circuit board in the future.

# How can I use it?

Materials needed: 1x OLED display, 3x Buttons, 1x RGB LED, 1x Breadboard, Minimum 12x male-female jumper cables, A Raspberry Pi that can operate 64 bits (For tensorflow)

![IMG_8810](https://github.com/user-attachments/assets/ea6aba26-966b-43eb-ac72-860d29def78d)


# Step 1

Install packages
- pip3 install tensorflow
- pip3 install Adafruit-SSD1306
- pip3 install adafruit-blinka
- pip install Pillow

# Background

When I first began this project it originally started out as a basic feature where you add time and start it, then the countdown begun. 


