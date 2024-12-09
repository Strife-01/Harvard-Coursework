from jar import Jar
import pytest


def main():
    test_jar()


def test_jar():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "\U0001F36A" * 3


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError) as err:
        jar.deposit(10)
    assert str(err.value) == "Too not enough space in the jar"


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    with pytest.raises(ValueError) as err:
        jar.withdraw(10)
    assert str(err.value) == "Not enough cookies in the jar"


if __name__ == "__main__":
    main()
