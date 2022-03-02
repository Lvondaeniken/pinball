from led_pattern import LedColor 

class WalkingLight:
    def __init__(self, timebase_ms, duration_s, led_count, color: LedColor):
        self.color = color
        self.timebase_ms = timebase_ms
        self.duration_s = duration_s
        self.led_count = led_count
        self.frame_counter = 0
        self.frames_to_survive = self.duration_s*1000/timebas_ms
        self.frames_per_led = self.frames_to_survive/self.led_count
        self.on_index = 0
        self.led_states = []
        for i in range(self.led_count):
            self.led_states.append(LedColor(0,0,0,0))

    def setBackground(self, color):
        self.background_color = color
        for led in self.led_states:
            led = color

    def getNextFrame(self):
        self.frame_counter+=1
        if self.frame_counter==self.frames_per_led:
            self.on_index+=1
            self.frame_counter=0
        self.led_states[self.on_index] = self.color
        return self.led_states
    
if __name__ == '__main__':
    w = WalkingLight(20, 5, 10)
