from math_series.series import lucas_check , fibonacci , sum_series 

def test_lucas_0():
    expected = 2
    actual = lucas_check(0)
    assert actual == expected

def test_lucas_1():
    expected = 1
    actual = lucas_check(1)
    assert actual == expected

def test_lucas_2():
    expected = 3
    actual = lucas_check(2)
    assert actual == expected



def test_fibonacci_0():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_fibonacci_1():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_fibonacci_2():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected



def test_sum_0():
    expected = 0
    actual = sum_series(0,0,0)
    assert actual == expected

def test_sum_1():
    expected = 2
    actual = sum_series(2,0,2)
    assert actual == expected

def test_sum_2():
    expected = 4
    actual = sum_series(2,0,0)
    assert actual == expected

def test_sum_3():
    expected = 2
    actual = sum_series(3,0,0)
    assert actual == expected





