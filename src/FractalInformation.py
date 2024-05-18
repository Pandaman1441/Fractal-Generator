class FractalInformation:
    def __init__(self):
        self.__fractalDictionary = {# phoenix fractals
                                    'phoenix': {
                                        'type': 'phoenix',
                                        'z': complex(-0.5, 0.0),
                                        'centerX': 0.0,
                                        'centerY': 0.0,
                                        'axisLen': 3.25},
                                    'peacock': {
                                        'type': 'phoenix',
                                        'z': complex(-0.5, 0.0),
                                        'centerX': -0.363287878200906,
                                        'centerY': 0.381197981824009,
                                        'axisLen': 0.0840187115019564},
                                    'monkey-knife-fight': {
                                        'type': 'phoenix',
                                        'z': complex(-0.5, 0.0),
                                        'centerX': -0.945542168674699,
                                        'centerY': 0.232234726688103,
                                        'axisLen': 0.136626506024096},
                                    'shrimp-cocktail': {
                                        'type': 'phoenix',
                                        'z': complex(-0.5, 0.0),
                                        'centerX': 0.529156626506024,
                                        'centerY': -0.3516077170418,
                                        'axisLen': 0.221204819277108},

                                    # mandelbrot fractals
                                    'elephants': {
                                        'type': 'mandelbrot',
                                        'z': complex(0, 0),
                                        'centerX': 0.3015,
                                        'centerY': -0.0200,
                                        'axisLen': 0.03},
                                    'leaf': {
                                        'type': 'mandelbrot',
                                        'z': complex(0, 0),
                                        'centerX': -1.543577002,
                                        'centerY': -0.000058690069,
                                        'axisLen': 0.000051248888},
                                    'mandelbrot': {
                                        'type': 'mandelbrot',
                                        'z': complex(0, 0),
                                        'centerX': -0.6,
                                        'centerY': 0.0,
                                        'axisLen': 2.5},
                                    'mandelbrot-zoomed': {
                                        'type': 'mandelbrot',
                                        'z': complex(0, 0),
                                        'centerX': -1.0,
                                        'centerY': 0.0,
                                        'axisLen': 1.0},
                                    'seahorse': {
                                        'type': 'mandelbrot',
                                        'z': complex(0, 0),
                                        'centerX': -0.748,
                                        'centerY': -0.102,
                                        'axisLen': 0.008},
                                    'spiral0': {
                                        'type': 'mandelbrot',
                                        'z': complex(0, 0),
                                        'centerX': -0.761335372924805,
                                        'centerY': 0.0835704803466797,
                                        'axisLen': 0.004978179931102462},
                                    'spiral1': {
                                        'type': 'mandelbrot',
                                        'z': complex(0, 0),
                                        'centerX': -0.747,
                                        'centerY': 0.1075,
                                        'axisLen': 0.002},
                                    'starfish': {
                                        'type': 'mandelbrot',
                                        'z': complex(0, 0),
                                        'centerX': -0.463595023481762,
                                        'centerY': 0.598380871135558,
                                        'axisLen': 0.00128413675654471},
                                    }
    def getDictionary(self):
        return self.__fractalDictionary

    def getFractal(self, key):
        if key in self.__fractalDictionary:
            return key
