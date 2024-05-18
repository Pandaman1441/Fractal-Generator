# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

##Instructions
*   This second part of the project will be to refactor the program again into a program that is more modular and easier to work with. Applying principles and methods we learned in class to make this program more streamlined.

## Requirements
*   Create a `Fractal` class and 3 sub-classes
    *   the `Fractal` class will set up the basis for all sub-class fractals, which will inherit it.
    *   This class will have a method to raise an error and close the program gracefully with an error and message we can use later to find where the error might have occured.
    *   This class will search through our list of fractals and raise an error if it is not
    *   Sub-classes
        *   These classes will define different fractals and provide the relevant information for their creation
*   Create a `FractalFactory` class
    *   This class will be where the fractal objects are created and sent back to the image painter.
    *   This class will set up the basis structure for the fractals and look through the file given to pull out the relevant information and sending it to the correct fractal type to complete the necessary information for the fractal to be created.
    *   This class will raise an error if any required data is missing from the file given.
    *   This class will also define the default fractal the program will use incase the user inputs no specific fractal
*   Create a `Palette` class and 2 sub-classes
    *   This class will be inherited to create the structure of the sub-classes
    *   This class will raise an error if a specified color is not an option
    *   Sub-classes
        *   These classes will define what color palettes are available and the colors in each palette
*   Create a `PaletteFactory` class
    *   This class will pull up the correct palette and return the palette
    *   This class will also raise an error if a given palette is not an option
    *   This class will also define a default palette the program will use incase the user does not input a specific palette.
*   Create a `ImagePainter` class
    *   This class will be the program that puts together all the previous classes together to create the outputted fractal.
    *   This class does not use an if/elif/else tree to determine which fractal should be used.

## Worries
*   Immediately after reading the instructions for about an hour I felt overwhelmed, so much so that I'm writing this before finishing all the requirements above.
*   Anyways I think if I just take each of these parts one step at a time it won't be too bad
*   It seems like I have to make several files that are just going change small things then return those changes so maybe like half of the files will be really easy. hopefully.
*   Ok coming back after writing all the requirements, I feel a bit better the program is mainly the fractal and palette factory.


## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

*   I'm going to have the palette and fractal subclasses in the same analysis because they'll take the same input and give the same output.
Main analysis
```
DESCRIPTION:
    Takes input from user and checks how many arguments were given, then send the filepath and palette to imagePainter
PARAMETERS:
    Input : str
        Input will be either nothing, a filepath and a string, or just a filepath
RETURNS:
    Returns nothing
```

ImagePainter analysis
```
DESCRIPTION:
    Gets information from fractal and palette factory to draw the fractal
PARAMETERS:
    FilePath : str
        sends the filePath to fractalFactory to parse through the file
    Palette : str
        sends the name of the palette requested to paletteFactory
    Iteration : int
        iteration count from fractal class
    Color : str
        color for each pixel from palette class
RETURNS:
    Returns fractal image
```

FractalFactory analysis
```
DESCRIPTION:
    Creates a dictionary with the information from the .frac file and calls which fractal to make
PARAMETERS:
    FilePath : str
        file the class will turn into dictionary for easier use
RETURNS:
    Returns fractal dictionary
```

Fractal analysis
```
DESCRIPTION:
    Abstract fractal class raises errors
PARAMETERS:
    C : complex
        this class will be empty but this is for the subclasses
RETURNS:
    Returns error
```

Fractals analysis
```
DESCRIPTION:
    Gets iteration count for a fractal
PARAMETERS:
    C : complex
        complex number for each pixel
RETURNS:
    Returns a iteration number for fractal
```

PaletteFactory analysis
```
DESCRIPTION:
    Checks for valid palette name and creates it if it is
PARAMETERS:
    Palette : str
        name of the desired palette
    n : int
        Iteration number for a fractal
RETURNS:
    Returns color palette list
```

Palette analysis
```
DESCRIPTION:
    Abstract class for palette subclasses and raises errors
PARAMETERS:
    n : int
        this class will be empty but this is for the subclasses
RETURNS:
    Returns errors
```

Palettes analysis
```
DESCRIPTION:
    Creates a color palette based on the iteration count
PARAMETERS:
    n : int
        iteration count for how many colors are needs
RETURNS:
    Returns specific color or whole palette
```


## Phase 2: Design *(30%)*

main
```
if sys.argv < 2
    ImagePainter.paint(default, default)
elif sys.argv == 2
    ImagePainter.paint(sys.argv(1), default)
else
    ImagePainter.paint(sys.argv(1), sys.argv(2))
```

