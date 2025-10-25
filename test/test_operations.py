from src.math_operations import add, sub

def test_add():
    assert add(3,2)==5
    assert add(1,8)==9
    assert add(4,6)==10

def test_sub():
    assert sub(-1,1)==0
    assert sub(3,1)==2
    assert sub(4,3)==1