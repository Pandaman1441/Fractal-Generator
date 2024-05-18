

from Fractal import Fractal

class Julia(Fractal):
    def __init__(self, fractalInfo):
        self.__fInfo = fractalInfo


    def getIteration(self, c):
        z = complex(self.__fInfo['creal'], self.__fInfo['cimag'])

        for i in range(self.__fInfo['iterations']):
            c = c * c + z
            if abs(c) > 2:
                return i
        return self.__fInfo['iterations'] - 1
    def getInfo(self):
        return self.__fInfo