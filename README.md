# pybencode
Python3 library for decoding a [Bencode](https://en.wikipedia.org/wiki/Bencode) string to a primitive type. Currently supports `int`, `bytes`, and `list` types.

# Importing into your project
To use pybencode, simply import the `decode()` function.
```python
from pybencode.decode import decode
```

# How to run script
The project also includes a `main.py` demonstrating common use cases for the library. From the root project directory simply run the `main.py` script.
`python main.py`

# How to use pybencode
pybencode provides a function for decoding a general Bencode string with `decode()`.

```python
from pybencode.decode import decode

s1 = decode('5:hello')
print(s1) # hello

s2 = decode('i999e')
print(s2) # 999

s3 = decode('l4:spami42ee')
print(s3) # ['spam', 42]
```

The library also includes functions for decoding a Bencode string if the type is known.


```python
from pybencode.decode import to_byte_string, to_int, to_list

s1 = to_byte_string('5:hello')
print(s1) # hello

s2 = to_int('i999e')
print(s2) # 999

s3 = to_list('l4:spami42ee')
print(s3) # ['spam', 42]
```

pybencode is also able to decode nested lists as well.
```python
from pybencode.decode import decode

s1 = decode('lli42eli99ei200eeee')
print(s1) # [[42, [99, 200]]]
```

# Testing
pybencode also includes unit tests. From the project root:
`python -m unittest tests.decode_tester`

# Exceptions
`PyBencodeException`: Is the base exception used throughout pybencode.
`InvalidBencode`: Is raised when an invalid Bencode string is passed as input to a decode function.

```
PyBencodeException
└─ InvalidBencode
```
---

# Todo
- [ ] Support decoding dict-types
- [ ] Support byte string in lists
- [ ] Add more unit tests
- [ ] Add more robust error handling
- [ ] Package library for better distribution
