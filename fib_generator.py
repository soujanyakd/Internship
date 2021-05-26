#using generators
def fib():
    n1=0
    n2=1
    nth=1
    while True:
        yield nth
        nth = n1 + n2
        n1 = n2
        n2 = nth
seq = fib()
for i in range(10):
    print(next(seq))