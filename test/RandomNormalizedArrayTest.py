import unittest

from Util.RandomNormalizedArray import RandomNormalizedArray


class RandomNormalizedArrayTest(unittest.TestCase):

    def test_get(self):
        randomNormalizedArray = RandomNormalizedArray(10)
        array = randomNormalizedArray.get()
        sum = 0.0
        for d in array:
            sum += d
        self.assertAlmostEqual(1.0, sum, 10)


if __name__ == '__main__':
    unittest.main()
