from posnos import pos

def test_pos():
    assert pos(10) == "Positive Number"
    
def test_neg():
    assert pos(-10) == "Negative Number"
    
def test_zero():
    assert pos(0) == "The Number is Zero"
