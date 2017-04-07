from fib import fib
import sys
#print(sys.argv)

def test_known_fibs():
    assert fib(1) == 1
    assert fib(2) == 2
    #assert 4 == 5
    #assert fib(5) is not None


if __name__ == '__main__':
    test_known_fibs()

#digite python3 testfib.pypara executar