import unittest
from Palette import Palette

class TestPalette(unittest.TestCase):
    def test_paletteLengths(self):
        self.assertEqual(Palette().getSize(1), 111)
        self.assertEqual(Palette().getSize(2), 111)

    def test_paletteColors(self):
        self.assertEqual(Palette().getColor(1,110), '#e8283f')
        self.assertEqual(Palette().getColor(1,2), '#baf12e')
        self.assertEqual(Palette().getColor(1,9), '#e0ceaf')
        self.assertEqual(Palette().getColor(1,30), '#f1da2e')
        self.assertEqual(Palette().getColor(1,56), '#deb69f')
        self.assertEqual(Palette().getColor(1,38), '#e1bc7e')
        self.assertEqual(Palette().getColor(1,12), '#e7ddd7')
        self.assertEqual(Palette().getColor(1,10), '#e1d1bd')
        self.assertEqual(Palette().getColor(2,5), '#FFEBA7')
        self.assertEqual(Palette().getColor(2,0), '#FFE4B5')
        self.assertEqual(Palette().getColor(2,1), '#FFE5B2')
        self.assertEqual(Palette().getColor(2,34), '#9AFF53')
        self.assertEqual(Palette().getColor(2,101), '#004E91')
        self.assertEqual(Palette().getColor(2,2), '#FFE6AF')
        self.assertEqual(Palette().getColor(2,32), '#A7FF59')


    if __name__ == '__main__':
        unittest.main()