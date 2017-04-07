from fib import fib
import unittest
import pytest

class TestFib(unittest.TestCase):
    def setUp(self):
        self.x = 1
        self.fx = 1

    def tearDown(self):
        pass

    def test_other_fib(self):
        self.assertEqual(fib(self.x), fib(self.fx))

    def test_known_fibs(self):
        self.assertEqual(fib(1),1)

@pytest.fixture
def fx():
    yield 5

@pytest.fixture
def fx():
    return 8