def f(a):
    return 2*a

def g(b):
    v = 3*f(b)
    return v

def h(c):
    v = g(c)-3
    return v

a = h(10)
print(a)