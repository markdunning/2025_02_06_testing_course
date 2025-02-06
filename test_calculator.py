# Import the add function so the test can use it
import pytest
from calculator import add
from calculator import divide
from calculator import subtract


def test_add():
   # Check that it adds two positive integers
   assert add(1, 2) == 3
   
   # Check that it adds zero
   assert add(5, 0) == 5
   
   # Check that it adds two negative integers
   assert add(-1, -2) == -3

  
def test_divide():
  with pytest.raises(ZeroDivisionError) as e:
        divide(1,0)
  assert str(e.value) == "Cannot divide by zero!"
  
def test_subtract():
    assert subtract(5, 1) == 4
