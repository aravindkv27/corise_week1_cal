from calculator import addition, multiplication, subtraction, division

def test_add():

    assert addition(10,5) == 15
    assert addition(10,15) == 25

def test_sub():

    assert subtraction(10,5) == 5

def test_mul():

    assert multiplication(10, 5) == 50

def test_div():

    assert division(10,5) ==  2

