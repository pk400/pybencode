def decode(bencode):
  '''
  Convert a Bencoded to a primitive type.

  Args:
    bencode (str): Bencoded string.

  Returns:
    (int, bytes, list, dict): The decoded Bencode string.

  Raises:
    TypeError: If not a valid Bencode.
  '''
  pass


def to_int(bencode):
  '''
  Convert a Bencode to an int.

  Args:
    bencode (str): Bencoded string.

  Returns:
    int: The decoded value.
  '''
  pass


def to_byte_string(bencode):
  '''
  Convert a Bencode to a byte string.

  Args:
    bencode (str): Bencoded string.

  Returns:
    bytes: The decoded value.
  '''
  pass


def to_list(bencode):
  '''
  Convert a Bencode to a list.

  Args:
    bencode (str): Bencoded string.

  Returns:
    list: The decoded value.
  '''
  pass


def to_dict(bencode):
  '''
  Convert a Bencode to a dict.

  Args:
    bencode (str): Bencoded string.

  Returns:
    dict: The decoded value.
  '''
  pass
