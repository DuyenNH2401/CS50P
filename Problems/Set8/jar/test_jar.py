from jar import Jar
import pytest

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(5)
    assert jar2.capacity == 5
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) =="🍪🍪"
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(3)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(-1)

if __name__ == '__main__':
    main()