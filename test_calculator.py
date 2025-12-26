import unittest
from unittest.mock import MagicMock
import calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):


        calculator.clear_all()


        calculator.label = MagicMock()


        self.screen_data = {"text": "0"}


        def get_item(key):
            return self.screen_data[key]


        def set_item(key, value):
            self.screen_data[key] = value


        calculator.label.__getitem__.side_effect = get_item
        calculator.label.__setitem__.side_effect = set_item

    def test_addition(self):
        # 5 + 3 = 8
        calculator.button_clicked("5")
        calculator.button_clicked("+")
        calculator.button_clicked("3")
        calculator.button_clicked("=")
        self.assertEqual(self.screen_data["text"], "8")

    def test_subtraction(self):
        # 10 - 2 = 8
        calculator.button_clicked("1")
        calculator.button_clicked("0")
        calculator.button_clicked("-")
        calculator.button_clicked("2")
        calculator.button_clicked("=")
        self.assertEqual(self.screen_data["text"], "8")

    def test_multiplication(self):
        # 4 * 4 = 16
        calculator.button_clicked("4")
        calculator.button_clicked("×")
        calculator.button_clicked("4")
        calculator.button_clicked("=")
        self.assertEqual(self.screen_data["text"], "16")

    def test_division(self):
        # 20 / 5 = 4
        calculator.button_clicked("2")
        calculator.button_clicked("0")
        calculator.button_clicked("÷")
        calculator.button_clicked("5")
        calculator.button_clicked("=")
        self.assertEqual(self.screen_data["text"], "4")

    def test_clear_button(self):
        # Type 123, then Clear, should be 0
        calculator.button_clicked("1")
        calculator.button_clicked("2")
        calculator.button_clicked("3")
        calculator.button_clicked("AC")
        self.assertEqual(self.screen_data["text"], "0")

    def test_decimal(self):
        # 1.5
        calculator.button_clicked("1")
        calculator.button_clicked(".")
        calculator.button_clicked("5")
        self.assertEqual(self.screen_data["text"], "1.5")

    def test_multiple_digits(self):
        # Type 789
        calculator.button_clicked("7")
        calculator.button_clicked("8")
        calculator.button_clicked("9")
        self.assertEqual(self.screen_data["text"], "789")


if __name__ == '__main__':
    unittest.main()