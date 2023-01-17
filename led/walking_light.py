from led.animations import AnimationInterface
from led.color import LedColor


class WalkingLight(AnimationInterface):
    def __init__(self, timebase_ms, duration_s, led_count, color: LedColor):
        self.color = color
        self.timebase_ms = timebase_ms
        self.duration_s = duration_s
        self.led_count = led_count
        self.frame_counter = 0
        self.frames_to_survive = self.duration_s * 1000 / timebase_ms
        self.frames_per_led = self.frames_to_survive / self.led_count
        self.on_index = 0
        self.background_color = LedColor(0, 0, 0)
        self.led_states = []
        for _ in range(self.led_count):
            self.led_states.append(self.background_color)

    def set_background(self, color):
        self.background_color = color
        for led in self.led_states:
            led = color

    def get_next_frame(self):
        self.frame_counter += 1
        if self.frame_counter == self.frames_per_led:
            self.on_index += 1
            self.frame_counter = 0
        self.led_states[self.on_index] = self.color
        if self.on_index > 0:
            self.led_states[self.on_index - 1] = self.background_color
        return self.led_states
