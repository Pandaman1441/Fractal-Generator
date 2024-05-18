from Royal import Royal
from Salmon import Salmon
from RandomPalette import RandomPalette

def makePalette(paletteName, iterations):
    name = paletteName.lower()
    if name == 'salmon':
        return Salmon(iterations)
    elif name == 'royal':
        return Royal(iterations)
    elif name == 'random':
        return RandomPalette(iterations)
    elif name == 'default':
        print("PaletteFactory: Creating default color palette")
        return Salmon(iterations)
    else:
        raise NotImplementedError("Invalid palette requested")


