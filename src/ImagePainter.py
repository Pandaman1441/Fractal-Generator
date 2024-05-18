
from tkinter import Tk,Canvas,PhotoImage, mainloop
import FractalFactory
import PaletteFactory
import sys
import time

class ImagePainter:
    def __init__(self):
        #self.__f = fractalPath
        #self.__p = palette
        pass

    def paint(self, fractalPath, palette):
        before = time.time()
        f = FractalFactory.makeFractal(fractalPath)
        fInfo = f.getInfo()
        iterations = int(fInfo['iterations'])
        p = PaletteFactory.makePalette(palette, iterations)
        pixelSize = fInfo['pixelsize']

        size = fInfo['pixels']
        window = Tk()
        canvas = Canvas(window, width=size, height=size, bg="#ffffff")
        pic = PhotoImage(width=size, height=size)
        canvas.create_image((size / 2, size / 2), image = pic, state = "normal")
        canvas.pack()

        for r in range(size, 0, -1):
            for c in range(size):
                x = fInfo['min']['x'] + c * pixelSize
                y = fInfo['min']['y'] + r * pixelSize
                I = f.getIteration(complex(x, y))
                color = p.getColor(I)
                pic.put(color, (c, size - r))
            window.update()
            print(self.pixelsWrittenSoFar(r, size), end = '\r', file = sys.stderr)
        pic.write(fInfo['imagename'])
        after = time.time()
        print(f"\nDone in {after - before:.3f} seconds.", file=sys.stderr)
        print(f"Your image was saved to " + fInfo['imagename'], file = sys.stderr)
        print("Close the image window to exit the program")
        mainloop()

    def pixelsWrittenSoFar(self, rows, size):
        portion = (size - rows) / size
        status_percent = '{:>4.0%}'.format(portion)
        status_bar_width = 34
        status_bar = '=' * int(status_bar_width * portion)
        status_bar = '{:<33}'.format(status_bar)
        return ''.join(list(['[', status_percent, ' ', status_bar, ']']))

