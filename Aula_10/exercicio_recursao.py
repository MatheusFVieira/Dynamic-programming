
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
import random


# === Helpers para listas aninhadas (pode ignorar — usados na Fase 9) ===
# `eh_lista(x)` voce vai usar dentro das suas funcoes recursivas que
# mexem com listas aninhadas. O resto so e chamado pelo proprio teste.

def eh_lista(a):
    return isinstance(a, list)


def gera_r(max_subdirs, max_arquivos, coloca_segredo):
    """Gera uma lista aninhada aleatoria; se coloca_segredo=True,
    insere a string 'segredo' em algum nivel dela."""
    subdirs, arquivos = 0, 0
    lista = []
    if max_subdirs > 0:
        subdirs = random.randint(max_subdirs // 2, max_subdirs)
    for _ in range(subdirs):
        lista.append(gera_r(max_subdirs - 1, max_arquivos - 1, False))
    if max_arquivos > 0:
        arquivos = random.randint(max_arquivos // 2, max_arquivos)
    for _ in range(arquivos):
        lista.append(random.randint(0, arquivos))
    if coloca_segredo:
        _adiciona_segredo(lista)
    return lista


def _adiciona_segredo(lista):
    plana = _aplaina(lista)
    posicao = random.randint(0, len(plana) - 1)
    plana[posicao].append('segredo')


def _aplaina(lista):
    plana = [lista]
    for a in lista:
        if eh_lista(a):
            plana.extend(_aplaina(a))
    return plana
# fim dos helpers


'''
EXPLICACAO

Bem-vindo a lista de RECURSAO!

Uma funcao recursiva e uma funcao que chama a si mesma. Soa estranho,
mas e o jeito natural de resolver problemas que tem uma "versao menor
do mesmo problema" la dentro.

O padrao geral e SEMPRE o mesmo:

    def funcao(entrada):
        if caso_base(entrada):
            return resposta_imediata
        else:
            resposta_menor = funcao(entrada_menor)
            return combina(entrada, resposta_menor)

- CASO RECURSIVO/TERCEIRIZACAO: chama a propria funcao com uma entrada MENOR e
  combina o resultado com o pedaco que voce tirou.
- CASO BASE: a entrada e pequena o suficiente pra responder na hora,
  sem precisar chamar a funcao de novo. Sem isso, existe apenas
  terceirizacao, a recursao nao para.

Vamos comecar com fatorial, que eh o exemplo classico.
'''


# ===== FASE 1 - Fatorial: aquecimento =====

'''
EXPLICACAO

O fatorial de n eh o produto 1*2*3*...*n.

    fatorial(4) = 1*2*3*4 = 24
    fatorial(5) = 1*2*3*4*5 = 120
    fatorial(1) = 1 = 120

    Ou seja, fatorial(10) é uma linguiça de 1 a 10, multiplicando todos os termos
    fatorial(10) = 1*2*3*4*5*6*7*8*9*10

Caso especial: fatorial(0) = 1 (por definicao).
'''

'''
EXERCICIO

Calcule a mao e preencha as variaveis.

1) Quanto eh fatorial de 0? (lembre do caso especial)
'''
fatorial_0 = '1'

'''
2) Quanto eh fatorial de 1?
'''
fatorial_1 = '1'

'''
3) Quanto eh fatorial de 2?
'''
fatorial_2 = '2'

'''
4) Quanto eh fatorial de 6?
'''
fatorial_6 = '720'



assert verifica(fatorial_0, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'), 'fatorial_0 incorreta'
assert verifica(fatorial_1, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'), 'fatorial_1 incorreta'
assert verifica(fatorial_2, '58b2aaa0bfae7acc021b3260e941117b529b2e69de878fd7d45c61a9'), 'fatorial_2 incorreta'
assert verifica(fatorial_6, 'f10fcdd526499546551e174a5da16e9bc210909699d815b5d18b236f'), 'fatorial_6 incorreta'
print('Exercicio fatorial aquecimento: OK')

'''
EXERCICIO: terceirizando

Uma coisa fundamental para podermos usar recursao eh que possamos fazer uma terceirizacao
produtiva. Ou seja: que seja possivel usar uma versao *menor* do problema
para nos ajudar a resolver uma versao *maior*.

Se eu tenho a missao de calcular fatorial(101), eu posso fazer um while 
para fazer as multiplicacoes
fatorial_101 = 1*2*3*4...*99*100*101

Mas eu tambem posso notar que seria *util* se eu tivesse disponivel o fatorial_100.

Porque seria util?
fatorial_101 = 1*2*3*4...*99*100*101
               -----------------
                 fatorial_100

'''

fatorial_100 = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
fatorial_101 = 'coloque o valor aqui'
assert verifica(fatorial_101, 'fba13926f0f806fd20c8c39a3c77b39a791f6943a8afb4b9f625e6b9'), 'fatorial_101 incorreta'
print('Exercicio fatorial terceirizacao 1: OK')

'''
Exercicio: terceirização 2

Ainda nessa questão da terceirizacao, utilize os fatoriais que voce
ja calculou pra encadear novos fatoriais.

Voce ja sabe que `fatorial_2` = 2 e `fatorial_6` = 720. Use essas
variaveis em EXPRESSOES Python para preencher as proximas.

    fatorial_3 = fatorial_2 * 3     (terceiriza o fatorial_2)
    fatorial_4 = fatorial_3 * 4     (terceiriza o fatorial_3 que voce acabou de calcular!)

Repare: voce esta "encadeando" as terceirizacoes. Cada nova variavel
reusa a anterior — exatamente o que a funcao recursiva vai fazer
quando ela mesma se chamar.
'''
fatorial_2 = 1*2
fatorial_3 = 'coloque o valor aqui'
fatorial_4 = 'coloque o valor aqui'
fatorial_5 = 'coloque o valor aqui'



assert verifica(fatorial_3, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'fatorial_3 incorreta'
assert verifica(fatorial_4, '31e37d936439ee86e5496116c51ebf72018be157ed61a638dd510046'), 'fatorial_4 incorreta'
assert verifica(fatorial_4, '31e37d936439ee86e5496116c51ebf72018be157ed61a638dd510046'), 'fatorial_4 incorreta'
assert verifica(fatorial_5, '7cc795e70f15408932d47023cf93dba92d0e4304bc182adbee2c8816'), 'fatorial_5 incorreta'
print('Exercicio fatorial terceirizacao 2: OK')


# ===== FASE 2 - Funcao fatorial(n) recursiva =====

'''
EXPLICACAO

Pensando recursivamente:

    fatorial(5) = 5 * fatorial(4)
    fatorial(4) = 4 * fatorial(3)
    ...
    fatorial(1) = 1 * fatorial(0)
    fatorial(0) = 1   <- caso base, responde direto

Ou seja, pra calcular fatorial(n), basta calcular fatorial(n-1) e
multiplicar por n. O caso base e n == 0 (ou n == 1, tanto faz, mas
0 fecha tudo).
'''

'''
EXERCICIO

Implemente a funcao recursiva fatorial(n).

DICA: pra passar nos primeiros testes, basta acertar fatorial(0) e
fatorial(1). Depois incremente com a chamada recursiva.

    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(5)
    120
'''
def fatorial(n):
    pass

# Bloco 1: casos base.
# Esses sao os casos em que a funcao responde direto, sem se chamar.
assert fatorial(0) == 1, 'fatorial(0) deveria ser 1 (caso base)'
assert fatorial(1) == 1, 'fatorial(1) deveria ser 1 (caso base)'
print('Exercicio fatorial casos base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
# Aqui a funcao precisa se chamar (terceirizar) pra resolver.
assert fatorial(2) == 2, 'fatorial(2) deveria ser 2'
assert fatorial(5) == 120, 'fatorial(5) deveria ser 120'
assert fatorial(10) == 3628800, 'fatorial(10) deveria ser 3628800'
assert fatorial(50) == 30414093201713378043612608166064768844377641568960512000000000000, 'fatorial(50) incorreto'

sys.setrecursionlimit(50)
try:
    fatorial(60)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao fatorial e recursiva? (nao estourou o limite)')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio fatorial caso recursivo: OK')





# ===== FASE 5 - Listas: primeiro e todos_menos_primeiro =====

'''
EXPLICACAO

Lembrete sobre listas:

    >>> lista = [564, 706, 153, 969, 490]
    >>> lista[0]        # primeiro elemento (indice 0)
    564
    >>> lista[3]        # quarto elemento (indice 3)
    969
    >>> lista[1:]       # todos os elementos a partir do indice 1
    [706, 153, 969, 490]
    >>> lista[2:]       # todos os elementos a partir do indice 2
    [153, 969, 490]

`lista[i]` pega UM elemento. `lista[i:]` cria uma NOVA lista com o
elemento i e todos os seguintes (nao modifica a original).
'''

lista_exemplo = [564, 706, 153, 969, 490]

'''
EXERCICIO

Preencha as variaveis abaixo usando EXPRESSAO Python (nao o valor
literal). Use a `lista_exemplo` definida acima.

1) Qual o primeiro elemento de `lista_exemplo`?
   Dica: `lista_exemplo[0]`.
'''
primeiro_de_exemplo_t = 'coloque o valor aqui'

'''
2) Quais sao todos os elementos a partir do segundo (indice 1)?
   Dica: `lista_exemplo[1:]`.
'''
resto_de_exemplo_t = 'coloque o valor aqui'

assert verifica(primeiro_de_exemplo_t, '7faa4a030e8abce38b5114a76e64a4bb2937e944cc1e916f8e484e04'), 'primeiro_de_exemplo_t incorreta'
assert verifica(resto_de_exemplo_t, 'c3f1af8db4fd07a5d174c6bea2f2d5d214c30767a27aa42c546a309c'), 'resto_de_exemplo_t incorreta'
print('Exercicio aquecimento listas: OK')

'''
EXERCICIO

Defina a funcao `primeiro(lista)` que retorna o primeiro elemento.

    >>> primeiro([1, 2, 3])
    1
    >>> primeiro([5])
    5
'''
def primeiro(lista):
    pass

assert primeiro([1, 2, 3]) == 1, 'primeiro([1,2,3]) deveria ser 1'
assert primeiro([2, 3]) == 2, 'primeiro([2,3]) deveria ser 2'
assert primeiro([5]) == 5, 'primeiro([5]) deveria ser 5'
print('Exercicio primeiro: OK')

'''
EXERCICIO

Defina a funcao `todos_menos_primeiro(lista)` que retorna uma NOVA
lista com todos os elementos menos o primeiro.

    >>> todos_menos_primeiro([1, 2, 3])
    [2, 3]
    >>> todos_menos_primeiro([5])
    []
'''
def todos_menos_primeiro(lista):
    pass

assert todos_menos_primeiro([1, 2, 3]) == [2, 3], 'todos_menos_primeiro([1,2,3]) deveria ser [2,3]'
assert todos_menos_primeiro([2, 3]) == [3], 'todos_menos_primeiro([2,3]) deveria ser [3]'
assert todos_menos_primeiro([5]) == [], 'todos_menos_primeiro([5]) deveria ser []'
print('Exercicio todos_menos_primeiro: OK')


# ===== FASE 6 - maximo recursivo =====

'''
EXPLICACAO

A ideia para achar o maximo recursivamente: o maximo de uma lista
e o MAIOR entre:
    - o primeiro elemento (lista[0])
    - o maximo de TODOS os outros (recursivamente, em lista[1:])

Caso base: se a lista tem 1 elemento, o maximo e esse elemento.
'''

lista_para_max = [3, 10, 15, 30, 2, 1]

'''
EXERCICIO

Vamos ilustrar o passo recursivo com VARIAVEIS, antes de escrever a
funcao. Considere a `lista_para_max` declarada acima.

1) Qual o primeiro elemento? (use uma EXPRESSAO Python — `lista_para_max[0]`)
'''
primeiro_da_lista = 'coloque o valor aqui'

'''
2) Quais os demais elementos (a partir do indice 1)?
'''
resto_da_lista = 'coloque o valor aqui'

'''
3) Qual o maximo do RESTO? (terceirize — calcule a mao o maior numero
   dentro de [10, 15, 30, 2, 1])
'''
maximo_do_resto = 'coloque o valor aqui'

'''
4) Junte os pedacos: o maximo da lista inteira e o max entre o
   `primeiro_da_lista` e o `maximo_do_resto`.
   Use uma EXPRESSAO Python (`max(primeiro_da_lista, maximo_do_resto)`).
'''
maximo_da_lista = 'coloque o valor aqui'

assert verifica(primeiro_da_lista, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'primeiro_da_lista incorreta'
assert verifica(resto_da_lista, '8ba8d10adbd563af8012f5f99a21865676935170240ed9c957ddc493'), 'resto_da_lista incorreta'
assert verifica(maximo_do_resto, '6332531eeafc6e0ede272192be898f549950fb32b209d04f0a98306a'), 'maximo_do_resto incorreta'
assert verifica(maximo_da_lista, '6332531eeafc6e0ede272192be898f549950fb32b209d04f0a98306a'), 'maximo_da_lista incorreta'
print('Exercicio maximo terceirizacao: OK')

'''
EXERCICIO

Defina a funcao recursiva `maximo(lista)`.

DICA: comece com o caso base — lista de 1 elemento. Isso ja passa o
primeiro teste. Depois implemente a recursao usando `lista[0]` e o
maximo de `lista[1:]` (exatamente o que voce acabou de fazer nas
variaveis acima).

Voce pode usar `max(a, b)` do Python pra comparar dois numeros.

    >>> maximo([3])
    3
    >>> maximo([3, 10, 15, 30, 2, 1])
    30
'''
def maximo(lista):
    pass

# Bloco 1: casos base (lista com 1 elemento — responde direto).
assert maximo([1]) == 1, 'maximo([1]) eh 1 (caso base)'
assert maximo([3]) == 3, 'maximo([3]) eh 3 (caso base)'
assert maximo([-1]) == -1, 'maximo([-1]) eh -1 (caso base)'
print('Exercicio maximo casos base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert maximo([1, 2, 3]) == 3, '[1, 2, 3] -> max eh 3'
assert maximo([3, 2, 1]) == 3, '[3, 2, 1] -> max eh 3'
assert maximo([3, 10, 15, 30, 2, 1]) == 30, '3, 10, 15, 30, 2, 1 -> max eh 30'
assert maximo([-7, -1, -2]) == -1, 'so negativos: -7, -1, -2 -> max eh -1'

sys.setrecursionlimit(50)
try:
    maximo(list(range(100)))
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao maximo e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio maximo caso recursivo: OK')


# ===== FASE 7 - Strings: primeira_letra e todas_as_letras_menos_primeira =====

'''
EXPLICACAO

A mesma indexacao/slicing que vale pra lista vale pra string:

    >>> palavra = 'banana'
    >>> palavra[0]    # primeiro caractere
    'b'
    >>> palavra[2]    # terceiro caractere
    'n'
    >>> palavra[1:]   # a partir do indice 1
    'anana'

String eh quase uma "lista de letras".
'''

palavra_exemplo = 'banana'

'''
EXERCICIO

Use EXPRESSAO Python sobre `palavra_exemplo`.

1) Qual a primeira letra de `palavra_exemplo`?
'''
primeira_letra_de_banana_t = 'coloque o valor aqui'

'''
2) E o resto (a partir da segunda letra)?
'''
resto_de_banana_t = 'coloque o valor aqui'

assert verifica(primeira_letra_de_banana_t, 'c681e18b81edaf2b66dd22376734dba5992e362bc3f91ab225854c17'), 'primeira_letra_de_banana_t incorreta'
assert verifica(resto_de_banana_t, 'dc04b379e66b8de4b5fe0ee4434825b54509166525143208d3a1e544'), 'resto_de_banana_t incorreta'
print('Exercicio aquecimento strings: OK')

'''
EXERCICIO

Defina `primeira_letra(string)` e `todas_as_letras_menos_primeira(string)`.

    >>> primeira_letra('banana')
    'b'
    >>> todas_as_letras_menos_primeira('banana')
    'anana'
'''
def primeira_letra(string):
    pass

def todas_as_letras_menos_primeira(string):
    pass

assert primeira_letra('banana') == 'b', "primeira_letra('banana') deveria ser 'b'"
assert primeira_letra('abacaxi') == 'a', "primeira_letra('abacaxi') deveria ser 'a'"
assert todas_as_letras_menos_primeira('banana') == 'anana', "todas_as_letras_menos_primeira('banana') deveria ser 'anana'"
assert todas_as_letras_menos_primeira('abacaxi') == 'bacaxi', "todas_as_letras_menos_primeira('abacaxi') deveria ser 'bacaxi'"
print('Exercicio primeira_letra e todas_as_letras_menos_primeira: OK')


# ===== FASE 8 - inverte recursiva =====

'''
EXPLICACAO

Inverter recursivamente:

    inverte('banana')
        = inverte('anana') + 'b'
        = inverte('nana') + 'a' + 'b'
        = ...
        = '' + 'a' + 'n' + 'a' + 'n' + 'a' + 'b'
        = 'ananab'

A ideia: pega a primeira letra, inverte o resto (terceirize!), e
junta a primeira no FIM.

Casos base: '' (string vazia) e palavras com 1 letra ja estao
"invertidas" (sao iguais a si mesmas).
'''

string_para_inverter = 'mundo'

'''
EXERCICIO

Vamos ilustrar o passo recursivo com VARIAVEIS, antes de escrever a
funcao. Considere a `string_para_inverter` = 'mundo' declarada acima.

1) Qual o PRIMEIRO caractere dela?
   Use uma EXPRESSAO Python: `string_para_inverter[0]`.
'''
primeiro_caractere = 'coloque o valor aqui'

'''
2) Quais sao os DEMAIS caracteres (a partir do indice 1)?
   Use `string_para_inverter[1:]`.
'''
demais_caracteres = 'coloque o valor aqui'

'''
3) Agora terceirize: inverta a mao os DEMAIS caracteres (ou seja,
   inverta a string 'undo').
'''
demais_caracteres_invertidos = 'coloque o valor aqui'

'''
4) Pra montar a string toda invertida, junte: os `demais_caracteres_invertidos`
   PRIMEIRO, e depois o `primeiro_caractere` no fim.

   Use uma EXPRESSAO Python: `demais_caracteres_invertidos + primeiro_caractere`.
'''
string_invertida = 'coloque o valor aqui'

assert verifica(primeiro_caractere, '4fde0463771d8c4fb82794d5d6d003725c819dd34360e7bf9c70cffe'), 'primeiro_caractere incorreta'
assert verifica(demais_caracteres, '00f3196e190cd065a00ca396e40748ddea0147c0bb48801c63c6847c'), 'demais_caracteres incorreta'
assert verifica(demais_caracteres_invertidos, 'e4d8d42fbe32d0d8a6e9a49b09a29c1ceae9ff5a48d2e8fccf93002c'), 'demais_caracteres_invertidos incorreta'
assert verifica(string_invertida, '96d33cf17c4f06a10bda1df00b953e45f23f228c7385326c832e4ad3'), 'string_invertida incorreta'
print('Exercicio inverte terceirizacao: OK')

'''
EXERCICIO

Defina a funcao recursiva `inverte(palavra)`.

DICA: pra comecar, faca funcionar pra '' e palavras com 1 letra (sao
iguais a si mesmas). Depois implemente a recursao — exatamente o que
voce fez nas variaveis acima:

    inverte(palavra) = inverte(palavra[1:]) + palavra[0]

    >>> inverte('')
    ''
    >>> inverte('a')
    'a'
    >>> inverte('banana')
    'ananab'
'''
def inverte(palavra):
    pass

# Bloco 1: casos base.
assert inverte('') == '', "inverte('') deveria ser '' (caso base)"
assert inverte('a') == 'a', "inverte('a') deveria ser 'a' (caso base)"
print('Exercicio inverte casos base: OK')

# Bloco 2: caso recursivo + teste de recursividade.
assert inverte('ab') == 'ba', "inverte('ab') deveria ser 'ba'"
assert inverte('aba') == 'aba', "inverte('aba') deveria ser 'aba' (palindromo)"
assert inverte('abb') == 'bba', "inverte('abb') deveria ser 'bba'"
assert inverte('banana') == 'ananab', "inverte('banana') deveria ser 'ananab'"
assert inverte('mundo') == 'odnum', "inverte('mundo') deveria ser 'odnum'"

sys.setrecursionlimit(50)
try:
    inverte('a' * 100)
    sys.setrecursionlimit(1000)
    raise AssertionError('a sua funcao inverte e recursiva?')
except RecursionError:
    sys.setrecursionlimit(1000)
print('Exercicio inverte caso recursivo: OK')


# ===== FASE 9 - acha_segredo em listas aninhadas =====

'''
EXPLICACAO

Imagine que voce esta procurando um arquivo no computador. Voce
comeca no drive C, mas se nao acha, precisa descer pras pastas
dentro dele — e dentro de cada uma dessas, pode ter MAIS pastas.

Vamos implementar essa logica procurando a string 'segredo' em uma
LISTA DE LISTAS. O segredo pode estar:
    - na lista principal
    - dentro de uma lista que esta na lista principal
    - dentro de uma lista dentro de uma lista (e assim por diante)

Pra ajudar, ja definimos a funcao `eh_lista(x)` no fim do arquivo
(retorna True se x e uma lista, False se nao e).

Exemplos:
'''
lista_com_segredo = [1, [2, 'segredo'], 3]
lista_sem_segredo = [1, [2, [3, 4]], 5]


'''
EXERCICIO

Defina a funcao recursiva `acha_segredo(lista)` que retorna True se
'segredo' aparece em qualquer nivel da lista, False caso contrario.

DICA: percorra a lista. Pra cada item:
    - se item == 'segredo', achou (retorna True)
    - se eh_lista(item), faca a chamada recursiva — se ela retornar
      True, voce achou
    - senao, segue procurando
Se chegou no fim sem achar, retorna False.

    >>> acha_segredo([1, [2, 'segredo'], 3])
    True
    >>> acha_segredo([1, [2, [3, 4]], 5])
    False
    >>> acha_segredo(['segredo'])
    True
    >>> acha_segredo([])
    False
'''
def acha_segredo(lista):
    pass

# Bloco 1: casos base (lista vazia ou com o segredo no topo, sem
# precisar terceirizar).

assert acha_segredo([]) == False, 'lista vazia: sem segredo (caso base)'
assert acha_segredo(['segredo']) == True, "['segredo'] tem o segredo direto (caso base)"
assert acha_segredo([1, 2, 3]) == False, 'so numeros no topo: sem segredo'
assert acha_segredo([1, 'segredo', 3]) == True, "'segredo' no topo, ainda sem precisar terceirizar"
print('Exercicio acha_segredo casos base: OK')

# Bloco 2: caso recursivo (segredo dentro de sublistas, precisa
# terceirizar) + cobertura ampla com listas aleatorias.
lista_com_segredo = [1, [2, 'segredo'], 3]
lista_sem_segredo = [1, [2, [3, 4]], 5]
assert acha_segredo(lista_com_segredo) == True, 'lista_com_segredo deveria ter o segredo'
assert acha_segredo(lista_sem_segredo) == False, 'lista_sem_segredo NAO deveria ter o segredo'
assert acha_segredo([[[['segredo']]]]) == True, 'segredo bem fundo'
assert acha_segredo([1, 2, 3, [4, 5, [6, 7]]]) == False, 'sem segredo em varios niveis'

# Cobertura ampla: gera 100 listas aleatorias e confere
random.seed(42)
for _i in range(100):
    _coloca = (_i % 2 == 0)
    _pasta = gera_r(4, 8, _coloca)
    assert acha_segredo(_pasta) == _coloca, f'acha_segredo errou no caso {_i} (esperado {_coloca})'

print('Exercicio acha_segredo caso recursivo: OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')

