from Palette import Palette
from random import randint


class RandomPalette(Palette):
    def __init__(self, iterations):
        self.__palette = []
        for i in range(iterations):
            self.__palette.append("#%06X" % randint(0, 0xFFFFFF))

    def getColor(self, n):
        return self.__palette[n]