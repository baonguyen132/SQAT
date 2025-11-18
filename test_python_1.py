import pytest

def add(x,y):
    return x+y

product = [
    (1,2,3),
    (4,5,9),
    (2,2,4),
    (5,6,10),
    (1,6,7)
]

@pytest.mark.parametrize("a,b,result",product)
def test_add(a,b,result):
    assert add(a,b) == result, f"Test faild: The sum of {a} and {b} should be {result}"