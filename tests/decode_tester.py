import unittest

from pybencode import exceptions
from pybencode.decode import decode


class DecodeTester(unittest.TestCase):
  def test_decode_empty_string(self):
    self.assertRaises(exceptions.InvalidBencode, decode, '')

  def test_decode_simple_int(self):
    self.assertEqual(decode('i42e'), 42)


if __name__ == '__main__':
    unittest.main()
