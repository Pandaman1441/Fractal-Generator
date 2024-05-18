from colour import Color
from Palette import Palette

class Salmon(Palette):
    def __init__(self, iterations):
        self.__color1 = Color("lightsalmon")
        self.__color2 = Color("lightseagreen")
        self.__palette = list(self.__color1.range_to(self.__color2, iterations))

    def getColor(self, n):
        return self.__palette[n]
