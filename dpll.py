# TRABALHO FINAL - LÓGICA PARA COMPUTAÇÃO - 2023.1 - 13:30
# JOAO ICARO MOREIRA, CARLOS GABRIEL LEITE, SIDEVALDO VINICIUS

import solver
import time

starting_time = time.time()

N = 4
counter = 1
clauses = []
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
    clauses.append(line)

# agora, iremos dicionar as clauses para garantir que cada coluna tenha no máximo uma rainha

for j in range(1, N+1):
    for i in range(1, N+1):
        other_indexes = list(range(1, N+1))
        other_indexes.remove(i)
        for other in other_indexes:
            clause = [-mapping_to_int[f"Q_{i}_{j}"], -
                      mapping_to_int[f"Q_{other}_{j}"]]
            solver.add_clause(clause)
            clauses.append(clause)

# vamos definir diagonais primarias com no maximo 1 rainha

for diff in range(2 - N, N - 1):
    a = [[i, j] for i in range(1, N+1) for j in range(1, N+1) if i-j == diff]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            clause = [-mapping_to_int[f"Q_{a[i][0]}_{a[i][1]}"], -
                      mapping_to_int[f"Q_{a[j][0]}_{a[j][1]}"]]
            solver.add_clause(clause)
            clauses.append(clause)

# diagonais secundarias com no maximo 1 rainha

for diff in range(3, N + N):
    a = [[i, j] for i in range(1, N+1) for j in range(1, N+1) if i+j == diff]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            clause = [-mapping_to_int[f"Q_{a[i][0]}_{a[i][1]}"], -
                      mapping_to_int[f"Q_{a[j][0]}_{a[j][1]}"]]
            solver.add_clause(clause)
            clauses.append(clause)


def print_board(model):
    count = 0
    board = []

    for _ in range(N):
        row = []
        for _ in range(N):
            row.append('0')
        board.append(row)

    for i in range(1, N+1):
        for j in range(1, N+1):
            if mapping_to_int[f"Q_{i}_{j}"] in model:
                board[i-1][j-1] = '1'
                count += 1
    for row in board:
        print(' '.join(row))

    return count, board

if solver.solve():

    print('\nInformações a respeito do DPLL')
    print('\nclauses Geradas:',clauses)
    print('\nModelo Gerado:', solver.get_model(), '\n')

    model = solver.get_model() #gerar o modelo

    print('Informações Sobre o Problema:\n')
    print(f'board: {N}x{N}\n')

    rainhas, board = print_board(model) #gerar o numero de rainhas e abstrair o board
    print(f'\nQuantidade de Rainhas: {rainhas}')
    
    ending_time = time.time()
    print(f"Tempo de Execução: {ending_time - starting_time} segundos")

    arq = open('entrada.txt', 'w')
    arq.writelines(f"{rainhas}")
    for row in board:
        arq.writelines(f"\n{' '.join(row)}")
else:
    print("Sem solução")
