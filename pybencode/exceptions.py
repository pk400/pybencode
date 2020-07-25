class PyBencodeException(Exception):
  '''Base exception for pybencode.'''
  pass


class InvalidBencode(PyBencodeException):
  '''Raised when pybencode failed to decode a Bencode string.'''
  pass
