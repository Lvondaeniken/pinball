from led_manager.led_color import LedColor 
import math
import random

#class WalkingLight:
class LedPattern:
    def __init__(self, timebase_ms, duration_s, led_count, color: LedColor):
        self.color = color
        self.timebase_ms = timebase_ms
        self.duration_s = duration_s
        self.led_count = led_count
        self.frame_counter = 0
        self.frames_to_survive = self.duration_s*1000/timebase_ms
        self.frames_per_led = self.frames_to_survive/self.led_count
        self.on_index = 0
        self.background_color = LedColor(0,0,0)
        self.led_states = []
        for i in range(self.led_count):
            self.led_states.append(self.background_color)

    def setBackground(self, color):
        self.background_color = color
        for led in self.led_states:
            led = color

    #def getNextFrame(self):
    def WalkingLights(self):
        self.frame_counter+=1
        if self.frame_counter==self.frames_per_led:
            self.on_index+=1
            self.frame_counter=0
        self.led_states[self.on_index] = self.color
        if self.on_index > 0:
            self.led_states[self.on_index-1] = self.background_color
        return self.led_states

    def WaterLights(self):
        self.frame_counter+=1
        if self.frame_counter==self.frames_per_led:
            self.on_index+=1
            self.frame_counter=0
        self.color.red = abs(20*int(math.cos((random.randint(0,24))*math.pi)/8))
        self.color.green = abs(20*int(math.cos((random.randint(0,24))*math.pi)/8))
        self.led_states[self.on_index] = self.color
        return self.led_states
    
    
if __name__ == '__main__':
    rail_one = WalkingLight(timebase_ms=20, duration=1, led_count=10, color=LedColor(255,255,255))
    for i in range (49):
        ledstates = rail_one.WalkingLights()
        for ledcolor in ledstates:
            print(ledcolor)
        print("--------------------")

    rail_two = LedPattern(timebase_ms=20, duration_s=1, led_count=10, color=LedColor(red=0,green=0,blue=255,brightness=100))
    for i in range (49):
        ledstates = rail_two.WaterLights()
        for ledcolor in ledstates:
            print(ledcolor)
        print("--------------------")
    print(abs(20*int(math.cos(random.randint(0,24)*math.pi/8))))
    



