from main import mathdiv
import pytest

def test_divide():
    m=mathdiv()
    assert m.divide(10,2)==5
    assert m.divide(9,3)==3

    with pytest.raises(ValueError,match="Cannot divide by zero!"): # for checking error
        assert m.divide(10,0)