import unittest

from pybencode import exceptions
from pybencode.decode import decode


class DecodeTester(unittest.TestCase):
  def test_convert_empty_string(self):
    self.assertRaises(exceptions.InvalidBencode, decode, '')


if __name__ == '__main__':
    unittest.main()
