import numpy as np

from mod import sinc2d

def test_internal():
    exp = (2.0 / np.pi) * (-2.0 / (3.0 * np.pi))
    obs = sinc2d(np.pi / 2.0, 3.0 * np.pi / 2.0)
    assert obs == exp

def test_edge_x():
    exp = (-2.0 / (3.0 * np.pi))
    obs = sinc2d(0.0, 3.0 * np.pi / 2.0)
    assert obs == exp

def test_edge_y():
    exp = (2.0 / np.pi)
    obs = sinc2d(np.pi / 2.0, 0.0)
    assert obs == exp

	
def test_corner(x,y):
	if x == 0.0 and y == 0.0:
		return 1.0
	elif x == 0.0:
		return np.sin(y) / y
	elif y == 0.0:
		return np.sin(x) / x
	else:
		return (np.sin(x) / x) * (np.sin(y) / y)