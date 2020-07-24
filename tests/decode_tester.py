import unittest

from pybencode import exceptions
from pybencode.decode import decode, to_byte_string, to_dict, to_int, to_list


class DecodeTester(unittest.TestCase):
  def test_decode_empty_string(self):
    self.assertRaises(exceptions.InvalidBencode, decode, '')


class DecodeToIntTester(unittest.TestCase):
  def test_empty_string_to_int(self):
    self.assertRaises(exceptions.InvalidBencode, to_int, '')

  def test_invalid_bencode_to_int(self):
    self.assertRaises(exceptions.InvalidBencode, to_int, 'i0A0e')

  def test_bencode_with_no_content_to_int(self):
    self.assertRaises(exceptions.InvalidBencode, to_int, 'ie')

  def test_decode_simple_int(self):
    self.assertEqual(decode('i42e'), 42)


class DecodeToByteStringTester(unittest.TestCase):
  pass


class DecodeToListTester(unittest.TestCase):
  pass


class DecodeToDictTester(unittest.TestCase):
  pass


if __name__ == '__main__':
    unittest.main()
