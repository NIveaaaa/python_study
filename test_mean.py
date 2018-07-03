from mean import mean
import pytest
def test_str():
	with pytest.raises(TypeError,
	match = "The algebraic mean of an empty list is undefined. "
    "Please provide a list of numbers"
	):
		mean([""])			   

def test_ints():
    num_list = [1, 2, 3, 4, 5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

def test_empty():
    num_list=[]
    obs = mean(num_list)
    exp = 0
    assert obs == exp	
	
def test_zero():
    num_list=[0,2,4,6]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

def test_double():
    # This one will fail in Python 2
    num_list=[1,2,3,4]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp

def test_long():
    big = 100000000
    obs = mean(range(1,big))
    exp = big/2.0
    assert obs == exp

def test_complex():
    # hint: there's a problem with this test
    num_list = [2 + 3j, 3 + 4j, -32 - 2j]
    obs = mean(num_list)
    exp = -9 + 5j/3
    assert obs == exp

