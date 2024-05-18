

import unittest
from Julia import Julia


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestJulia(unittest.TestCase):
    def test_Iterations(self):
        testJ = Julia({  'type': 'julia',
                        'creal': -1.0125,
                        'cimag': 0.275,
                        'pixels': 1024,
                        'centerx': 0.0,
                        'centery': 0.0,
                        'axislength': 4.0,
                        'iterations': 78
                      })
        self.assertEqual(testJ.getIteration(complex(0,0)), 77)
        self.assertEqual(testJ.getIteration(complex(.98, .138)), 17)
        self.assertEqual(testJ.getIteration(complex(.56, .19)), 4)
        self.assertEqual(testJ.getIteration(complex(-.68, .49)), 3)
        self.assertEqual(testJ.getIteration(complex(-.37, -.81)), 1)


if __name__ == '__main__':
    unittest.main()