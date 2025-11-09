import pytest
from numb3rs import validate

def main():
    test()

def test():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("123.23.0.999") == False
    assert validate("999.256.999.999") == False

    return

if __name__ == '__main__':
    main()
