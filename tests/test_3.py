import pytest
import numpy as np
def test_add2and3(capsys):
    from answers_module import add2and3
    A = np.random.rand(3, 5)
    assert np.allclose(add2and3(A), np.sum(A[1,:]) + np.sum(A[:,2]))
    A = np.random.rand(1, 2)
    res = add2and3(A)
    captured = capsys.readouterr()
    assert captured.out.lower().find("Matrix too small".lower()) != -1

def test_squareme(capsys):
    from answers_module import squareme
    A = np.random.rand(3, 2)
    row = 2
    assert np.allclose(squareme(A, row), A[row-1] ** 2, rtol=1e-1, atol=0)

    res = squareme(A, 5)
    captured = capsys.readouterr()
    assert captured.out.lower().find("Row not found".lower()) != -1
