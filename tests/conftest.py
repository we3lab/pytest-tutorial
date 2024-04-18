""" This file contains the fixtures that are used in the tests. """

import pytest
import pandas as pd

DATA_PATH = 'tests/data/data.csv'

@pytest.fixture(scope="module")
def read_data():
    a_b_data = pd.read_csv(DATA_PATH)
    return a_b_data