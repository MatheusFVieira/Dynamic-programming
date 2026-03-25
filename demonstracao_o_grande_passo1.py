def casal_13(lista):
    for n in lista:
        if 13-n in lista:
            return True
    return False

import time
import random

def gera_lista(n=400):
    print('a lista agora tem '+str(n)+' elementos.')
    return [random.randint(1,10*n) for x in range(n)]

def tempos(function_list, generator, n=400):
    l = generator(n)
    for f in function_list:
        start = time.process_time()
        for a in range(1,100):
          l1 = l[:]
          f(l1)
        end = time.process_time()
        print(f'o algoritmo {f} levou: {end-start}')
    


def comparar_casal13():
        tempos(function_list=[casal_13],generator=gera_lista,n=400)
        tempos(function_list=[casal_13],generator=gera_lista,n=800)
        tempos(function_list=[casal_13],generator=gera_lista,n=1600)
        tempos(function_list=[casal_13],generator=gera_lista,n=3200)

comparar_casal13()