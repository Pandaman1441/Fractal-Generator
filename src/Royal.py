
from colour import Color
from Palette import Palette

class Royal(Palette):
    def __init__(self, iterations):
        self.__color1 = Color("darkmagenta")
        self.__color2 = Color("goldenrod")
        self.__palette = list(self.__color1.range_to(self.__color2, iterations))

    def getColor(self, n):
        return self.__palette[n]