ImagePainter
```
class ImagePainter

def __init__(fractalPath, palette)
    self.f = fractalPath
    self.p = palette
def paint
    f = FractalFactory.makeFractal(self.f)
    fInfo = Fractals.getInfo
    iter = fInfo[iterations]
    p = paletteFactory.makePalette(self.p, iter)
    pixelSize = fInfo[pixelSize]

    size = fInfo[pixels]
    window = Tk
    canvas = canvas(window, size, size, white)
    pic = PhotoImage(size, size)
    canvas.create image((size / 2, size / 2), pic, normal)

    for r in range(size, 0, -1)
        for c in range(size)
            x = minX + c * pixelSize
            y = minY + r * pixelSize
            I = fractal.getIteration(complex(x,y)
            color = palette.getColor(I)
            pic.put(color, (c, size - r)
        window.update

        print(pixelsWrittenSoFar(r), end = '\r', file = sys.stderr)

        pic.write(fInfo[imagename] + fInfo[iterations]
```

FractalFactory
```
def makeFractal(fractalPath)
    f = open(fractalPath)
    requirements = [type,centerX,centerY,axislength,pixels,iterations]
    juliaReqs = [creal,cimag]
    fDictionary = {}
    for line in f:
        if line == ''
            pass
        elif line[0] == '#'
            pass
        else
            line = line.strip()
            temp = line.split(':')
            reqsGood = checkReqs(temp)
            fDictionary[reqsGood[0]] = reqsGood[1]
    f.close()

    fDictionary = convertFile(fDictionary, fractalPath)

    if fDictionary[type] == mandelbrot
        return mandelbrot(fDictionary)
    elif fDictionary[type] == phoenix
        return phoenix(fDictionary)
    elif fDictionary[type] == newton
        return newton(fDictionary)

def checkReqs(temp)
    if temp[0] == type and temp[1] is not numeric
        return type, temp[1]
    elif temp[0] == pixels or iterations and temp[1] is numeric
        return temp[0], int(temp[1])
    elif temp[0] == centerx or centery or axislength
        return temp[0], float(temp[1])
    elif temp == creal or cimag and is numeric
        return temp[0], float(temp[1])

def convertFile(fDictionary, fractalPath)
    newDictionary = {
        type : fDictionary[type]
        pixels : fDictionary[pixels]
        axislength : fDictionary[axislength]
        pixelsize : fDictionary[axislength] / fDictionary[pixels]
        iterations : fDictionary[iterations]
        min : {
            x : fDictionary[centerx] - abs(fDictionary[axislength] / 2),
            y : fDictionary[centery] - abs(fDictionary[axislength] / 2)
        }
        max : {
            x : fDictionary[centerx] + abs(fDictionary[axislength] / 2),
            y : fDictionary[centery] + abs(fDictionary[axislength] / 2)
        }
        imagename : fractalPath.split(/)[-1].split(.)[0] + 'png'
        }
    if newDictionary[type] == julia
        newDictionary[creal] = fDictionary[creal]
        newDictionary[cimag] = fDictionary[cimag]
    return newDictionary
def defaultFractal
    fDictionary = {
        'type': fractal,
        'pixels' : 400,
        'axislength' : 5.0,
        'pixelsize' : 0.00500,
        'iterations' : 111,
        'min' : {'x' : -2, 'y' : -2}
        'max' : {'x' : 2, 'y' : 2}
        'imagename' : fractalName
    }
    return fDictionary
```

Fractal
```
class Fractal

def __init__
    raise NotImplementedError

def count
    raise NotImplementedError
```

Fractals
```
class fractalName

def __init__(fractalInfo)
    fInfo = fractalInfo

def getIteration(c)
    z = complex(0.0, 0.0)
    for i in range(fInfo[iterations])
        z = z * z + c
        if abs(z) > 2
            return i
    return fInfo[iterations] - 1
```

PaletteFactory
```
def makePalette(paletteName, iterations)
    if paletteName == 'paletteName1'
        return paletteName1(iterations)
    elif paletteName == 'paletteName2'
        return paletteName2(iterations)
    elif paletteName == 'paletteName3'
        return paletteName3(iterations)
def defaultPalette(iterations)
    return paletteName3(iterations)
```

Palette
```
class palette

def __init__(iterations)
    raise NotImplementedError

def getColor
    raise NotImplementedError
```

Palettes
```
class paletteName

def __init__(iterations)
    color1 = color1
    color2 = color2
    palette = list(color1.range_to(color2, iterations)

def getColor(n)
    return palette[n]
```

*   some parts of this phase look a bit too much like normal code but it was just easier to write it up this way.


## Phase 3: Implementation *(15%)*

## Translating
*   So I work imagePainter and main but I realized its gonna be better to work from the bottom up so i'm gonna do fractal and palette factory last
*   Doing my palettes and I was able to find a way online to show all the colors pythons can use, so I spent some time messing with the colors I'm gonna use.
*   I found a way to make a list of random colors so I'll have an extra palette option do that and have my default be a consistent one.
*   When I wrote the pseudocode for the fractal factory I wrote it close to real code to make it easier to think through it all and so I copy pasted it into a file and formatted it so theres no immediate errors but I don't know if it actually works

