from typing import Optional
from led_handling.animations import AnimationInterface
from led_handling.led_color import LedColor


class BlinkingLight(AnimationInterface):
    def __init__(
        self,
        timebase_ms: int,
        duration_s: int,
        frequency_hz: int,
        led_count: int,
        color: LedColor,
        background: LedColor,
    ):
        self.color = color
        self.frames_to_survive = round(duration_s * 1000 / timebase_ms)
        self.half_period_frames = round(1000 / (2 * frequency_hz * timebase_ms))
        print(f"{self.frames_to_survive=}")
        print(f"{self.half_period_frames=}")
        self.led_count = led_count
        self.frame_counter = 0
        self.background_color = background
        print(f"{self.background_color=}")
        print(f"{self.color=}")
        self._set_to_color(self.background_color)

    def get_next_frame(self) -> Optional[list[LedColor]]:
        if self.frame_counter < self.frames_to_survive:
            # check if half period has past
            if self.frame_counter % self.half_period_frames == 0:
                # check if it is an even or odd half period
                if (self.frame_counter / self.half_period_frames) % 2 == 0:
                    self._set_to_color(self.color)
                else:
                    self._set_to_color(self.background_color)
            self.frame_counter += 1
            return self.led_states
        elif self.frame_counter == self.frames_to_survive:
            self._set_to_color(LedColor(0, 0, 0))
            self.frame_counter += 1
            return self.led_states
        else:
            return None

    def _set_to_color(self, color: LedColor):
        self.led_states: list[LedColor] = []
        for _ in range(self.led_count):
            self.led_states.append(color)
