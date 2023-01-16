from answers_module import myrec
import pytest
def test_myrec():
    assert myrec(0) == 0
    assert myrec(6) == 6
    assert myrec(532) == 532
    with pytest.raises(Exception):
        myrec(-1)