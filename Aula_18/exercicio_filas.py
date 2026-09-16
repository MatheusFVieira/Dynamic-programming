# Exercicio - grafos, antes do metro: a fila (a roda de Josephus).

# === Helper de verificacao (pode ignorar) ===
# So as tres simulacoes a mao do comeco usam a funcao `verifica`: ela
# compara o seu valor com a resposta correta (que fica escondida em
# formato de hash). Voce nao precisa entender ela - se voce errou, ela
# imprime "Valor errado: voce colocou X" e o assert logo abaixo dispara.
# As funcoes, mais pra baixo, sao conferidas com assert normal, que mostra
# o esperado e o que voce devolveu.
import hashlib
def verifica(valor, codigo, ordem_importa=False, nome_questao=''):
    if isinstance(valor, tuple):
        valor = list(valor)
    if isinstance(valor, dict):
        valor = sorted(valor.items())
    valores = [valor]
    if isinstance(valor, list):
        valores = [valor if ordem_importa else sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    def _hash(v):
        s = f'{nome_questao}:{v}' if nome_questao else str(v)
        return hashlib.sha224(s.encode('utf-8')).hexdigest()
    respostas = [_hash(v) == codigo for v in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True
# fim do helper

'''
EXPLICACAO

O problema de Josephus eh assim conhecido por causa da lenda de Flavius
Josephus, um historiador que viveu no seculo 1. Segundo o relato de
Josephus do cerco de Yodfat, ele e seus companheiros (40 soldados) foram
presos em uma caverna, cuja saida foi bloqueada pelos romanos.

Eles preferiram suicidar-se a serem capturados, e decidiram que iriam
formar um circulo e comecar a matar-se pulando de tres em tres. Josephus
afirma que, por sorte ou talvez pela mao de Deus, ele permaneceu por
ultimo e preferiu entregar-se aos romanos a suicidar-se.

Na nossa roda, as pessoas sao numeradas de 1 ate `pessoas`, e o `pulo`
diz de quantas em quantas sai uma: com pulo = 3, conta-se 1, 2, 3, e o
terceiro sai. A contagem recomeca de quem estava logo depois dele.

Junto desse arquivo ha uma imagem, josephus.jpg, fazendo o exemplo com 5
pessoas e pulo = 2: saem o 2, o 4, o 1 e o 5, nessa ordem, e sobra o 3.

Esse eh um problema classico, e tem nome: PROBLEMA DE JOSEPHUS. Eh assim
que voce vai encontrar ele nos sites de exercicio.
'''


'''
ENUNCIADO

Faca o miolo de um SIMULADOR DA RODA DE JOSEPHUS.

Um grupo de pessoas forma uma roda, numeradas de 1 ate o total. Contando
em volta da roda, sai uma pessoa de n em n - e a contagem
recomeca de quem estava logo depois dela. Sai gente ate sobrar uma so.

Por um menu, o usuario pode:

  1) MONTAR uma roda nova: quantas pessoas, e de quantas em quantas sai uma;
  2) andar UMA RODADA: ver quem saiu e quem continua na roda;
  3) ver QUEM SOBRA no fim, sem mexer na roda atual;
  4) ver a LISTA POR DENTRO: a lista inteira, o proximo, e quantos estao
     na roda de verdade;
  5) SAIR.

Regras:

  - a roda tem pelo menos 1 pessoa, e sai uma de pelo menos 1 em 1;
  - quando sobra uma pessoa so, a roda acabou: andar mais uma rodada nao
    tira ninguem;
  - as pessoas sao numeradas de 1 ate o total.

O menu ja esta pronto la embaixo. O que falta sao tres simulacoes a mao,
logo no comeco, e seis funcoes.
'''

'''
EXPLICACAO

A roda desta aula eh uma FILA. Fila eh um jeito de guardar coisas que tem
duas operacoes basicas: INSERE e RETIRA.

A ideia eh que quem eh inserido entra "no fim" da fila, e, quando
retiramos alguem, sai o mais antigo, que esta "na frente".

Eh uma fila de supermercado: quem chega entra no fim, e quem eh atendido
eh quem esta la ha mais tempo.

Ou seja: quem entrou primeiro sai primeiro. Em ingles isso tem nome, e
voce vai reencontrar ele: FIRST IN, FIRST OUT, ou FIFO.
'''

'''
EXPLICACAO

Em Python, a melhor maneira de implementar é usar
uma LISTA mais um INDICE que anda - uma variavel
`proximo`, que guarda a POSICAO do primeiro elemento que ainda esta na fila
o proximo a sair.

    fila = []
    proximo = 0

INSERE eh o append de sempre: o novo entra no fim da lista.

    fila.append(2)

    fila == [2]
             ^
             --- proximo = 0 (o indice)

    Vamos fazer mais duas insersoes

    fila.append(7)
    fila.append(12)

    fila == [2, 7 ,12]
             ^
             --- proximo = 0 (o indice)

RETIRA nao apaga ninguem da lista. Indicamos que o 2
saiu ao aumentar a variavel proximo

    quem_saiu = fila[proximo]
    proximo = proximo + 1

    fila == [2, 7 ,12]
                ^
                --- proximo = 1 (o indice)



Repare: quem ja saiu CONTINUA na lista, mas a gente considera que SAIU 
da fila, por estar nas posicoes antes do `proximo`.
Quem esta na fila de verdade? Do indice `proximo` ate o fim

Em vocabulario de estrutura de dados, a frente da fila se chama FRONT e o
fim se chama BACK; inserir eh ENQUEUE e retirar eh DEQUEUE.

EXEMPLO

    comecando com a fila vazia:  fila = [],         proximo = 0
    insere(2)                    fila = [2],        proximo = 0
    insere(5)                    fila = [2, 5],     proximo = 0
    insere(1)                    fila = [2, 5, 1],  proximo = 0
    retira()      sai o 2        fila = [2, 5, 1],  proximo = 1

No fim, quem esta na fila de verdade sao o 5 e o 1 - o fila[1:] -, mas a
lista continua com os tres.

Esse exemplo voce responderia assim:
'''

fila_exemplo = [2, 5, 1]    # isso eh a resposta do exemplo acima, que eu ja deixei feita
proximo_exemplo = 1


'''
EXERCICIO

Comece com uma fila vazia: fila = [], proximo = 0.
Execute:
    insere(3)
    insere(4)
    insere(1)
    insere(2)

Como ficam a lista e o proximo? Responda a lista, em forma de lista, na
variavel fila1, e o proximo na variavel proximo1.
'''
fila1 = [3,4,1,2]
proximo1 = 0

assert verifica(fila1, 'c075a25eb0397123b4e117fdd66afac421ddd2850684763be50c0941', ordem_importa=True, nome_questao='fila1'), 'fila1 incorreta'
assert verifica(proximo1, 'b5258f189284587bd7c60ee12d8c3a7944e77758a49aae1f9b473e52', nome_questao='proximo1'), 'proximo1 incorreto'
print('Exercicio 1 (fila1 e proximo1): OK')


'''
EXERCICIO

Comece com uma fila vazia: fila = [], proximo = 0.
Execute:
    insere(3)
    insere(4)
    retira()
    insere(1)
    insere(2)
    retira()

Como ficam a lista e o proximo? Responda a lista, em forma de lista, na
variavel fila2, e o proximo na variavel proximo2.
'''
fila2 = [3, 4, 1, 2]
proximo2 = 2

assert verifica(fila2, '8a94b78f9030e6475ca315f110cb070e5e25942046d79e1ca3dd233e', ordem_importa=True, nome_questao='fila2'), 'fila2 incorreta - lembre que retirar nao apaga ninguem da lista, so anda o proximo'
assert verifica(proximo2, 'f1e8dbdf153f8d7c3d59d34710231c522d6f72cabf6c0fb418554f32', nome_questao='proximo2'), 'proximo2 incorreto'
print('Exercicio 2 (fila2 e proximo2): OK')


'''
EXERCICIO

Comece com uma fila vazia: fila = [], proximo = 0.
Execute:
    insere(3)
    insere(4)
    retira()
    insere(1)
    retira()
    insere(2)
    retira()
    insere(7)

Como ficam a lista e o proximo? Responda a lista, em forma de lista, na
variavel fila3, e o proximo na variavel proximo3.
'''
fila3 = [3, 4, 1, 2, 7]
proximo3 = 3

assert verifica(fila3, 'ba600c9f29eebf9fe2c60a07552f903975234072e25100fa7b14cc7a', ordem_importa=True, nome_questao='fila3'), 'fila3 incorreta - lembre que retirar nao apaga ninguem da lista, so anda o proximo'
assert verifica(proximo3, 'fef6ef6ab46ba2ef9716998af600af5bb10210cbb93819ebebeefb80', nome_questao='proximo3'), 'proximo3 incorreto'
print('Exercicio 3 (fila3 e proximo3): OK')


'''
EXPLICACAO

Quantas pessoas estao na fila? Aqui mora uma armadilha. Como nada nunca
sai da lista, o len(fila) conta TAMBEM quem ja foi embora:

    fila = [2, 5, 1]
    proximo = 1              # o 2 ja saiu

    len(fila)              -> 3, contando o 2, que ja foi embora
    len(fila) - proximo    -> 2, que sao o 5 e o 1

Quem ja saiu esta nas posicoes ANTES do proximo - as posicoes 0, 1, ...,
proximo - 1, que sao exatamente `proximo` pessoas. Tirando elas, sobra a
fila de verdade.
'''

'''
EXERCICIO

Faca uma funcao tamanho(fila, proximo) que devolve quantas pessoas ainda
estao na fila.

    >>> tamanho([2, 5, 1], 1)
    2
'''
def tamanho(fila, proximo):
    return len(fila) - proximo
    pass


# Os testes abaixo batem sempre na mesma tecla: nada sai da lista, entao o
# len(fila) conta tambem quem ja foi embora. Quem saiu esta nas posicoes
# antes do proximo - sao `proximo` pessoas -, e por isso a fila de verdade
# tem len(fila) - proximo.

# Ninguem saiu ainda (proximo = 0). Aqui o len(fila) acerta - mas so por
# coincidencia: nenhuma posicao ficou para tras.
assert tamanho([10, 20, 30], 0) == 3, f'ninguem saiu, os tres estao na fila; voce devolveu {tamanho([10, 20, 30], 0)}'

# O 10 e o 20 ja sairam: estao nas posicoes 0 e 1, antes do proximo (2). A
# lista ainda tem tres numeros, mas na fila so sobrou o 30.
assert tamanho([10, 20, 30], 2) == 1, f'o 10 e o 20 ja sairam, so o 30 continua na fila - o len(fila) contaria os tres; voce devolveu {tamanho([10, 20, 30], 2)}'

# Todo mundo saiu (proximo = 3, o tamanho da lista): a lista esta cheia, e
# a fila esta vazia.
assert tamanho([10, 20, 30], 3) == 0, f'os tres ja sairam, a fila esta vazia - mesmo com a lista tendo tres numeros; voce devolveu {tamanho([10, 20, 30], 3)}'

# A fila que nunca recebeu ninguem.
assert tamanho([], 0) == 0, f'fila nova, sem ninguem; voce devolveu {tamanho([], 0)}'

# A lista CRESCE quando alguem vai da frente pro fim: aqui o 10 e o 20
# sairam da frente e entraram de novo no fim. Sao cinco posicoes, duas ja
# ficaram para tras (as de antes do proximo), e na fila estao tres pessoas:
# o 30, o 10 e o 20.
assert tamanho([10, 20, 30, 10, 20], 2) == 3, f'cinco posicoes na lista, duas antes do proximo: sobram tres na fila; voce devolveu {tamanho([10, 20, 30, 10, 20], 2)}'
print('Exercicio 4 (tamanho): OK')


'''
EXERCICIO

Faca uma funcao primeiro(fila, proximo) que devolve quem esta na frente
da fila - quem seria o proximo a sair -, SEM retirar ninguem.

Cuidado: a frente da fila NAO eh o fila[0]. A posicao 0 eh de quem entrou
primeiro na lista, e essa pessoa pode ja ter saido.

So vale chamar com a fila nao vazia: numa fila vazia nao ha ninguem na
frente.

    >>> primeiro([2, 5, 1], 1)
    5
'''
def primeiro(fila, proximo):
    return fila[proximo]
    pass


assert primeiro([10, 20, 30, 40], 0) == 10, f'ninguem saiu ainda, o 10 esta na frente; voce devolveu {primeiro([10, 20, 30, 40], 0)}'
assert primeiro([10, 20, 30, 40], 2) == 30, f'o 10 e o 20 ja sairam (estao antes do proximo), entao quem esta na frente eh o 30; voce devolveu {primeiro([10, 20, 30, 40], 2)}'
fila_t = [10, 20, 30, 40]
primeiro(fila_t, 1)
assert fila_t == [10, 20, 30, 40], f'olhar quem esta na frente nao pode mexer na lista; ela ficou {fila_t}'
print('Exercicio 5 (primeiro): OK')


'''
EXPLICACAO

A roda gira assim: quem esta na frente sai da frente e entra de novo no
fim. Na nossa fila, eh um RETIRA seguido de um INSERE da mesma pessoa:

    fila = [1, 2, 3],       proximo = 0     na fila de verdade: [1, 2, 3]

    depois de girar uma vez:

    fila = [1, 2, 3, 1],    proximo = 1     na fila de verdade: [2, 3, 1]

A partir daqui, as funcoes recebem a fila E o proximo. Repare que eles
sao de tipos diferentes em Python:

  - a fila eh uma LISTA, e lista eh MUTAVEL: o append que a funcao faz
    muda a mesma lista que esta la fora. Nao precisa devolver a lista.
  - o proximo eh um NUMERO, e numero eh IMUTAVEL: a funcao nao consegue
    mudar o proximo de quem a chamou. Por isso ela DEVOLVE o novo proximo,
    e quem chama guarda:

        proximo = vira_1(fila, proximo)
'''

'''
EXERCICIO

Faca uma funcao vira_1(fila, proximo) que tira quem esta na frente da
fila e coloca de novo no fim. Devolve o novo proximo.

    >>> fila = [1, 2, 3]
    >>> proximo = vira_1(fila, 0)
    >>> proximo
    1
    >>> fila
    [1, 2, 3, 1]
    >>> fila[proximo:]
    [2, 3, 1]
'''
def vira_1(fila, proximo):
    fila.append(fila[proximo])
    return proximo + 1
    pass


fila_t = [1, 2, 3]
proximo_t = vira_1(fila_t, 0)
assert proximo_t == 1, f'o indice tem que andar uma casa, e a funcao tem que DEVOLVER o proximo novo; voce devolveu {proximo_t}'
assert fila_t == [1, 2, 3, 1], f'o 1 entra de novo no fim, e NINGUEM sai da lista; a lista ficou {fila_t}'
proximo_t = vira_1(fila_t, proximo_t)
assert proximo_t == 2 and fila_t == [1, 2, 3, 1, 2], f'girando de novo, agora eh o 2 que vai pro fim; ficou fila = {fila_t}, proximo = {proximo_t}'
assert tamanho(fila_t, proximo_t) == 3, 'girar a roda nao muda quantas pessoas estao nela'
assert primeiro(fila_t, proximo_t) == 3, 'depois de girar duas vezes, o 3 esta na frente'

# A frente NAO eh a posicao 0: aqui o 10 ja saiu, e quem gira eh o 20.
fila_t = [10, 20, 30]
proximo_t = vira_1(fila_t, 1)
assert proximo_t == 2 and fila_t == [10, 20, 30, 20], f'quem gira eh quem esta na posicao proximo (o 20), e nao na posicao 0; ficou fila = {fila_t}, proximo = {proximo_t}'
print('Exercicio 6 (vira_1): OK')


'''
EXERCICIO

Faca uma funcao vira_n(fila, proximo, n) que gira a roda n vezes: o da
frente vai pro fim, depois o novo da frente vai pro fim, e assim por
diante, n vezes no total. Devolve o novo proximo.

Use o vira_1 - e guarde o proximo que ele devolve a cada volta, senao a
volta seguinte gira a mesma pessoa de novo.

    >>> fila = [1, 2, 3, 4, 5, 6]
    >>> proximo = vira_n(fila, 0, 3)
    >>> proximo
    3
    >>> fila
    [1, 2, 3, 4, 5, 6, 1, 2, 3]
    >>> fila[proximo:]
    [4, 5, 6, 1, 2, 3]

O n pode ser maior do que o numero de pessoas na fila - a roda so da mais
de uma volta. E o n pode ser 0: ai nada gira.
'''
def vira_n(fila, proximo, n): 
    i = 0 
    while i < n: 
        proximo = vira_1(fila, proximo) 
        i += 1 
    return proximo
    pass


fila_t = [1, 2, 3, 4, 5, 6]
proximo_t = vira_n(fila_t, 0, 3)
assert proximo_t == 3, f'girando 3 vezes, o indice anda 3 casas; voce devolveu {proximo_t}'
assert fila_t == [1, 2, 3, 4, 5, 6, 1, 2, 3], f'o 1, o 2 e o 3 entram de novo no fim, nessa ordem; a lista ficou {fila_t}'
proximo_t = vira_n(fila_t, proximo_t, 3)
assert fila_t[proximo_t:] == [1, 2, 3, 4, 5, 6], f'mais 3 e a roda deu a volta inteira; na fila de verdade ficou {fila_t[proximo_t:]}'
proximo_t = vira_n(fila_t, proximo_t, 1)
assert fila_t[proximo_t:] == [2, 3, 4, 5, 6, 1], f'mais 1 e o 1 vai pro fim; na fila de verdade ficou {fila_t[proximo_t:]}'

# n = 0: nada gira.
fila_t = [7, 8]
proximo_t = vira_n(fila_t, 0, 0)
assert proximo_t == 0 and fila_t == [7, 8], f'girar 0 vezes nao muda nada; ficou fila = {fila_t}, proximo = {proximo_t}'

# n maior que a fila: com tres pessoas, girar 5 vezes da uma volta inteira
# e mais duas.
fila_t = [1, 2, 3]
proximo_t = vira_n(fila_t, 0, 5)
assert fila_t[proximo_t:] == [3, 1, 2], f'o 1, o 2, o 3, o 1 e o 2 giram; na fila de verdade ficou {fila_t[proximo_t:]}'
print('Exercicio 7 (vira_n): OK')


'''
EXERCICIO

Faca uma funcao vira_n_sai_1(fila, proximo, n) que gira a roda n vezes,
como o vira_n, e depois RETIRA quem ficou na frente - sem colocar de
volta. Devolve o novo proximo.

    >>> fila = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> proximo = vira_n_sai_1(fila, 0, 4)
    #   o 1, o 2, o 3 e o 4 vao pro fim; o 5 sai e nao volta
    >>> proximo
    5
    >>> fila[proximo:]
    [6, 7, 8, 9, 1, 2, 3, 4]
    >>> fila[proximo - 1]
    5

Repare na ultima linha: quem saiu continua na lista, logo antes do
proximo. Nada sai da lista - so o indice anda.
'''
def vira_n_sai_1(fila, proximo, n):
    i = 0 
    while i < n: 
        proximo = vira_1(fila, proximo) 
        i += 1 
    proximo += 1
    return proximo
    pass


fila_t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
proximo_t = vira_n_sai_1(fila_t, 0, 4)
assert proximo_t == 5, f'o 1, o 2, o 3 e o 4 giram (4 casas) e o 5 sai (mais uma): o proximo vai pra 5; voce devolveu {proximo_t}'
assert fila_t == [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4], f'os quatro que giraram entram no fim, e o 5 NAO entra de novo; a lista ficou {fila_t}'
assert fila_t[proximo_t - 1] == 5, 'quem saiu continua na lista, logo antes do proximo'
proximo_t = vira_n_sai_1(fila_t, proximo_t, 4)
assert fila_t[proximo_t:] == [2, 3, 4, 6, 7, 8, 9], f'o 6, o 7, o 8 e o 9 giram, e o 1 sai; na fila de verdade ficou {fila_t[proximo_t:]}'
proximo_t = vira_n_sai_1(fila_t, proximo_t, 4)
assert fila_t[proximo_t:] == [8, 9, 2, 3, 4, 6], f'o 2, o 3, o 4 e o 6 giram, e o 7 sai; na fila de verdade ficou {fila_t[proximo_t:]}'
proximo_t = vira_n_sai_1(fila_t, proximo_t, 4)
assert fila_t[proximo_t:] == [6, 8, 9, 2, 3], f'o 8, o 9, o 2 e o 3 giram, e o 4 sai; na fila de verdade ficou {fila_t[proximo_t:]}'

# n = 0: ninguem gira, e quem esta na frente sai direto.
fila_t = [1, 2, 3]
proximo_t = vira_n_sai_1(fila_t, 0, 0)
assert proximo_t == 1 and fila_t == [1, 2, 3], f'sem girar, o 1 sai e a lista nao ganha ninguem; ficou fila = {fila_t}, proximo = {proximo_t}'

# n maior que a roda: com duas pessoas, girar 3 vezes da mais de uma volta.
fila_t = [1, 2]
proximo_t = vira_n_sai_1(fila_t, 0, 3)
assert fila_t[proximo_t:] == [1], f'o 1, o 2 e o 1 de novo giram, e o 2 sai; na fila de verdade ficou {fila_t[proximo_t:]}'
print('Exercicio 8 (vira_n_sai_1): OK')



'''
EXERCICIO

Faca uma funcao sobrevivente(pessoas, pulo) que monta a roda com as
pessoas numeradas de 1 ate `pessoas`, tira uma de `pulo` em `pulo` ate
sobrar uma so, e devolve o numero de quem sobrou.

Um jeito:

  - comece com a lista [1, 2, ..., pessoas] (um for com append resolve) e
    o proximo em 0;
  - enquanto tiver mais de uma pessoa na fila, faca uma rodada com o
    vira_n_sai_1;
  - quando sobrar uma so, ela eh quem esta na frente.

Cuidado com a contagem: com pulo = 3, contam-se 1, 2, 3 e o TERCEIRO sai
- ou seja, giram dois.

    >>> sobrevivente(5, 2)
    3

Exemplo completo: sobrevivente(10, 3)

    fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], proximo = 0

    1a rodada: o 1 e o 2 giram, e o 3 sai
        fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2], proximo = 3
        na fila de verdade: [4, 5, 6, 7, 8, 9, 10, 1, 2]

    2a rodada: o 4 e o 5 giram, e o 6 sai
        fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 4, 5], proximo = 6
        na fila de verdade: [7, 8, 9, 10, 1, 2, 4, 5]

    daqui em diante, so a fila de verdade:
    3a rodada: sai o 9     ->  [10, 1, 2, 4, 5, 7, 8]
    4a rodada: sai o 2     ->  [4, 5, 7, 8, 10, 1]
    5a rodada: sai o 7     ->  [8, 10, 1, 4, 5]
    6a rodada: sai o 1     ->  [4, 5, 8, 10]
    7a rodada: sai o 8     ->  [10, 4, 5]
    8a rodada: sai o 5     ->  [10, 4]
    9a rodada: sai o 10    ->  [4]

    sobrou o 4
'''
def sobrevivente(pessoas, pulo):
    pass


print('  iniciando os testes do sobrevivente')
print('  (Se travar aqui, aperte Ctrl+C: a roda nao esta diminuindo - confira se cada rodada TIRA')
print('   alguem. E se der "IndexError: list index out of range", confira o seu while: quantas')
print('   pessoas ainda estao na roda eh tamanho(fila, proximo), e nao len(fila), que nunca diminui.)')
assert sobrevivente(1, 7) == 1, f'roda de uma pessoa so: ninguem sai, e ela sobra; voce devolveu {sobrevivente(1, 7)}'
assert sobrevivente(5, 3) == 4, f'com 5 pessoas de tres em tres saem o 3, o 1, o 5, o 2, sobra o 4; voce devolveu {sobrevivente(6, 3)}'
assert sobrevivente(5, 2) == 3, f'o exemplo da imagem: saem o 2, o 4, o 1 e o 5, e sobra o 3; voce devolveu {sobrevivente(5, 2)}'
assert sobrevivente(10, 3) == 4, f'o exemplo completo do enunciado; voce devolveu {sobrevivente(10, 3)}'
assert sobrevivente(5, 1) == 5, f'pulo 1: sai todo mundo na ordem, e o ultimo sobra; voce devolveu {sobrevivente(5, 1)}'
assert sobrevivente(6, 3) == 1, f'com 6 pessoas de tres em tres saem o 3, o 6, o 4, o 2 e o 5; voce devolveu {sobrevivente(6, 3)}'
assert sobrevivente(4, 6) == 3, f'pulo maior que a roda: a contagem da mais de uma volta antes de alguem sair; voce devolveu {sobrevivente(4, 6)}'
assert sobrevivente(41, 3) == 31, f'a roda da lenda, 41 pessoas de tres em tres - na versao mais contada, 31 eh o lugar que Josephus escolheu; voce devolveu {sobrevivente(41, 3)}'
assert sobrevivente(1234, 233) == 25, f'uma roda grande, 1234 pessoas com pulo 233; voce devolveu {sobrevivente(1234, 233)}'
print('Exercicio 9 (sobrevivente): OK')

print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== O menu =====
#
# Ja esta pronto - eh o seu simulador rodando em cima das funcoes que voce
# escreveu. Pra usar, descomente a ultima linha do arquivo.

def main():
    pessoas = 41    # o app comeca com a roda da lenda
    pulo = 3
    fila = []
    for pessoa in range(1, pessoas + 1):
        fila.append(pessoa)
    proximo = 0

    while True:
        print()
        print('=== RODA DE JOSEPHUS ===')
        print(f'{pessoas} pessoas, sai uma de {pulo} em {pulo}')
        print(f'na roda: {fila[proximo:]}')
        print('1. Montar uma roda nova')
        print('2. Andar uma rodada')
        print('3. Quem sobra no fim')
        print('4. Ver a lista por dentro')
        print('5. Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            quantas = input('  quantas pessoas: ')
            de_quantas = input('  sai uma de quantas em quantas: ')
            if not quantas.isdigit() or not de_quantas.isdigit() or int(quantas) < 1 or int(de_quantas) < 1:
                print('  as duas respostas tem que ser numeros inteiros, de 1 pra cima')
            else:
                pessoas = int(quantas)
                pulo = int(de_quantas)
                fila = []
                for pessoa in range(1, pessoas + 1):
                    fila.append(pessoa)
                proximo = 0
                print(f'  roda nova, com {pessoas} pessoas')

        elif opcao == '2':
            if tamanho(fila, proximo) == 1:
                print(f'  a roda ja acabou: sobrou o {primeiro(fila, proximo)}')
            else:
                proximo = vira_n_sai_1(fila, proximo, pulo - 1)
                # quem saiu continua na lista, logo antes do proximo
                print(f'  saiu o {fila[proximo - 1]}')

        elif opcao == '3':
            print(f'  no fim, sobra o {sobrevivente(pessoas, pulo)}')

        elif opcao == '4':
            print(f'  a lista inteira: {fila}')
            print(f'  proximo = {proximo}')
            print(f'  len(fila) = {len(fila)}, mas na roda de verdade estao {tamanho(fila, proximo)}')

        elif opcao == '5':
            break

        else:
            print('Opcao invalida')


# Pra rodar o app, descomente:
# main()


# ===== Depois desta aula: filas num juiz online =====
#
# A fila desta aula - uma lista mais um indice que anda - eh a mesma que a
# busca em largura vai usar na aula do metro. Antes dela, da pra treinar
# em dois problemas de fila, que se resolvem so com o que voce escreveu
# aqui. E tem o proprio Josephus, que eh outra historia.
#
# OS PROBLEMAS DE FILA
#
#   LC 2073 - Time Needed to Buy Tickets
#       https://leetcode.com/problems/time-needed-to-buy-tickets
#       n pessoas numa fila de ingressos, e tickets[i] eh quantos a pessoa
#       i quer comprar. A cada segundo, quem esta na frente compra UM
#       ingresso: se ainda quer mais, volta pro fim; se nao, vai embora.
#       Quanto tempo ate a pessoa k terminar de comprar?
#
#       Eh o vira_1 com uma condicao: a pessoa so volta pro fim se ainda
#       faltar ingresso pra ela. Ponha na fila os NUMEROS das pessoas (0,
#       1, 2, ...), guarde numa lista a parte quantos ingressos faltam pra
#       cada uma, e conte os segundos a cada retirada. n e tickets[i] vao
#       so ate 100, entao a fila da no maximo 10 mil voltas - nada aperta.
#
#   LC 1700 - Number of Students Unable to Eat Lunch
#       https://leetcode.com/problems/number-of-students-unable-to-eat-lunch
#       Os alunos estao numa FILA, e os sanduiches numa PILHA (o de cima eh
#       o sandwiches[0]). Quem esta na frente pega o sanduiche de cima se
#       gostar dele, e vai embora; se nao gostar, volta pro fim. Quantos
#       ficam sem comer?
#
#       Duas pecas a mais que o 2073:
#         - a pilha de sanduiches tambem se resolve com um indice que anda
#           - um `topo`, que avanca quando alguem pega o sanduiche de cima.
#           Nada sai da lista de sanduiches, igual a fila;
#         - a fila NAO acaba sozinha. Se todo mundo que esta nela voltou
#           pro fim, um seguido do outro, sem ninguem comer, ninguem vai
#           comer mais. Conte quantos voltaram seguidos (e zere a conta
#           quando alguem come), e pare quando ela chegar no
#           tamanho(fila, proximo). A resposta eh esse tamanho.
#
# E O PROPRIO JOSEPHUS?
#
#   LC 1823 - Find the Winner of the Circular Game
#       https://leetcode.com/problems/find-the-winner-of-the-circular-game
#       Eh esta aula com outros nomes: n amigos numa roda, sai um de k em
#       k, quem sobra? O n vai so ate 500, e o sobrevivente() desta aula
#       passa - medido, o pior caso roda em 0,02 segundo. Mas o problema
#       termina pedindo tempo linear e memoria CONSTANTE, e isso a roda nao
#       faz: nada sai da lista, e ela cresce ate umas n * k posicoes.
#
#   beecrowd 1030 - A Lenda de Flavious Josephus
#       https://judge.beecrowd.com/pt/problems/view/1030
#       O enunciado eh a lenda que esta la em cima, e aqui simular nao da.
#       O n vai ate 10 mil, o k ate mil, e sao ate 30 rodas por entrada.
#       Medido: a roda mais pesada leva 0,7 segundo e a lista chega a 10
#       milhoes de posicoes; trinta delas levam uns 20 segundos, muito
#       mais do que o juiz espera.
#
# Os dois pedem a RECORRENCIA: uma conta que acha o sobrevivente sem
# montar a roda.
#
# A RECORRENCIA DO JOSEPHUS
#
# Numere as POSICOES da roda a partir de 0, e chame de J(n) a posicao do
# sobrevivente numa roda de n pessoas, com o pulo k fixo. A pessoa eh a
# posicao mais 1.
#
# Com n = 5 e k = 2, a roda eh
#
#     posicao:  0  1  2  3  4
#     pessoa:   1  2  3  4  5
#
# A primeira rodada tira o 2. Sobram quatro, e a contagem recomeca do 3:
#
#     posicao na roda nova:  0  1  2  3
#     pessoa:                3  4  5  1
#
# Isso eh uma roda de 4 pessoas, com o mesmo k - so que comecando do 3.
# Entao quem sobra na roda de 5 eh quem sobra na roda de 4, J(4), traduzido
# de volta pra numeracao antiga.
#
# E a traducao eh andar k casas: a posicao 0 da roda nova eh a posicao 2
# da antiga, a 1 eh a 3, a 2 eh a 4, e a 3 eh a 0 - que eh onde a roda deu
# a volta. Ou seja:
#
#     J(5) = (J(4) + 2) % 5
#
# O `% 5` eh o "deu a volta". Para uma roda qualquer:
#
#     J(n) = (J(n - 1) + k) % n
#     J(1) = 0                      # sozinho na roda, ele eh a posicao 0
#
# Conferindo com n = 5 e k = 2, de baixo pra cima:
#
#     J(1) = 0
#     J(2) = (0 + 2) % 2 = 0
#     J(3) = (0 + 2) % 3 = 2
#     J(4) = (2 + 2) % 4 = 0
#     J(5) = (0 + 2) % 5 = 2        # posicao 2 eh a pessoa 3, como na imagem
#
# Da pra escrever isso recursivo, e voce sabe fazer. Mas no beecrowd o n
# vai a 10 mil, e o Python desiste quando passam de mil chamadas
# empilhadas (RecursionError). Entao faca como a conferencia acima, de
# baixo pra cima, com um for:
#
#     def sobrevivente_rapido(pessoas, pulo):
#         posicao = 0                                    # J(1)
#         for tamanho_da_roda in range(2, pessoas + 1):
#             posicao = (posicao + pulo) % tamanho_da_roda
#         return posicao + 1                             # posicao comeca em 0, pessoa em 1
#
# Tempo linear e memoria constante - o que o LeetCode pede. As 30 rodas mais
# pesadas do beecrowd levam, juntas, uns 0,01 segundo.
#
# COMO SUBMETER
#
# O LeetCode pede um METODO dentro de uma class Solution. Cole as suas
# funcoes ACIMA da classe e chame elas de dentro do metodo - o nome do
# metodo eh o que o juiz mandar:
#
#     class Solution:
#         def findTheWinner(self, n, k):
#             return sobrevivente(n, k)
#
# Pode ignorar o self. E cole junto tudo o que a sua funcao usa: o
# sobrevivente chama o vira_n_sai_1, que chama o vira_n, e assim por
# diante.
#
# O beecrowd nao chama funcao nenhuma: ele manda o texto da entrada, voce
# le com input() e escreve a resposta com print(), no formato que o
# enunciado pede.
