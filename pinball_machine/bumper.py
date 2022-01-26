class Bumper:
    def __init__(self, identifier: str, leds: list):
        self.id = identifier  
        self.leds = leds
        
    def increment_level(self):
        self.current_level += 1

    def reset_level(self):
        self.current_level = 0