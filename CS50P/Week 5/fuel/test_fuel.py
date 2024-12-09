import fuel


def test_gauge():
    assert fuel.gauge(fuel.convert("3/4")) == "75%"
    assert fuel.gauge(fuel.convert("1/4")) == "25%"
    assert fuel.gauge(fuel.convert("4/4")) == "F"
    assert fuel.gauge(fuel.convert("0/4")) == "E"


test_gauge()
