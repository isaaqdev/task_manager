from src import app

def test_add():
    assert app.add(1,2) == 3

def test_false_add():    
    assert app.add(1,2) != 4


def test_sub():
    assert app.sub(1,2) == -1

def test_false_sub():
    assert app.sub(1,2) != 4

