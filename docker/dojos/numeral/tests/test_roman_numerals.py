from unittest import TestCase
import app.roman_numerals as n_romans

class tests_ToRoman(TestCase):
    def test_convert_1_to_I(self):
        decimal = 1
        expected = 'I'

        result = n_romans.to_roman(decimal)

        self.assertEqual(expected, result)
    
    def test_convert_5_to_V(self):
        decimal = 5
        expected = 'V'

        result = n_romans.to_roman(decimal)

        self.assertEqual(expected, result)
    
    def test_convert_10_to_X(self):
        decimal = 10
        expected = 'X'

        result = n_romans.to_roman(decimal)

        self.assertEqual(expected, result)

    def test_convert_50_to_L(self):
        decimal = 50
        expected = 'L'

        result = n_romans.to_roman(decimal)

        self.assertEqual(expected, result)

    def test_convert_100_to_C(self):
        decimal = 100
        expected = 'C'

        result = n_romans.to_roman(decimal)

        self.assertEqual(expected, result)
    
    def test_convert_500_to_D(self):
        decimal = 500
        expected = 'D'

        result = n_romans.to_roman(decimal)

        self.assertEqual(expected, result)

    def test_convert_1000_to_M(self):
        decimal = 1000
        expected = 'M'

        result = n_romans.to_roman(decimal)

        self.assertEqual(expected, result)
    
    def test_convert_2_to_II(self):
        roman = 2
        expected = 'II'

        result = n_romans.to_roman(roman)

        self.assertEqual(expected, result)
    
    def test_convert_3_to_III(self):
        roman = 3
        expected = 'III'

        result = n_romans.to_roman(roman)

        self.assertEqual(expected, result)
    
    def test_convert_4_to_IV(self):
        roman = 4
        expected = 'IV'

        result = n_romans.to_roman(roman)

        self.assertEqual(expected, result)

    
"""     def test_convert_3_to_III(self):
        roman = 3
        expected = 'III'

        result = n_romans.to_roman(roman)

        self.assertEqual(expected, result) """

class tests_FromRoman(TestCase):
    def test_convert_I_to_1(self):
        roman = 'I'
        expected = 1

        result = n_romans.from_roman(roman)

        self.assertEqual(expected, result)
    
    def test_convert_V_to_5(self):
        roman = 'V'
        expected = 5

        result = n_romans.from_roman(roman)

        self.assertEqual(expected, result)

    def test_convert_X_to_10(self):
        roman = 'X'
        expected = 10

        result = n_romans.from_roman(roman)

        self.assertEqual(expected, result)

    def test_convert_L_to_50(self):
        roman = 'L'
        expected = 50

        result = n_romans.from_roman(roman)

        self.assertEqual(expected, result)

    def test_convert_C_to_100(self):
        roman = 'C'
        expected = 100

        result = n_romans.from_roman(roman)

        self.assertEqual(expected, result)

    def test_convert_D_to_500(self):
        roman = 'D'
        expected = 500

        result = n_romans.from_roman(roman)

        self.assertEqual(expected, result)

    def test_convert_M_to_1000(self):
        roman = 'M'
        expected = 1000

        result = n_romans.from_roman(roman)

        self.assertEqual(expected, result)
