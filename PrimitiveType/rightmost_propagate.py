def rightPro(x:int) -> int:
    y = x
    x &= ~(x-1) # isolate the rightmost 1
    print(x)
    y += (x-1)

    return y

x = 36
print("original", bin(x))
y = rightPro(x)
print("after",bin(y))