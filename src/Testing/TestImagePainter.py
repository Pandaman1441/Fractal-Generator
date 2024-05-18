import unittest
from ImagePainter import ImagePainter

class TestImagePainter(unittest.TestCase):
    def test_pixelsWrittenSoFar(self):
        image = ImagePainter(512, '#ffffff')
        self.assertEqual(image.pixelsWrittenSoFar(1), '[100% =================================]')
        self.assertEqual(image.pixelsWrittenSoFar(7), '[ 99% =================================]')
        self.assertEqual(image.pixelsWrittenSoFar(257), '[ 50% ================                 ]')
        self.assertEqual(image.pixelsWrittenSoFar(256), '[ 50% =================                ]')
        self.assertEqual(image.pixelsWrittenSoFar(100), '[ 80% ===========================      ]')
        self.assertEqual(image.pixelsWrittenSoFar(640), '[-25%                                  ]')
        self.assertEqual(image.pixelsWrittenSoFar(137), '[ 73% ========================         ]')
        self.assertEqual(image.pixelsWrittenSoFar(512), '[  0%                                  ]')
