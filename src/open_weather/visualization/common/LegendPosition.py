from enum import Enum

class LegendPosition(str, Enum):
    UPPER_RIGHT = "upper right"
    UPPER_LEFT = "upper left"
    LOWER_CENTER = "lower center"
    BEST = "best"