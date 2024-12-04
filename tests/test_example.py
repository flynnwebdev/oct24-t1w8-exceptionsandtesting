def test_success():
    assert 10 / 2 == 5

def test_failure():
    assert 10 / 2 == 0

def test_exception():
    if True:
        raise ValueError('You got a value error!')
    
