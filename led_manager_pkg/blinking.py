from led_manager_pkg.led_color import LedColor

class BlinkingLight:
    def __init__(self, timebase_ms, duration_s, frequency_hz, led_count, color: LedColor, background: LedColor):
        # save params
        self.color = color
        self.frames_to_survive = duration_s*1000/timebase_ms
        self.half_period_frames = 1000/(2*frequency_hz*timebase_ms)
        print(f'half period {self.half_period_frames}')
        self.led_count = led_count
        self.frame_counter = 0
        self.background_color = background
        print(self.color.red)
        print(self.background_color.red)

    def get_next_frame(self):
        leds = []
        if self.frame_counter < self.frames_to_survive:
            # check if half period has past
            if self.frame_counter % self.half_period_frames == 0:
                #check if it is an even or odd half period
                if (self.frame_counter/self.half_period_frames)%2 == 0:
                    for i in range(self.led_count):
                        leds.append(self.color)
                        print('do this')
                else:
                    for i in range(self.led_count):
                        leds.append(self.background_color)
                        print('do that')
            # increment counter
            self.frame_counter+=1
            return leds
        else:
            return None
    
if __name__ == '__main__':
    b = BlinkingLight(100, 10, 1, 10, LedColor(50,100,100), LedColor(100,0,0))
    for i in range (20):
        ledstates = b.get_next_frame()


