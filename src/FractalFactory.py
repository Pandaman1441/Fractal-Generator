
from Mandelbrot import Mandelbrot
from Phoenix import Phoenix

from Julia import Julia

def makeFractal(fractalPath):
    if fractalPath == 'default':
        fDictionary = defaultFractal()
    else:
        f = open(fractalPath)
        requirements = ['type','centerx','centerx','axislength','pixels','iterations']
        juliaReqs = ['creal','cimag']
        fDictionary = {}
        for line in f:
            line = ''.join(line.split())
            if line == '':
                pass
            elif line[0] == '#':
                pass

            else:
                line = line.strip()
                temp = line.split(':')
                reqsGood = checkReqs(temp)
                fDictionary[reqsGood[0]] = reqsGood[1]
        f.close()

        for check in requirements:
            if check not in fDictionary:
                raise RuntimeError("The '" + check + "' parameter is missing")
        if fDictionary['type'] == 'julia':
            for check in juliaReqs:
                if check not in fDictionary:
                    raise RuntimeError("The '" + check + "' parameter is missing")
        fDictionary = convertFile(fDictionary)



    if fDictionary['type'] == 'mandelbrot':
        return Mandelbrot(fDictionary)
    elif fDictionary['type'] == 'phoenix':
        return Phoenix(fDictionary)
    elif fDictionary['type'] == 'julia':
           return Julia(fDictionary)

def checkReqs(temp):
    fractals = ['mandelbrot','phoenix','julia']
    if temp[0].lower() == 'type':
        if temp[1].lower() in fractals:
            return 'type', temp[1].lower()
        else:
            raise RuntimeError("Fractal type '" + temp[1] + "' is not supported")
    elif temp[0].lower() == 'pixels' or 'iterations'and temp[1].isnumeric():
        try:
            return temp[0].lower(), int(temp[1])
        except:
            raise RuntimeError("The Value of the '" + temp[0] + "' parameter is not a integer")
    elif temp[0].lower() == 'centerx' or 'centery' or 'axislength':
        try:
            return temp[0].lower(), float(temp[1])
        except ValueError:
            raise RuntimeError("The Value of the '" + temp[0] + "' parameter is not a number")
    elif temp[0].lower() == 'creal' or 'cimag' and temp[1].isnumeric():
        try:
            return temp[0].lower(), float(temp[1])
        except:
            raise RuntimeError("The Value of the '" + temp[0] + "' parameter is not a number")
    else:
        raise NotImplementedError

def convertFile(fDictionary):
    newDictionary = {
        'type' : fDictionary['type'],
        'pixels' : int(fDictionary['pixels']),
        'axislength' : float(fDictionary['axislength']),
        'pixelsize' : fDictionary['axislength'] / fDictionary['pixels'],
        'iterations' : int(fDictionary['iterations']),
        'min' : {
            'x' : fDictionary['centerx'] - abs(fDictionary['axislength'] / 2),
            'y' : fDictionary['centery'] - abs(fDictionary['axislength'] / 2)
        },
        'max' : {
            'x': fDictionary['centerx'] + abs(fDictionary['axislength'] / 2),
            'y' : fDictionary['centery'] + abs(fDictionary['axislength'] / 2)
        },
        'imagename' : fDictionary['type'] + '.png'
        }
    if newDictionary['type'] == 'julia':
        newDictionary['creal'] = float(fDictionary['creal'])
        newDictionary['cimag'] = float(fDictionary['cimag'])
    return newDictionary
def defaultFractal():
    print("FractalFactory: Creating default fractal")
    fDictionary = {
        'type': 'mandelbrot',
        'pixels' : 640,
        'axislength' : 4.0,
        'pixelsize' : 0.00625,
        'iterations' : 100,
        'min' : {'x' : -2.0, 'y' : -2.0},
        'max' : {'x' : 2.0, 'y' : 2.0},
        'imagename' : 'mandelbrot.png'
    }
    return fDictionary
