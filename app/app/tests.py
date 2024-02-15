# sample tests
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    # test calc module
    def test_add_numbers(self):
        # test adding num together
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        # test subtracting num
        res = calc.subtract(1, 5)
        self.assertEqual(res, -4)
