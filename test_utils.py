import pytest
import utils
def test_fact():
    with pytest.raises(ValueError):
        utils.fact(-1)
    assert utils.fact(4)
    assert utils.fact(1)==1