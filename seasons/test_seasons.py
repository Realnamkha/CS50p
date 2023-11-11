from seasons import get
import pytest

def test_input():
     with pytest.raises(TypeError):
         get(12-12-2012) == 'Invalid date'
