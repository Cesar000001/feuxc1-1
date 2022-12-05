def on_button_pressed_a():
    radio.send_string("Sy")
input.on_button_pressed(Button.A, on_button_pressed_a)

def feuV():
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
def feuO():
    strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))

def on_received_string(receivedString):
    global t, state
    if receivedString == "F0":
        feuO()
        basic.pause(2000)
        feuR()
        t = 20
        state = 1
    if receivedString == "Sy":
        t = 7
        state = 1
radio.on_received_string(on_received_string)

def feuR():
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
def neopixel2():
    global strip
    strip = neopixel.create(DigitalPin.P2, 5, NeoPixelMode.RGB)
    strip.set_brightness(32)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
def décompte():
    global t, state
    basic.show_number(t)
    basic.pause(1000)
    t += -1
    if t == 5:
        radio.send_string("F0")
    if t == 0:
        state = 0
        feuV()
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
t = 0
strip: neopixel.Strip = None
state = 0
radio.set_group(10)
neopixel2()
state = 20
feuR()
basic.show_leds("""
    . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
""")

def on_forever():
    if state == 1:
        décompte()
    else:
        pass
basic.forever(on_forever)
