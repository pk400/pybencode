from pybencode import exceptions


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
  if not bencode:
    raise exceptions.InvalidBencode('Bencode string cannot be empty.')
  if _is_int(bencode):
    return _to_int(bencode)
  elif _is_list(bencode):
    return _to_list(bencode)
  elif _is_dict(bencode):
    return _to_dict(bencode)
  elif _is_byte_string(bencode):
    return _to_byte_string(bencode)
  raise exceptions.InvalidBencode('Failed to decode the Bencode string.'
    ' Unsupported type.')


def to_int(bencode):
  '''
  Convert a Bencode to an int.

  Args:
    bencode (str): Bencoded string.

  Returns:
    int: The decoded value.
  '''
  _check_bencode_type(bencode, _is_int,
    expected_format='i<integer encoded in base ten ASCII>e')
  return to_int(bencode)


def to_byte_string(bencode):
  '''
  Convert a Bencode to a byte string.

  Args:
    bencode (str): Bencoded string.

  Returns:
    bytes: The decoded value.
  '''
  _check_bencode_type(bencode, _is_byte_string,
    expected_format='<length>:<contents>')
  return _to_byte_string(bencode)


def to_list(bencode):
  '''
  Convert a Bencode to a list.

  Args:
    bencode (str): Bencoded string.

  Returns:
    list: The decoded value.
  '''
  _check_bencode_type(bencode, _is_list, expected_format='l<contents>e')
  return _to_list(bencode)


def to_dict(bencode):
  '''
  Convert a Bencode to a dict.

  Args:
    bencode (str): Bencoded string.

  Returns:
    dict: The decoded value.
  '''
  _check_bencode_type(bencode, _is_dict, expected_format='d<contents>e')
  return _to_dict(bencode)


def _is_int(bencode):
  return bencode[0] == 'i' and bencode[-1] == 'e' \
    and bencode[(2 if bencode[1] == '-' else 1):len(bencode) - 1].isdigit()


def _is_byte_string(bencode):
  parts = bencode.split(':')
  return len(parts) > 1 and parts[0].isdigit() and len(parts[1]) > 0


def _is_list(bencode):
  return bencode[0] == 'l' and bencode[-1] == 'e'


def _is_dict(bencode):
  return bencode[0] == 'd' and bencode[-1] == 'e'


def _to_int(bencode):
  return int(bencode[1:len(bencode) - 1])


def _to_byte_string(bencode):
  return bencode.split(':')[1]


def _to_list(bencode):
  size = len(bencode)
  contents = bencode[1:size - 1]
  decoded = []
  for index, char in enumerate(contents):
    if char == 'i':
      decoded.append(_get_int_from_substring(contents[index + 1:]))
  return decoded


def _to_dict(bencode):
  pass


def _get_int_from_substring(substring):
  for index, char in enumerate(substring):
    if char == 'e':
      break
    if not char.isdigit():
      raise exceptions.InvalidBencode('Failed to convert bencode to int.'
        f' Expected an int but found a {type(char)}.')
  return int(substring[:index])


def _check_bencode_type(bencode, predicate, expected_format):
  if not bencode or not predicate(bencode):
    raise exceptions.InvalidBencode('Failed to convert a Bencode to an int.'
      f' Expected a Bencode string in the format: {expected_format}')
