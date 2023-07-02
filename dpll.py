# TRABALHO FINAL - LÓGICA PARA COMPUTAÇÃO - 2023.1 - 13:30
# JOAO ICARO MOREIRA, CARLOS GABRIEL LEITE, SIDEVALDO VINICIUS

import solver
import time

tempo_inicial = time.time()

N = 4
counter = 1
clausulas = []
mapping_to_int = {}
mapping_to_int_inv = {}
positions = [[i, j] for i in range(1, N+1) for j in range(1, N+1)]  # [1, 1] até [N, N]

for position in positions:
    key = f"Q_{position[0]}_{position[1]}"
    mapping_to_int[key] = counter
    mapping_to_int_inv[counter] = key #apenas para exemplificação
    counter += 1

for i in range(1, N+1):
    line = []
    for j in range(1, N+1):
        line.append(mapping_to_int[f"Q_{i}_{j}"])
    solver.add_clause(line)
    clausulas.append(line)

# agora, iremos dicionar as clausulas para garantir que cada coluna tenha no máximo uma rainha

for j in range(1, N+1):
    for i in range(1, N+1):
        other_indexes = list(range(1, N+1))
        other_indexes.remove(i)
        for other in other_indexes:
            clause = [-mapping_to_int[f"Q_{i}_{j}"], -
                      mapping_to_int[f"Q_{other}_{j}"]]
            solver.add_clause(clause)
            clausulas.append(clause)

# vamos definir diagonais primarias com no maximo 1 rainha

for diff in range(2 - N, N - 1):
    a = [[i, j] for i in range(1, N+1) for j in range(1, N+1) if i-j == diff]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            clause = [-mapping_to_int[f"Q_{a[i][0]}_{a[i][1]}"], -
                      mapping_to_int[f"Q_{a[j][0]}_{a[j][1]}"]]
            solver.add_clause(clause)
            clausulas.append(clause)

# diagonais secundarias com no maximo 1 rainha

for diff in range(3, N + N):
    a = [[i, j] for i in range(1, N+1) for j in range(1, N+1) if i+j == diff]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            clause = [-mapping_to_int[f"Q_{a[i][0]}_{a[i][1]}"], -
                      mapping_to_int[f"Q_{a[j][0]}_{a[j][1]}"]]
            solver.add_clause(clause)
            clausulas.append(clause)


def imprimir_tabuleiro(model):
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

if solver.solve():

    print('\nInformações a respeito do DPLL')
    print('\nClausulas Geradas:',clausulas)
    print('\nModelo Gerado:', solver.get_model(), '\n')

    model = solver.get_model() #gerar o modelo

    print('Informações Sobre o Problema:\n')
    print(f'Tabuleiro: {N}x{N}\n')

    rainhas, tabuleiro = imprimir_tabuleiro(model) #gerar o numero de rainhas e abstrair o tabuleiro
    print(f'\nQuantidade de Rainhas: {rainhas}')
    
    tempo_final = time.time()
    print(f"Tempo de Execução: {tempo_final - tempo_inicial} segundos")

    arq = open('entrada.txt', 'w')
    arq.writelines(f"{rainhas}")
    for linha in tabuleiro:
        arq.writelines(f"\n{' '.join(linha)}")
else:
    print("Sem solução")
