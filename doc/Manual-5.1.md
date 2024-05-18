# Fractal Visualizer User Manual

##Starting the Fractal Visualizer
*   To start this program, navigate to the main directory of the program.
*   From there you can run the following command `python main.py [Fractal Path][Palette]`

##Inputs
### Valid Inputs
*   For this program you will have the option of entering no arguments and the program will output our default fractal with our default color palette.
*   If you want to view a different fractal, then you can enter a file path to a .frac file
    *   If no palette argument is inputted the fractal you requested will be printed out with our default color palette.
    *   These are the possible fractal types this program can output.
        *   Mandelbrot
        *   Phoenix
        *   Julia
*   If you would like to see a fractal with a different color palette, you can input the name of a color palette the program offers.
    *   This is a list of color palettes this program can use.
        *   Salmon
        *   Royal
        *   Random
### Invalid Inputs
*   Entering a file path to fractal type that is not supported will result in a error.
*   Entering a file path that does not exist will result in a error.
*   Entering a palette that is not supported will result in a error.
*   Entering a misspelling of a supported palette will also result in a error.

##Outputs
*   Ideally you entered the correct arguments and should see a new window pop up that will start printing out your fractal line by line.
*   In the console you should also see a progress bar
*   Once your fractal is finished printing the program will save a png file with the name of the fractal and how many iterations it took to create it.
*   After the program finished printing the fractal and saving your image then it will prompt you to close the fractal viewer pop up to exit the program.