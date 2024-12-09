import numb3rs


def test_validate():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("512.512.512.512") == False
    assert numb3rs.validate("1.2.3.1000") == False
    assert numb3rs.validate("cat") == False
