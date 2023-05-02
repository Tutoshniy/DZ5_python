def fibonaci(k: int) -> int:
    a, b = 0, 1
    for i in range(k):
        if i == 0:
            yield a
        elif i == 1:
            yield b
        else:
            b, a = a+b, b
            yield b


for n in fibonaci(10):
    print(n)
