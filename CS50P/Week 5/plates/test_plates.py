import plates


def test_is_valid():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("CS50P") == False
    assert plates.is_valid("PI3.14") == False
    assert plates.is_valid("H") == False
    assert plates.is_valid("OUTATIME") == False
