# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

## Instructions
*   This first part of the project will be to clean up the existing program while keep its functionality the same. Go through the given code and make the code look cleaner

## Requirements
*   Read through the code and understand it, write down anything you think is wrong with it and then make adjustments
*   the following are possible code smells
    *   numeric literals that don't have context or meaning
    *   global variables
    *   poorly named variables
    *   comments tell to much
    *   false comments
    *   when a function or method have too many parameters
    *   functions or methods that have too much
    *   too many nested if else statements
    *   spaghetti code
    *   redundant code
    *   code that is not being used
*   Rewrite the given code to make it cleaner while keeping the same functionality.
*   Write a UML class diagram and User manual


## Worries
*   I went through the files we were given and there is a lot to look through
*   So what I'm worried about is sometimes I can barely understand how my code works so this might take a bit to figure out.
*   Without looking very much I'm pretty confused what the difference between mandelbrot and phoenix are.
*   But thinking about what overview of this assignment it doesn't sound difficult.


## Phase 1: System Analysis *(10%)*

## Inputs
*   The inputs for this program will mainly be through the command line
*   The inputs will consist of which picture the user wants printed to their screen

## Outputs
*   Outputs for this program will just be the pictures the user requested
*   If the user doesn't specify which picture the program will output a list of possible pictures it can output.

Main class Analysis
```
DESCRIPTION:
    Takes input from user and uses input to find which image to print out
PARAMETERS:
    input : str
        input will be used to call the correct class, phoenix or mandelbrot
RETURNS:
    Returns the image requested

```

FractalInformation class Analysis
```
DESCRIPTION:
    Defines the dictionary containing fractal names and other important info
PARAMETERS:
    fractalInfo : str
        This will just be some way to find which info to find
RETURNS:
    Returns values of the called dictionary
```

Mandelbrot class Analysis
```
DESCRIPTION:
    Prints out a mandelbrot fractal image
PARAMETERS:
    fractalInfo : int
        This will be the info from FractalInformation to create the fractal specified
RETURNS:
    Returns the info of what the fractal looks like to ImagePainter
```

Phoenix class Analysis
```
DESCRIPTION:
    Prints out a phoenix fractal image
PARAMETERS:
    fractalInfo : int
        This will be the info from FractalInformation to create a phoenix fractal specfied by the user
RETURNS:
    Returns the info of what the fractal looks like to ImagePainter
```

Palette class Analysis
```
DESCRIPTION:
    This is the collection of colors that can be used for the images
PARAMETERS:
    fractalInfo : int
        This will be info detailing what color each pixel should be as it printed out
RETURNS:
    returns what color each pixel will be
```

ImagePainter class Analysis
```
DESCRIPTION:
    This class draws the image
PARAMETERS:
    Cords : int
        this will be the values for each coordinate in the grid to draw the fractal with color
RETURNS:
    returns the finished image
```

*   fractalInfo is just a placeholder because I'm not sure what info each fractal needs.

## Phase 2: Design *(30%)*


Main
```
if length of sys.argv < 2
    print("{}" . format("Please provide the name of a fractal as an agrument")
    for i in fractals
        print fractal name
    exit
else if sys.argv not in fractals
    print("ERROR:" , sys.argv, "is not a valid fractal")
    print("Please enter one of the following valid fractals")
    for i in fractals:
        print fractal name
    exit
else
    type = getFractal(sys.argv)
    if type == Mandelbrot:
        Mandelbrot(type, sys.argv)
    else if type == Phoenix:
        Phoenix(type, sys.argv)
```

FractalInformation
```
Fractals = {Phoenix fractals : {"centerX" : int,"centerY : int, "axisLength" : int}, MandelBrot fractals : {"centerX" : int, centerY : int, axisLength : int}
def getDictionary()
    return Fractals

def getFractal(fractalName)
    if fractalName in Fractals:
        return name
```

ImagePainter
```
def imagePainter(size, bg)
    window = TK()
    canvas = Canvas(window, width = size, height = size, bg = w)
    canvas.pack()
    pic = PhotoImage(width = size, height = size)
    canvas.create_image((size/2, size/2), image = pic, state = normal)

def paint(minX, minY, pixelSize, size, z)
    for r in range(size, 0, -1):
        for c in range(size)
            x = min[0] + c * size
            y = min[1] + r * size
            iter =
    pic.put(color, (col, size - row))

def update()
    window.update()

def makePNG(fractal)
    pic.write(f"{fractal}.png")




```

Fractals (this will be the code for both mandelbrot and phoenix fractals)
```
size = 512
white = ' '
def fractal(key, fractalName)
    image = imagePainter.imagePainter(size, white)
    minX = key[centerX] - (key[axisLen] / 2.0)
    maxX = key[centerX] + (key[axisLen] / 2.0)
    minY = key[centerY] - (key[axisLen] / 2.0)
    maxY = key[centerY] + (key[axisLen] / 2.0)
    z = key[z]
    pixelSize = abs(maxX - minX) / 512
    before = time()
    image.paint(minX, minY, pixelSize, size, z)
    after = time()
    print(f"\n Done in {after - before:.3f} seconds!", file = sys.stderr)
    image.writePNG(fractalName)
    print(f"Wrote picture {fractalName}.png", file = sys.stderr)
    Print("Close the image window to exit the program", file = sys.stderr)
    mainloop()


def getIteration(c, z):
    if z == complex(0.0,0.0): # mandelbrot
        for i in range(115):
            z = z * z + c
            if abs(z) > 2
                return i
        if i >= 115:
            i = 115 - 1
        return i

    if z == complex(-0.5,0.0): # phoenix
        for i in range(102):
            z = z * z + c
            if abs(z) > 2:
                return i
        return 102

def pixelsWrittenSoFar(rows, cols)
    portion = (512) - rows) / 512
    pixels = (512 - rows) * 512
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[',status_percent, ' ', status_bar, ']']))

```

