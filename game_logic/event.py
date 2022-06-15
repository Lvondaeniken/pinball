from enum import Enum, auto
class PinballEvent(Enum):
    BUMPER1_HIT = auto()
    BUMPER2_HIT = auto()
    BUMPER3_HIT = auto()
    TARGET1_HIT = auto()
    TARGET2_HIT = auto()
    TARGET3_HIT = auto()
    KICKER_L_ENABLE = auto()
    KICKER_R_ENABLE = auto()
    BALLSHOOTER_ENABLE = auto()
    
    