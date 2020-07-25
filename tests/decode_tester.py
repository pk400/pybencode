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

  def test_decode_negative_int(self):
    self.assertEqual(decode('i-42e'), -42)


class DecodeToByteStringTester(unittest.TestCase):
  def test_empty_string_to_byte_string(self):
    self.assertRaises(exceptions.InvalidBencode, to_byte_string, '')

  def test_invalid_bencode_to_byte_string(self):
    self.assertRaises(exceptions.InvalidBencode, to_byte_string, ':')
    self.assertRaises(exceptions.InvalidBencode, to_byte_string, 'x:')
    self.assertRaises(exceptions.InvalidBencode, to_byte_string, ':x')
    self.assertRaises(exceptions.InvalidBencode, to_byte_string, 'x:x')


class DecodeToListTester(unittest.TestCase):
  def test_list_of_int(self):
    self.assertListEqual(decode('li42ei0ei999ee'), [42, 0, 999])

  def test_invalid_int_found(self):
    self.assertRaises(exceptions.InvalidBencode, to_list, 'li0A0ee')

  def test_nested_lists(self):
    self.assertListEqual(decode('lli42eee'), [[42]])
    self.assertListEqual(decode('lli42eli99eeee'), [[42], [99]])


class DecodeToDictTester(unittest.TestCase):
  pass


if __name__ == '__main__':
    unittest.main()
