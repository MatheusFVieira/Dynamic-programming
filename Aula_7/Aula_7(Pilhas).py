# def f(a):
#     return 2*a

# def g(b):
#     v = 3*f(b)
#     return v

# def h(c):
#     v = g(c)-3
#     return v

# a = h(10)
# print(a)


def string_balanceada(string):
    pilha = []
    for i in string:
        if i in "([{":
            pilha.append(i)
        elif pilha == []:
            return False
        elif i in ")]}":
            topo = pilha.pop()
            if not encaixa (topo, i):
                return False
    if pilha != []:
        return True
    else:
        return False

def encaixa(abre, fecha):
    if abre == '(' and fecha == ')': return True
    if abre == '[' and fecha == ']': return True
    if abre == '{' and fecha == '}': return True
    return False
    
if(string_balanceada('([]]{}') == False):
    print("Correto1")  
if(string_balanceada('([]){}') == True):
    print("Correto2") 
if(string_balanceada('())') == False):
    print("Correto3") 
if(string_balanceada('([]{') == False):
    print("Correto4")  