import pytest
import numpy as np

from some_functions import add

@pytest.fixture
def arrange_add_data(read_data):
    a = read_data['a']
    b = read_data['b']
    expected_result = read_data['add_result']
    # list of tuples
    return list(zip(a, b, expected_result))

def test_add(arrange_add_data):
    for a, b, expected_result in arrange_add_data:
        assert np.allclose(add(a, b), expected_result)

class TestAdd:
    def test_add_integers(self):
        assert add(1, 2) == 3

    def test_add_floats(self):
        assert np.allclose(add(1.1, 2.2), 3.3)

    def test_add_strings(self):
        assert add('hello', 'world') == 'helloworld'

    def test_add_lists(self):
        assert add([1, 2], [3, 4]) == [1, 2, 3, 4]


@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (1, 2, 3),
        (1.1, 2.2, 3.3),
        ('hello', 'world', 'helloworld'),
        ([1, 2], [3, 4], [1, 2, 3, 4])
    ]
)
def test_add_parametrize(a, b, expected_result):
    if isinstance(expected_result, (int, float)):
        assert np.allclose(add(a, b), expected_result)
    else:
        assert add(a, b) == expected_result

@pytest.mark.parametrize(
    "a, b",
    [
        (1, '2'),
        ('hello', 1),
        ([1, 2], 3),
        ({1: 1}, {2: 2})
    ]
)
def test_add_raises_type_error(a, b):
    with pytest.raises(TypeError):
        add(a ,b)
