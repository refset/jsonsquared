from __future__ import unicode_literals

from jsonsquared.csv_string import has_value, decode, decode_list
from jsonsquared.errors import ParseFailure

try:
    import unittest2 as unittest
except ImportError:
    import unittest
from decimal import Decimal

class TestHasValue(unittest.TestCase):
    def test_has_value(self):
        self.assertTrue(has_value('wat'))

    def test_empty_string(self):
        self.assertFalse(has_value(''))

    def test_whitespace_string(self):
        self.assertFalse(has_value(' \t\r\n'))


class TestDecode(unittest.TestCase):
    def test_no_value_raises_valueerror(self):
        self.assertRaises(ValueError, decode, '  ')

    def test_null(self):
        self.assertEquals(decode(' null\n'), None)

    def test_true(self):
        self.assertEquals(decode('true '), True)

    def test_false(self):
        self.assertEquals(decode('\N{NO-BREAK SPACE} false'), False)

    def test_empty_object(self):
        self.assertEquals(decode(' {} '), {})

    def test_null_is_case_sensitive(self):
        self.assertEquals(decode('Null'), 'Null')

    def test_true_is_case_sensitive(self):
        self.assertEquals(decode('TRUE'), 'TRUE')

    def test_false_is_case_sensitive(self):
        self.assertEquals(decode('falsE'), 'falsE')

    def test_empty_object_no_internal_whitespace_allowed(self):
        self.assertEquals(decode(' { } '), '{ }')

    def test_natural_number(self):
        self.assertEquals(decode('42'), Decimal('42'))

    def test_negative_integer(self):
        self.assertEquals(decode('-9'), Decimal('-9'))

    def test_decimal_number(self):
        self.assertEquals(decode('0.0009'), Decimal('0.0009'))

    def test_exponent_number(self):
        self.assertEquals(decode(-1.96e-20), Decimal('-1.96e-20'))
