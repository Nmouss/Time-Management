from gpiozero import LED
""" I had to create this class
    due to circular import problems
                                """

# setup leds
Blue = LED(26)
Green = LED(19)
Red = LED(13)
Blue.on()
Green.on()
Red.on()
class LEDS:
    # on
    def green_on():
        Green.off()

    def blue_on():
        Blue.off()

    def red_on():
        Red.off()

    def yellow_on():
        Red.off()
        Green.off()
    # off   
    def green_off():
        Green.on()

    def blue_off():
        Blue.on()

    def red_off():
        Red.on()

    def yellow_off():
        Red.on()
        Green.on()