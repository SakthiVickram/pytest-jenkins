from src.calculator import add
import pytest
def test_add():
    result = add(3, 4)
    assert result == 9
def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)