## Post Translation
*   I've transferred all my pseudocode over and made some edits and there's no errors but there is also no output.
*   ok so I was giving my image painter default but not as a string so nothing was happening also i was calling a method that i forgot to write
*   So my hard coded fractal was working but my code for converting the .frac files was not and i kept getting an index error. I think it was because there were spaces in front of some of the numbers but I striped the list again and it's working now
*   I was working on the phoenix fractal get iteration and was trying to make it simpler but i opted just to use my code from the last part and it worked so i'm just going to leave it as is
*   I think I'm done there's probably some problems but i'm able to get my 3 fractals to work and my palettes all work as well so I'm going to move on to the next phase.


## Phase 4: Testing & Debugging *(30%)*

##Testing
*   so I still need to add the text that appears while the image is loading and other stuff
*   Ok user interface stuff looks good and is working as it should
*   Testing correct inputs
    *   Default fractal and palette
    ```
    $ python src/main.py
    FractalFactory: Creating default fractal
    PaletteFactory: Creating default color palette
    [100% =================================]
    Done in 28.723 seconds.
    Your image was saved to mandelbrot.png
    Close the image window to exit the program
    ```
    *   Specific fractal with default palette
    ```
    $ python src/main.py data/mandelbrot.frac
    PaletteFactory: Creating default color palette
    [100% =================================]
    Done in 29.273 seconds.
    Your image was saved to mandelbrot.png
    Close the image window to exit the program
    ```
    *   Specific fractal with specific palette
    ```
    $ python src/main.py data/mandelbrot.frac random
    [100% =================================]
    Done in 20.954 seconds.
    Your image was saved to mandelbrot.png
    Close the image window to exit the program
    ```
*   Getting correct errors
    *   missing or inaccessible file
    ```
    $ python src/main.py data/NOT_EXIST ColorCube
    Traceback (most recent call last):
      File "C:\Users\Owner\Desktop\cs1440\cs1440-assn5\src\main.py", line 38, in <module>
        ImagePainter().paint(sys.argv[1], sys.argv[2])
      File "C:\Users\Owner\Desktop\cs1440\cs1440-assn5\src\ImagePainter.py", line 16, in paint
        f = FractalFactory.makeFractal(fractalPath)
      File "C:\Users\Owner\Desktop\cs1440\cs1440-assn5\src\FractalFactory.py", line 11, in makeFractal
        f = open(fractalPath)
    FileNotFoundError: [Errno 2] No such file or directory: 'data/NOT_EXIST'
    ```
    *   Invalid palette name
    ```
    $ python src/main.py data/mandelbrot.frac NOT_EXIST
    Traceback (most recent call last):
      File "C:\Users\Owner\Desktop\cs1440\cs1440-assn5\src\main.py", line 38, in <module>
        ImagePainter().paint(sys.argv[1], sys.argv[2])
      File "C:\Users\Owner\Desktop\cs1440\cs1440-assn5\src\ImagePainter.py", line 19, in paint
        p = PaletteFactory.makePalette(palette, iterations)
      File "C:\Users\Owner\Desktop\cs1440\cs1440-assn5\src\PaletteFactory.py", line 17, in makePalette
        raise NotImplementedError("Invalid palette requested")
    NotImplementedError: Invalid palette requested
    ```
*   I ran through the invalid.frac file and got all raised an error everytime it needed to, i just changed values as i went through
*   I'm going to write new unit tests and run those then that should be it.
*   I was looking in the instructions for how many unit tests there should be and it doesn't specify, they are only mentioned once in the design phase
*   Either way i'm going to write unit tests for the fractals, that should be simple enough.
*   I made some new unit test just to test what iteration some complex numbers give
    ```
    $ python src/runTests.py
    test_Iterations (Testing.TestMandelbrot.TestMandelbrot) ... ok
    test_Iterations (Testing.TestPhoenix.TestPhoenix) ... ok
    test_Iterations (Testing.TestJulia.TestJulia) ... ok

    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK
    ```

## Phase 5: Deployment *(5%)*

**Deliver:**

#Valididated

## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.

*   My worst written part is probably my fractal factory just because there is a lot going on in that file so there bound to be some confusing part.
*   In my fractal factory where I had it parse through the .frac file and check the values, I couldn't understand why if I had it check centerX and centerY before pixels and iteration it would cause an error
*   These modular programs feel a lot easier to take apart and find where some errors are occurring
*   I think my documentation is pretty not in depth but there is a lot of what is going through my thought process, but it's understandable at least to me.
*   Adding new features would be pretty easy for this one i think if it new fractals or palettes supper easy, if it like redoing the interface it might be while longer but everything works so you only have to work on one file ideally.
*   I think because of how fractals work it runs poorly, I don't know if it's just my laptop or that's just how fractals are but I'm sure there are better ways to make it perform better.


