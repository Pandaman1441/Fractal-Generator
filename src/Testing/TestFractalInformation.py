import unittest
from FractalInformation import FractalInformation

class TestFractalInformation(unittest.TestCase):
    def test_getFractal(self):
        self.assertEqual(FractalInformation().getFractal('peacock'), 'peacock')
        self.assertEqual(FractalInformation().getFractal('shrimp-cocktail'), 'shrimp-cocktail')
        self.assertEqual(FractalInformation().getFractal('leaf'), 'leaf')
        self.assertEqual(FractalInformation().getFractal('mandelbrot-zoomed'), 'mandelbrot-zoomed')
        self.assertEqual(FractalInformation().getFractal('spiral0'), 'spiral0')
        self.assertEqual(FractalInformation().getFractal('starfish'), 'starfish')

    def test_fractalAxisLength(self):
        fractals = FractalInformation().getDictionary()
        self.assertEqual(fractals['monkey-knife-fight']['axisLen'], 0.136626506024096)
        self.assertEqual(fractals['elephants']['axisLen'], 0.03)
        self.assertEqual(fractals['mandelbrot']['axisLen'], 2.5)
        self.assertEqual(fractals['seahorse']['axisLen'], 0.008)
        self.assertEqual(fractals['spiral1']['axisLen'], 0.002)
        self.assertEqual(fractals['phoenix']['axisLen'], 3.25)

    def test_dictionaryLength(self):
        dictionary = FractalInformation().getDictionary()
        self.assertEqual(len(dictionary), 12)

    if __name__ == '__main__':
        unittest.main()
