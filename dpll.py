# TRABALHO PONTO EXTRA - LÓGICA 13:30
# JOAO ICARO MOREIRA, CARLOS GABRIEL LEITE, SIDEVALDO VINICIUS

import solver

# neste primeiro trecho, definimos o tamanho do tabuleiro pela variavel N (nxn), além de criarmos uma variavel
# contadora para atribuir valores para cada posicao no tabuleiro e dois dicionarios para mapear as posições
# para simbolos proposicionais, uma vez que por lista isso é impossivel, considerando que a posição é
# indicada por números, e não caracteres.

# Por fim, criamos uma lista que define todas as posições no tabuleiro, o fato de ser range 1 até n + 1 é para
# evitarmos o uso dos valores i e j para 0, ou seja, começamos com i e j = 1 e terminando um numero após o fim anteriromente
# determinado, não alterando em nada o funcionamento do código

N = 4
counter = 1
clausulas = []
mapping_to_int = {}
mapping_to_int_inv = {}
positions = [[i, j] for i in range(1, N+1)
             for j in range(1, N+1)]  # [1, 1] até [N, N]
'''print('posições do tabuleiro:', positions)'''

# agora vamos atribuir um valor inteiro a cada posição no tabuleiro usando os dicionários criados anteriormente
# iremos passar por cada posicao, i sendo a linha e j sendo a coluna, iremos criar uma key de dicionarios, representada
# pelo formato "Q_linha_coluna" e vamos adicionar o nosso contador (começando em 1) nessa posição, dentro do dicionario
# mapping_to_int, ao mesmo tempo, iremos adicionar um elemento no dificionario que é seu inverso, ou seja.

# enquanto temos um dicionario que a proposição indica a posição do número contador,
# também temos um dicionário que faz o contrário, em que o número contador indica a posição da proposição

# devo acrescentar que o uso do dict inv é opcional, não sendo utilizado no código em questão

for position in positions:
    key = f"Q_{position[0]}_{position[1]}"
    mapping_to_int[key] = counter
    mapping_to_int_inv[counter] = key
    counter += 1

# visualizar dict mapping_to_int
'''for cada_elemento in mapping_to_int:
   print(f'posição {cada_elemento}: ', mapping_to_int[cada_elemento])'''

# visualizar dict mapping_to_int_inv
'''for cada_elemento in mapping_to_int_inv:
   print(cada_elemento, mapping_to_int_inv[cada_elemento])'''

# logo após, iremos fazer cada linha possuir no maximou ma rainha, para isso, iremos simular o tabuleiro
# criando um laço para as linhas e um laço que passa de elemento em elemento da linha (cada coluna),
# ou seja, um n = 4, irá passar por cada uma das 4 linhas, e em cada uma delas, criar 4 valores (coluna).

# nesse laço de cada coluna, iremos adicionar o numero que corresponde a posição proposicional indicada na lista acima, por exemplo:

# se Q_1_1 guarda o numero 10, nosso tabuleiro inicialmente será representado por:
''' 10 0 0 0 -> line.append(mapping_to_int[f"Q_{i}_{j}"]) '''

# por fim, teriamos por exemplo:

'''
  10 0 0 0 
  1 1 1 1
  2 2 2 2
  3 3 3 3
'''

# resumindo, cada elemento do tabuleiro agora será o inteiro que está sendo armazenado dentro de cada proposição
# porém, não iremos adicionar cada linha realmente a um tabuleiro, iremos adicionar cada linha em uma lista que contém todas
# as clausulas, sendo assim, um exemplo de como a lista de clausulas final poderia estar:

''' [ [10, 0 , 0 , 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3] ] '''

for i in range(1, N+1):
    line = []
    for j in range(1, N+1):
        line.append(mapping_to_int[f"Q_{i}_{j}"])
    solver.add_clause(line)
    clausulas.append(line)
# agora, iremos dicionar as clausulas para garantir que cada coluna tenha no máximo uma rainha
# começamos da mesma maneira, simulando as linhas e colunas do tabuleiro, mas dessa vez, iremos
# criar uma lista que contém todos os elementos positivos, ou seja:

# a lista contem, inicialmente: '''[1, 2, 3 ,4]'''

# iremos remover o valro correspondente ao i cada vez que criamos essa lista, sabemos que i vai de 1 a 4 (dito pelo range),

# entao, a lista irá começar como [1, 2, 3, 4] e como estamos na primeira repeticao, ficará [2, 3, 4], pois removemos o i = 1
# depois ela ficará [1, 3, 4], removemos o i = 2, depois [1, 2, 4], depois [1, 2, 3] e isso se repetirá mais 3 vezes

# por fim, toda vez que sobrarem apenas os elementos "desejaveis", iremos percorrer cada um dos numeros, criando uma variavel
# temporaria para armazenar cada um deles, chamada de 'other' ou 'outro', ela irá incrementar 4 vezes para o i incrementar 1 vez,
# tendo em consideração que um laço está dentro do outro, entao quando i = 1 e other = 4,
# iremos criar uma clausula pelo [ dicionario mapping_to_int["Q_1_1"], mapping_to_int['Q_4_1'] ], indicando
# que duas rainhas nao podem ocupar essas posicoes simultaneamente, para isso, o numero dentro do dicionario será passado como negativo

# resultado exemplo: [[-1, -4]] (nao necessariamente 1 e 4 sao os valores da posicao Q_i_j e q_other_j)

