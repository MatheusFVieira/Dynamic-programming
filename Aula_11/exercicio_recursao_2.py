# === Helper de verificacao (pode ignorar) ===
# A funcao `verifica` compara o seu valor com a resposta correta (que
# fica escondida em formato de hash). Voce nao precisa entender ela -
# se voce errou, ela imprime "Valor errado: voce colocou X" e o assert
# logo abaixo dispara.
import hashlib
def verifica(valor, codigo):
    valores = [valor]
    if isinstance(valor, list):
        valores = [sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    respostas = [hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo for valor in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True
# fim do helper

import sys

# === Helper para listas aninhadas (pode ignorar) ===
# `eh_lista(x)` voce vai usar dentro da funcao soma_ll, na fase 7.

def eh_lista(a):
    return isinstance(a, list)
# fim do helper

'''
EXPLICACAO

Segunda lista de RECURSAO. O padrao continua o mesmo:

    def funcao(entrada):
        if caso_base(entrada):
            return resposta_imediata
        else:
            resposta_menor = funcao(entrada_menor)
            return combina(entrada, resposta_menor)

- CASO RECURSIVO (terceirizacao): chamamos a propria funcao com uma
  entrada MENOR e combinamos o resultado com o pedaco que foi tirado.
- CASO BASE: a entrada e pequena o suficiente pra responder direto.

Em cada fase, voce primeiro preenche VARIAVEIS que ilustram o passo
recursivo (com calculo a mao), e so depois implementa a funcao. A
ideia e voce ENTENDER o algoritmo antes de codar.
'''

# ===== FASE 1 - soma_n_primeiros =====

'''
EXPLICACAO

`soma_n_primeiros(n)` retorna a soma dos numeros de 1 ate n:

    soma_n_primeiros(3) = 1 + 2 + 3 = 6
    soma_n_primeiros(5) = 1 + 2 + 3 + 4 + 5 = 15
    soma_n_primeiros(100) = 5050

Caso base: soma_n_primeiros(1) = 1
Terceirizacao: soma_n_primeiros(n) = soma_n_primeiros(n - 1) + n
'''

soma_de_1 = 1   # caso base, ja preenchido

'''
EXERCICIO - terceirizacao em cadeia

Use o `soma_de_1` em uma EXPRESSAO Python pra calcular `soma_de_2`.
Depois use `soma_de_2` pra calcular `soma_de_3`, e assim por diante.

    soma_de_2 = soma_de_1 + 2     (terceiriza o de 1)
    soma_de_3 = soma_de_2 + 3     (terceiriza o que voce acabou de calcular!)

Cada variavel reusa a anterior — exatamente o que a funcao recursiva
vai fazer quando ela se chamar.
'''
soma_de_2 = 'coloque o valor aqui'
soma_de_3 = 'coloque o valor aqui'
soma_de_4 = 'coloque o valor aqui'

'''
EXERCICIO

Imagine que voce ja sabe que `soma_de_99 = 4950` (e isso eh verdade
mesmo — voce nao precisa calcular). Quanto vale `soma_de_100`?

Use uma EXPRESSAO Python, nao precisa fazer a conta na mao
'''
soma_de_99 = 4950
soma_de_100 = 'coloque o valor aqui'

assert verifica(soma_de_2, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'soma_de_2 incorreta'
assert verifica(soma_de_3, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'soma_de_3 incorreta'
assert verifica(soma_de_4, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c'), 'soma_de_4 incorreta'
assert verifica(soma_de_100, 'dd257f72fb3e38dece91f7716fe2baa34e680a5bd3b3b0c8c28cac0a'), 'soma_de_100 incorreta'
print('Exercicio soma_n_primeiros terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `soma_n_primeiros(n)` que retorna a
soma dos inteiros de 1 ate n.

DICA: caso base — n == 1 retorna 1. Terceirizacao — chamar
soma_n_primeiros(n - 1) e somar n.

    >>> soma_n_primeiros(1)
    1
    >>> soma_n_primeiros(3)
    6
    >>> soma_n_primeiros(100)
    5050
'''
def soma_n_primeiros(n):
    pass

# Bloco 1: caso base.
assert soma_n_primeiros(1) == 1, 'soma_n_primeiros(1) deveria ser 1 (caso base)'
print('Exercicio soma_n_primeiros caso base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert soma_n_primeiros(2) == 3
assert soma_n_primeiros(3) == 6
assert soma_n_primeiros(5) == 15
assert soma_n_primeiros(10) == 55
assert soma_n_primeiros(100) == 5050

sys.setrecursionlimit(50)
try:
    soma_n_primeiros(1000)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao soma_n_primeiros e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio soma_n_primeiros caso recursivo: OK')


# ===== FASE 2 - soma_lista =====

'''
EXPLICACAO

`soma_lista(lista)` retorna a soma de TODOS os numeros da lista.

    soma_lista([10, 2]) = 12
    soma_lista([10, 2, 3]) = 15
    soma_lista([]) = 0   (caso base)

Terceirizacao: soma_lista([primeiro, ...resto]) = primeiro + soma_lista(resto)
'''

lista_para_soma_lista = [10, 2, 3]

'''
EXERCICIO

Vamos ilustrar o passo recursivo com VARIAVEIS, antes de escrever a
funcao. Considere a `lista_para_soma_lista` = [10, 2, 3] acima.

1) Qual o PRIMEIRO elemento? (use uma EXPRESSAO: `lista_para_soma_lista[0]`)
'''
primeiro_para_soma_lista = 'coloque o valor aqui'

'''
2) Quais os DEMAIS (a partir do indice 1)?
'''
demais_para_soma_lista = 'coloque o valor aqui'

'''
3) Terceirize: qual a SOMA dos demais? (calcule a mao — soma de [2, 3])
'''
soma_dos_demais_soma_lista = 'coloque o valor aqui'

'''
4) Junte: a soma total e `primeiro + soma_dos_demais`.
'''
total_da_soma_lista = 'coloque o valor aqui'

assert verifica(primeiro_para_soma_lista, '3aac67cd73162d439f9947d61357a1b62432f0ca84b7f435f4177a8c'), 'primeiro_para_soma_lista incorreta'
assert verifica(demais_para_soma_lista, '6e203ed3f5165334817e0c19f82f510152817eafabbb2405a4df890f'), 'demais_para_soma_lista incorreta'
assert verifica(soma_dos_demais_soma_lista, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17'), 'soma_dos_demais_soma_lista incorreta'
assert verifica(total_da_soma_lista, '87592c38e2b36a1d35437714ecedee4d6fad7a1a0b1bf5d7a2ab68ef'), 'total_da_soma_lista incorreta'
print('Exercicio soma_lista terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `soma_lista(lista)`.

DICA: caso base — lista vazia retorna 0. Terceirizacao — pega
`lista[0]` e soma com `soma_lista(lista[1:])`.

    >>> soma_lista([])
    0
    >>> soma_lista([10, 2, 3])
    15
'''
def soma_lista(lista):
    pass

# Bloco 1: caso base.
assert soma_lista([]) == 0, 'soma_lista([]) deveria ser 0 (caso base)'
assert soma_lista([1]) == 1, 'soma_lista com 1 elemento'
assert soma_lista([-3]) == -3, 'soma_lista com 1 negativo'
print('Exercicio soma_lista caso base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert soma_lista([1, 2, 30]) == 33
assert soma_lista([10, 2, 3]) == 15
assert soma_lista([10, 2, 3, 4]) == 19
assert soma_lista([-1, -2, -3, -4]) == -10

sys.setrecursionlimit(50)
try:
    soma_lista([1] * 100)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao soma_lista e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio soma_lista caso recursivo: OK')


# ===== FASE 3 - conta_recursiva =====

'''
EXPLICACAO

`conta_recursiva(lista, numero)` retorna quantas vezes `numero`
aparece em `lista`.

    conta_recursiva([0, 1, 2, 1, 4], 1) = 2
    conta_recursiva([0, 1, 2, 1, 4], 4) = 1
    conta_recursiva([0, 1, 2, 1, 4], 5) = 0
    conta_recursiva([], 5)              = 0   (caso base)

Terceirizacao: percorre primeiro+resto. Se primeiro == numero, soma 1
no resultado do resto; senao, so retorna o resultado do resto.
'''

lista_para_conta = [0, 1, 2, 1, 4]
numero_para_conta = 1

'''
EXERCICIO

Considere a `lista_para_conta` = [0, 1, 2, 1, 4] e `numero_para_conta` = 1.

1) Qual o RESTO (lista a partir do indice 1)?
'''
demais_para_conta = 'coloque o valor aqui'

'''
2) Terceirize: quantas vezes o 1 aparece nos DEMAIS? (conte a mao em
   [1, 2, 1, 4])
'''
conta_nos_demais = 'coloque o valor aqui'

'''
3) Junte: o primeiro elemento e 0 (diferente de 1, entao soma 0 ao
   total). A conta total da lista inteira e:

       0 + conta_nos_demais

   (zero porque o primeiro 0 NAO eh igual ao 1 procurado)
'''
total_de_contas = 'coloque o valor aqui'

assert verifica(demais_para_conta, '2d68bdf2c0c0d588f4b84b61fc3d4f83c56208690357c39bc51e16ee'), 'demais_para_conta incorreta'
assert verifica(conta_nos_demais, '58b2aaa0bfae7acc021b3260e941117b529b2e69de878fd7d45c61a9'), 'conta_nos_demais incorreta'
assert verifica(total_de_contas, '58b2aaa0bfae7acc021b3260e941117b529b2e69de878fd7d45c61a9'), 'total_de_contas incorreta'
print('Exercicio conta_recursiva terceirizacao: OK')

'''
EXERCICIO

Implemente `conta_recursiva(lista, numero)`.

DICA: caso base — lista vazia retorna 0. Terceirizacao — se
`lista[0] == numero`, retorna 1 + conta_recursiva(lista[1:], numero);
senao retorna conta_recursiva(lista[1:], numero).

    >>> conta_recursiva([], 5)
    0
    >>> conta_recursiva([0, 1, 2, 1, 4], 1)
    2
'''
def conta_recursiva(lista, numero):
    pass

# Bloco 1: caso base.
assert conta_recursiva([], 5) == 0, 'conta_recursiva([], 5) (caso base)'
assert conta_recursiva([5], 5) == 1, 'conta_recursiva([5], 5)'
assert conta_recursiva([1], 5) == 0, 'conta_recursiva([1], 5)'
print('Exercicio conta_recursiva caso base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert conta_recursiva([0, 1, 2, 1, 4], 1) == 2
assert conta_recursiva([0, 1, 2, 1, 4], 4) == 1
assert conta_recursiva([0, 1, 2, 1, 4], 5) == 0
assert conta_recursiva([1, 1], 1) == 2
assert conta_recursiva([1, 1], 2) == 0

sys.setrecursionlimit(50)
try:
    conta_recursiva([1] * 100, 1)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao conta_recursiva e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio conta_recursiva caso recursivo: OK')




# ===== FASE 5 - palindromo_recursivo =====

'''
EXPLICACAO

Um PALINDROMO eh uma string que se le igual de tras pra frente:
'abba', 'osso', 'arara' sao palindromos. 'banana' nao eh.

`palindromo_recursivo(string)` retorna True se string for palindromo.

    palindromo_recursivo('abba')    = True
    palindromo_recursivo('aaa')     = True
    palindromo_recursivo('aac')     = False
    palindromo_recursivo('')        = True   (caso base)
    palindromo_recursivo('a')       = True   (caso base)

Terceirizacao: olha a primeira e a ultima letra. Se forem diferentes,
ja sabe que NAO eh palindromo (retorna False). Se forem iguais,
TERCEIRIZA pro pedaco do meio: se o meio for palindromo, a string
inteira eh.

DICA Python:
    string[0]     # primeira letra
    string[-1]    # ultima letra
    string[1:-1]  # tudo menos a primeira e a ultima
'''

string_para_palindromo = 'abba'

'''
EXERCICIO

Considere `string_para_palindromo` = 'abba'.

1) Qual a PRIMEIRA letra? (use uma EXPRESSAO: `string_para_palindromo[0]`)
'''
primeira_letra_pal = 'coloque o valor aqui'

'''
2) Qual a ULTIMA letra? (use `string_para_palindromo[-1]`)
'''
ultima_letra_pal = 'coloque o valor aqui'

'''
3) Qual eh o MEIO (tudo menos a primeira e a ultima)?
   (use `string_para_palindromo[1:-1]`)
'''
meio_pal = 'coloque o valor aqui'

'''
4) Terceirize: o meio ('bb') eh um palindromo? (True/False)
'''
meio_eh_palindromo = 'coloque o valor aqui'

'''
5) Junte: 'abba' eh palindromo se a primeira == ultima E o meio for
   palindromo. Use uma EXPRESSAO Python:

       (primeira_letra_pal == ultima_letra_pal) and meio_eh_palindromo
'''
eh_palindromo_total = 'coloque o valor aqui'

assert verifica(primeira_letra_pal, 'abd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5'), 'primeira_letra_pal incorreta'
assert verifica(ultima_letra_pal, 'abd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5'), 'ultima_letra_pal incorreta'
assert verifica(meio_pal, '10596a6ddb01d26e3f0fcec5243cefc3c87b125eae9d32ec86c1670f'), 'meio_pal incorreta'
assert verifica(meio_eh_palindromo, 'b45899583510159617e22fca2b6f561a09289be12ccb30f6df8d4a11'), 'meio_eh_palindromo incorreta'
assert verifica(eh_palindromo_total, 'b45899583510159617e22fca2b6f561a09289be12ccb30f6df8d4a11'), 'eh_palindromo_total incorreta'
print('Exercicio palindromo terceirizacao: OK')

'''
EXERCICIO

Implemente `palindromo_recursivo(string)`.

DICA: caso base — string vazia ou de 1 letra eh palindromo (True).
Terceirizacao — se string[0] != string[-1], retorna False. Senao,
retorna palindromo_recursivo(string[1:-1]).

    >>> palindromo_recursivo('')
    True
    >>> palindromo_recursivo('a')
    True
    >>> palindromo_recursivo('abba')
    True
    >>> palindromo_recursivo('banana')
    False
'''
def palindromo_recursivo(string):
    pass

# Bloco 1: caso base.
assert palindromo_recursivo('') == True, 'palindromo_recursivo("") (caso base)'
assert palindromo_recursivo('a') == True, 'palindromo_recursivo("a") (caso base)'
print('Exercicio palindromo caso base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert palindromo_recursivo('abba') == True
assert palindromo_recursivo('abbabba') == True
assert palindromo_recursivo('aaa') == True
assert palindromo_recursivo('aaaa') == True
assert palindromo_recursivo('aac') == False
assert palindromo_recursivo('baacb') == False
assert palindromo_recursivo('abaacba') == False

sys.setrecursionlimit(50)
try:
    palindromo_recursivo('a' * 100)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao palindromo_recursivo e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio palindromo caso recursivo: OK')



# ===== FASE 7 - soma_ll (listas aninhadas) =====

'''
EXPLICACAO

`soma_ll(lista)` retorna a soma de TODOS os numeros, contando os
de dentro das sublistas em qualquer nivel.

    soma_ll([1, 2, 3])               = 6
    soma_ll([[1, 2], [3]])           = 6
    soma_ll([[[1, 2, 3], [4, 5], 11, 4], 9, 8, 4]) = 47

Aqui a recursao eh um pouco diferente: em vez de "primeiro + resto",
a funcao PERCORRE cada item da lista. Pra cada item:
    - se for numero: soma ele direto
    - se for lista: TERCEIRIZA — pede a soma_ll DELE, e soma o resultado

Pra ajudar, ja definimos `eh_lista(x)` no topo do arquivo (retorna
True se x eh uma lista).
'''

lista_para_soma_ll = [[1, 2, 3], [4, 5], 11, 4]

'''
EXERCICIO

Considere `lista_para_soma_ll` = [[1, 2, 3], [4, 5], 11, 4]. Ela tem
4 itens no topo: duas sublistas, e os numeros 11 e 4.

1) Terceirize: qual a soma da PRIMEIRA sublista, [1, 2, 3]?
'''
soma_da_primeira_sublista = 'coloque o valor aqui'

'''
2) Terceirize: qual a soma da SEGUNDA sublista, [4, 5]?
'''
soma_da_segunda_sublista = 'coloque o valor aqui'

'''
3) Junte: a soma_ll da lista inteira eh a soma das duas parcelas, mais os numeros soltos.
   Use uma EXPRESSAO Python:

       soma_da_primeira_sublista + soma_da_segunda_sublista + numero solto 1 + numero solto 2
'''
total_da_soma_ll = 'coloque o valor aqui'

assert verifica(soma_da_primeira_sublista, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'soma_da_primeira_sublista incorreta'
assert verifica(soma_da_segunda_sublista, '192f56eb9bd894a72b30c303247b107be2c4591f310dd69a67927f48'), 'soma_da_segunda_sublista incorreta'
assert verifica(total_da_soma_ll, '6332531eeafc6e0ede272192be898f549950fb32b209d04f0a98306a'), 'total_da_soma_ll incorreta'
print('Exercicio soma_ll terceirizacao: OK')

'''
EXERCICIO

Implemente a funcao recursiva `soma_ll(lista)`. Ela percorre a lista
e, pra cada item, soma o item (se for numero) ou a soma_ll desse
item (se for uma sublista).

DICA: comece com `total = 0`. Faca um for percorrendo a lista. Use
`eh_lista(item)` pra decidir.

    >>> soma_ll([])
    0
    >>> soma_ll([[], []])
    0
    >>> soma_ll([1, 2, 3])
    6
    >>> soma_ll([[1, 2, 3], [4, 5], 11, 4])
    30
    >>> soma_ll([[[1, 2, 3], [4, 5], 11, 4], 9, 8, 4])
    51
'''
def soma_ll(lista):
    pass

# Bloco 1: casos base (sem sublistas).
assert soma_ll([]) == 0, 'soma_ll([]) (caso base)'
assert soma_ll([1]) == 1, 'soma_ll com 1 elemento'
assert soma_ll([1, 2, 3]) == 6, 'lista plana'
assert soma_ll([-3]) == -3, 'um negativo'
print('Exercicio soma_ll casos base: OK')

# Bloco 2: caso recursivo (sublistas a terceirizar).
assert soma_ll([[], []]) == 0, 'so sublistas vazias'
assert soma_ll([[1], [2]]) == 3, 'duas sublistas simples'
assert soma_ll([[-1], [1]]) == 0, 'soma zero entre sublistas'
assert soma_ll([[[1, 2, 3], [4, 5], 11], 9, 8]) == 43
assert soma_ll([[[1, 2, 3], [4, 5], 11, 4], 9, 8, 4]) == 51
assert soma_ll([[1], [[2], 1]]) == 4, 'aninhamento de mais de 1 nivel'
print('Exercicio soma_ll caso recursivo: OK')


print('\n=== PARABENS! Todos os exercicios principais completos! ===')

