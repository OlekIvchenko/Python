number = 5
def summa(a, b):
    # c = a + b
    # return c
    return a + b

def mult(a, b = 5) -> int:
    """Info mult ..."""
    return a * b

def new_summa(*a):
    summa = 0
    for i in a:
        summa += i
    return summa
    # print(summa)

def new_summa_arr(a):
    summa = 0
    for i in a:
        summa += i
    return summa

def factorial(n):
    if n == 1:
        return n
    else: return n * factorial(n-1)

# F(4) -> 4 * F(4-1) -> 4 * F(3) -> 4 * 6 -> 24
# F(3) -> 3 * F(3-1) -> 3 * F(2) -> 3 * 2 -> 6
# F(2) -> 2 * F(2-1) -> 2 * F(1) -> 2 * 1 -> 2
# F(1) -> 1