for j in range(1, N+1):
    for i in range(1, N+1):
        other_indexes = list(range(1, N+1))
        #print(f'\noutros indices antes de remover i = {i}:\n', other_indexes)
        other_indexes.remove(i)
        #print('\noutros indices depois:', other_indexes)
        for other in other_indexes:
            clause = [-mapping_to_int[f"Q_{i}_{j}"], -
                      mapping_to_int[f"Q_{other}_{j}"]]
            #print('clausulas: ', clause)
            solver.add_clause(clause)
            clausulas.append(clause)

# vamos definir diagonais primarias com no maximo 1 rainha
# iremos percorrer o tabuleiro 4x4 da seguinte maneira:
# n = 4, posicao inicial do for: -2, posicao final: 3
# iremos criar uma lista com todas as posições da diagonal principal, a verificação nela para sabermos se a
# posição está correta é a diferença das variaveis i e j serem iguais ao valor do diff

# logo após, iremos criar um laço que vai executar o numero de elementos dentro de a, ou seja, se tiverem 4 elementos
# na diagonal principal, iremos percorrer 4x, após isso, cada vez que percorremos isso, iremos percorrer novamente essa quantidade
# de vezes, mas agora irá de um valor específico até esse ultimo elemento 4, iremos sempre começar pelo valor de i acrescentado a 1
# agora, iremos adicionar como clausulas, os numeros representados pela posicao
# 'q_(lista_diagonal[posicao i][elemento 0])_(lista_diagonal[posicao i][elemento 1])

# a = [ [1, 3], [2, 4] ]
# i = 0 e j = 1:
# clausula: [ -3, -8]

# a = [[1, 2], [2, 3], [3, 4]]
# i = 0, j = 1:
# clausula: [-2, -7]

'''
diff = -1
decidimos não declarar diff = -1, embora sempre seja válido, para facilitar o entendimento e explicação da diag. secundária,
porém, é só remover o for externo e identar corretamente, caso queira validar
'''

for diff in range(2 - N, N - 1):
    a = [[i, j] for i in range(1, N+1) for j in range(1, N+1) if i-j == diff]
    #print('diagonais principais: ', a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            #print('valores de i e j: ', i, j)
            clause = [-mapping_to_int[f"Q_{a[i][0]}_{a[i][1]}"], -
                      mapping_to_int[f"Q_{a[j][0]}_{a[j][1]}"]]
            #print('clausula:', clause)
            solver.add_clause(clause)
            clausulas.append(clause)

# iremos fazer a exata mesma coisa para a diagonal secundária, so que agora o diff irá começar pelo numero 3,
# e irá até o numero 8, ou seja: 3,4,5,6,7 e, agora para sabermos os elementos da diagonal secundária, é quando
# a soma de i e j forem iguais a diff, nao a subtração, a partir daí, todo o processo se repete

'''tentamos encontrar um valor valido para este diff, de -10 até 10 apenas o 5 era mais interessante
porém estava inválido, então decidimos manter a maneira passada'''

# diagonais secundarias com no maximo 1 rainha
for diff in range(3, N + N):
    # print(diff)
    a = [[i, j] for i in range(1, N+1) for j in range(1, N+1) if i+j == diff]
    #print('diagonais secundarias: ', a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            #print('valores de i e j: ', i, j)
            clause = [-mapping_to_int[f"Q_{a[i][0]}_{a[i][1]}"], -
                      mapping_to_int[f"Q_{a[j][0]}_{a[j][1]}"]]
            #print('clausula:', clause)
            solver.add_clause(clause)
            clausulas.append(clause)

# por fim, iremos imprimir o tabuleiro, funciona da seguinte maneira:
# [ 1 1 1 1 ]
# [ 1 1 1 1 ]
# [ 1 1 1 1 ]
# [ 1 1 1 1 ]
# se trata de uma matriz, 4 linhas e 4 colunas

# para cada_linha in range(4):
#   crie a lista das linhas
#   para cada 4 elementos da linha,
#     coloque o numero 0 em cada um deles

# por fim, adicione as 4 linhas na lista principal do tabuleiro
# depois, verifique cada posição, verificando se o elemento posição q_i_j do dict
# está presente no nosso modelo (resolução), caso esteja:
# o elemento da posição [i][j] que contem a rainha receberá o elemento 1

# depois, usamos o join, que imprime cada linha do tabuleiro sem o formato delista, aplicando um espaço entre cada numero

# os conhecimentos aplicados nessa e nas demais funções são de: fup - matrizes e algebra linear


def print_board(model):
    contador = 0
    tabuleiro = []

    for i in range(N):
        linha = []
        for j in range(N):
            linha.append('0')
        tabuleiro.append(linha)

    for i in range(1, N+1):
        for j in range(1, N+1):
            if mapping_to_int[f"Q_{i}_{j}"] in model:
                tabuleiro[i-1][j-1] = '1'
                contador += 1
    for linha in tabuleiro:
        print(' '.join(linha))

    return contador, tabuleiro

    # sem join:
    # for linha in tabuleiro:
    # print(linha)


# por fim, se o resultado da função solve for True, iremos imprimir as informações, se não, não há solução
if solver.solve():

    print('clausulas\n\n')
    print(clausulas)

    print('\nResultado: ', solver.get_model(), '\n')

    model = solver.get_model()
    print(f'Tabuleiro: {N}x{N}\n')

    resultado, tabuleiro = print_board(model)
    print(f'\nQuantidade de Rainhas: {resultado}')

    count = 0
    arq = open('entrada.txt', 'w')
    arq.writelines(f"{resultado}")
    for linha in tabuleiro:
        arq.writelines(f"\n{' '.join(linha)}")

else:
    print("Sem solução")
