input.onButtonPressed(Button.A, function () {
    radio.sendString("Sy")
})
function feuV () {
    strip.showColor(neopixel.colors(NeoPixelColors.Green))
}
function feuO () {
    strip.showColor(neopixel.colors(NeoPixelColors.Orange))
}
function neopixel2 () {
    strip = neopixel.create(DigitalPin.P2, 5, NeoPixelMode.RGB)
    strip.setBrightness(32)
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
}
radio.onReceivedString(function (receivedString) {
    if (receivedString == "F0") {
        feuO()
        basic.pause(2000)
        feuR()
        t = 30
        state = 1
    }
    if (receivedString == "Sy") {
        t = 7
        state = 1
    }
})
function feuR () {
    strip.showColor(neopixel.colors(NeoPixelColors.Red))
}
function décompte () {
    basic.showNumber(t)
    basic.pause(1000)
    t += -1
    if (t == 6) {
        radio.sendString("F0")
    }
    if (t == 0) {
        state = 0
        feuV()
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
}
let t = 0
let strip: neopixel.Strip = null
let state = 0
radio.setGroup(10)
neopixel2()
state = 20
feuR()
basic.showLeds(`
    . . # . .
    . . # . .
    . . # . .
    . . . . .
    . . # . .
    `)
basic.forever(function () {
    if (state == 1) {
        décompte()
    } else {
    	
    }
})
