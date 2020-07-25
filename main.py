from pybencode.decode import decode, to_byte_string, to_dict, to_int, to_list


def main():
  s1 = 'i42e'
  assert decode(s1) == 42
  assert to_int(s1) == 42
  s2 = '4:spam'
  assert decode(s2) == 'spam'
  assert to_byte_string(s2) == 'spam'
  s3 = 'li99ei0ee'
  assert decode(s3) == [99, 0]
  assert to_list(s3) == [99, 0]


if __name__ == '__main__':
  main()