Palette
```
def palette()
    palette = [colors]

def getColor(p)
    return palette[p]

def getSize()
    return len(palette)
```

*   A lot of the code above I just pulled from the code we already have, if the function works without much changes I basically copied it over.

## Phase 3: Implementation *(15%)*

## Translating
*   main is working the same, if you enter no fractal. everything else is not done yet so i can't test anything else yet
*   I forgot to write my paint function
*   writing my imagepainter method and i'm not sure how to use get iteration and palette without using eachother in their classes
*   ok so if I have image painter get the interations because it seems like a lot of extra writing to have imagePainter to also try to differentiate between phoenix or mbrot
*   I'm going to make this change them go back and add the changes to my pseudocode and my UML diagram.
*   Wait no I'm just now remember why I wrote it like that, imagePainter calls getIteration and it returns an I and we pass the I to palette to get the color
*   I think Mandelbrot, imagepainter are done, palette and fractalinfo are for sure done. so I'm going to try to test a mandelbrot fractal
*   ran the command and nothing happened so i'm not quite sure what to do now
*   ok so in main i had type == input in dictionary, which just made type = true instead of it being a mandelbrot or phoenix fractal.
*   ran the leaf fractal and it came out in a different color but it looked the same, i then tried mandelbrot and it got an index error
*   I'm going to write up phoenix and then that'll be everything translated i think.
*   OK basically just copy pasted phoenix from mandelbrot, had to change some numbers but it works at least kinda

## Post Translation
*   So the program kinda works, for phoenix and mandelbrot i get an index error in get color which should be from my interation count
*   ok yea so i went through all the fractals and only leaf finished printing out and it took 40 seconds so i think the problem is with how i'm doing my getIteration methods.
*   I think my best bet is too instead of trying to hard code the numbers i'll try to simplify them and put them in imagePainter instead of each fractal class
*   I've changed getIteration into getPixelColor and it just gets the color for each iteration instead of having two call for different methods
*   Mandelbrot fractals seem to work and i cmp'ed them with my backups and they are the same but I don't know how to include the palette for the phoenix fractals
*   My phoenix fractals also seem to be broken
*   I think that took me 2 hours to figure out how the phoenix fractal worked, I don't think i understand it fully still, I just took as much of the code that worked and put in my getPixelColor method
*   I'm going to run through all the fractals and then compare them, and if they all check out then i'll call this phase done.
*   All the fractals looked the same and all the mandelbrot fractals came out the same but the phoenix fractals were different slightly
*   Ok so I was trying to just use the len function on the palette for phoenix fractals but the number of colors in the palette is different from the number the given code uses
*   the palette in the original phoenix_fractal has 111 colors but when getting the iteration they range to 102 and not the 111 which was what I was doing
*   Either way all the new pngs are the same as the old ones now.

## Phase 4: Testing & Debugging *(30%)*

For this phase I'm gonna make sure my unit tests are good then run through them for testing.

## Testing
*   Ok so i'm trying to change method names but for the get color of pixel test I have that just being getIteration so it doesn't return a string just an integer.
*   So I ran those tests to get the int values of each color and replaced them as the answer.
*   I'm going to try to write a test for each file, right now I have two for each fractal file so four total
*   Wrote basically 8 new tests because the old ones had so many things that I changed or turned into other methods
*   Anyways running all the unit tests passes now
```
$ python runTests.py
test_getIteration (Testing.TestMandelbrot.TestMandelbrot) ... ok
test_pixelsWrittenSoFar (Testing.TestMandelbrot.TestMandelbrot) ... ok
test_colorOfThePixel (Testing.TestPhoenix.TestPhoenix) ... ok
test_pixelsWrittenSoFar (Testing.TestPhoenix.TestPhoenix) ... ok
test_paletteColors (Testing.TestPalette.TestPalette) ... ok
test_paletteLengths (Testing.TestPalette.TestPalette) ... ok
test_fractalAxisLength (Testing.TestFractalInformation.TestFractalInformation) ... ok
test_getFractal (Testing.TestFractalInformation.TestFractalInformation) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.003s

OK

```

## Phase 5: Deployment *(5%)*


## Phase 6: Maintenance


*   I think most of the code is fine, I'm not the best coder so I can't really say its well written but my phoenix getIteration was the most confusing to me and it mix mash of the starter code and me trying to make it fit in what I had already written.
*   My documentation for the most part is fine, I haven't seen any other SPD so I don't know if i have too much or too little. But it should make sense just reading down
*   I think have this program split into parts definitely helps to find where you could put new code or where some problems might occur
*   I think someone else could probably take my code and refactor it again to be better but I this is all I've got so hopefully its enough.

