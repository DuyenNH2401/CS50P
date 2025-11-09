import pytest
from working import convert

def main():
    test_format()
    test_time()
    test_hour()
    test_minute()

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_hour():
    with pytest.raises(ValueError):
        convert("19:00 PM to 17 PM")

def test_minute():
    with pytest.raises(ValueError):
        convert("12:30 AM to 9:70 PM")
        convert("12: 70 AM to 9:30 PM")

if __name__ == '__main__':
    main()