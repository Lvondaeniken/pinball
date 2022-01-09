class Bumper:
    # current level represents the amount of collected ingredients
    current_level = 0
    # id is a unique identifier
    id = 'b0'
    
    def __init__(self, identifier, leds):
        self.id = identifier  
        self.leds = leds
        
    def increment_level(self):
        self.current_level += 1

    def reset_level(self):
        self.current_level = 0