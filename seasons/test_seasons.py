from seasons import  as f
import pytest

def test_input():
     with pytest.raises(TypeError):
         f(12-12-2012) == 'Invalid date'
