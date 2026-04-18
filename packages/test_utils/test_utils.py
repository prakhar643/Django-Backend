
from packages.mypackage.math import add
from packages.mypackage.utils import utils_function


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_utils_function():
    assert utils_function() == "This is a utility function"