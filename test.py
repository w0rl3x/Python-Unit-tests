import unittest

from circle import area
from circle import perimeter

class CircleAreaTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_square_mul(self):
        res = area(2)
        self.assertEqual(res, 12.566370614359173)

    def test_area_random(self):
        res = area(32767)
        self.assertEqual(res, 3373053541.855952)
    
    def test_p_zero_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_p_random1(self):
        res = perimeter(2)
        self.assertEqual(res, 12.566370614359173)
    
    def test_p_random2(self):
        res = perimeter(6)
        self.assertEqual(res, 37.69911184307752)

    def test_p_random3(self):
        res = perimeter(2147483647)
        self.assertEqual(res, 13493037698.238832)