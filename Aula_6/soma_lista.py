def maxSub(lista):
    maior_ate = lista[0]
    for i in range(0,len(lista)):
        for j in range(i, len(lista)):
            soma = sum(lista[i:j+1])
            if soma > maior_ate:
                maior_ate = soma
    return maior_ate

l1 = [1,2,3]
assert maxSub(l1) == 6

l2 = [1,2,3,-1]
assert maxSub(l2) == 6

l3 = [1,2,3,-1,5]
assert maxSub(l3) == 10