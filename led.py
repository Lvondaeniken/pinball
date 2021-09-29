#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import random
import math
import time
from neopixel import *
import argparse
import threading

# LED strip configuration:
LED_COUNT      = 90      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/$
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor$
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

blueLastTime = 0

def current_milli_time():
    return round(time.time() * 1000)

# Define functions which animate LEDs in various ways.
def colorInline(strip, color, wait_ms=1):
    """Wipe color across display a pixel at a time."""
    for i in range (0, 25):
        strip.setPixelColor(i, color)
#       if i>6:
#               strip.setPixelColor(LED_COUNT-i+6, Color(0,0,0)) 
        #strip.show()
        time.sleep(wait_ms/1000.0)

def blueTaetschBang(strip, wait_ms=1):
    global blueLastTime
    """HAVE EACH LED ALTERNATE THROUGH BLUE AT RANDOM"""
    greenred = 0 # Default value to adjust green and red simultaneously to adjust brightness of blue leds
    currentMillis = current_milli_time()
    if ( blueLastTime < currentMillis - 200):
        blueLastTime = currentMillis
        for i in range (25,88):
            greenred = abs(20*int(math.cos(((i-random.randint(0,24))*math.pi)/8)))
            color = Color(greenred,greenred,255)    
            strip.setPixelColor(i, color) 
    #strip.show()
    #time.sleep(wait_ms/1000.0)

def launchSwipe(strip, color, wait_ms=10):
        for i in range(25,0,-1):
            strip.setPixelColor(i, color)
            #strip.show()
            time.sleep(wait_ms/1000.0)


def colorBottle(strip, color, wait_ms=10):
    strip.setPixelColor(88, color)
    #strip.show()

def colorBottleSelect(strip, wait_ms=10):
    strip.setPixelColor(88, Color(255,0,0))
    print("255")
    strip.show()
    time.sleep(wait_ms/10.0)

    strip.setPixelColor(88, Color(205,0,0))
    print("205")
    strip.show()
    time.sleep(wait_ms/10.0)

    strip.setPixelColor(88, Color(155,0,0))
    print("155")
    strip.show()
    time.sleep(wait_ms/10.0)

    strip.setPixelColor(88, Color(105,0,0))
    print("105")
    strip.show()
    time.sleep(wait_ms/10.0)

    strip.setPixelColor(88, Color(55,0,0))
    print("55")
    strip.show()
    time.sleep(wait_ms/10.0)

    strip.setPixelColor(88, Color(0,0,0))
    print("0")
    strip.show()
    time.sleep(wait_ms/10.0)


def colorWipe(strip, color, wait_ms=10):
    """Wipe color across display a pixel at a time."""
    for i in range(LED_COUNT+1):
        strip.setPixelColor(LED_COUNT-i, color)
#       if i>6:
#               strip.setPixelColor(LED_COUNT-i+6, Color(0,0,0)) 
        #strip.show()
        time.sleep(wait_ms/1000.0)



#### ----- ORIGINAL (Unused) COLORPIPE --------
def colorPipe(strip, color, wait_ms=10):
    """Wipe color across display a pixel at a time."""
    for i in range (25,89):
        strip.setPixelColor(i, color)
        if i>6:
            strip.setPixelColor(LED_COUNT-i+6, Color(0,0,0)) 
        strip.show()
        time.sleep(wait_ms/1000.0)

def brightnessPipe(strip, brightness, wait_ms=10):
    """Wipe color across display a pixel at a time."""
    for i in range (25,89):
        strip.setBrightness(i, brightness)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
                        strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j)))
            strip.show()
            time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the d')
    args = parser.parse_args()
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')


    
    try:

        while True:
            
            #print ('Color Test to find positions')
            #colorInline(strip, Color(0,0,0)) # Red wipe on strip based of pixel number
            #colorInline(strip, Color(80,80,255)) # Red wipe on strip based of pixel number
            
            
            ####################colorInline(strip, Color(0,255,0))

            #colorPipe(strip, Color(255,0,0)) # Green wipe on strip
            #colorPipe(strip, Color(0,255,0)) # Red wipe on strip
            #colorPipe(strip, Color(40,40,255)) # Blue wipe on strip
            #colorPipe(strip, Color(greenred,greenred,55))
            
        
            blueTaetschBang(strip)
            
            ####################launchSwipe(strip, Color(255,255,255))


            ####################colorBottle(strip, Color(105,0,0))
            #colorBottleSelect(strip)



            #brightnessPipe(strip, 255) # Black wipe on strip
            #brightnessPipe(strip, 160) # Black wipe on strip
            #brightnessPipe(strip, 120) # Black wipe on strip
            #brightnessPipe(strip, 160) # Black wipe on strip

            #print ('Color wipe animations.')
            #colorWipe(strip, Color(255, 0, 0))  # Red wipe
            #colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            #colorWipe(strip, Color(0, 0, 255))  # Green wipe
            
            #print ('Theater chase animations.')
            #theaterChase(strip, Color(127, 127, 127))  # White theater chase
            #theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            #theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
        
            #print ('Rainbow animations.')
            #rainbow(strip)
            #rainbowCycle(strip)
            #theaterChaseRainbow(strip)
            strip.show()
        
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
