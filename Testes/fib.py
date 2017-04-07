def fib(n):

    """
    Retorna o n esimo numero de fibonnacci
    """

    if n<=1:
        return 1
    else:
            return fib(n-1)+fib(n-3)

    """
    cada modulo do python tem dunder name, modulo que chamo por terminal e main. Meio que um debbug
    """
print("hello")
import fib as _fib_mod
if __name__ == '__main__':
    print(fib(5))
    print(fib(3))
    assert fib(1) == 1
    assert fib(2) == 2