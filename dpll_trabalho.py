from solver import Solver

"""PRIMEIRO TESTE DO TRABALHO, RECEBER O ARQUIVO ENTRADA.TXT E VERIFICAR
SATISFAZIBILIDADE, BASTA EXECUTAR O ARQUIVO 'python3 dpll_trabalho.py' NO
MESMO DIRETORIO ONDE ESTÁ O ARQUIVO 'exemplo.txt'"""

#gerar instancia do nosso Solver
solver = Solver()

#verificar se o arquivo está de maneira conforme
with open('exemplo.txt', 'r') as arquivo:

    num_clausulas_entrada, num_atomos_entrada = map(int, arquivo.readline().split())
    print(f'numero de atomos: {num_atomos_entrada}, numero de clausulas: {num_clausulas_entrada}\n')

    clausulas = []

    for linha in arquivo:
        clausula = list(map(int, linha.split()))

        if len(clausula) != num_atomos_entrada:
            print('Número de átomos incosistentes com a entrada!')
            exit()

        clausulas.append(clausula)

if len(clausulas) != num_clausulas_entrada:
    print('Número de clausulas incosistentes com a entrada!')
    exit()

try:
    #adicionar cada clausula do arquivo
    for cada_clausula in clausulas:
        solver.add_clause(cada_clausula)

    #gerar modelo
    model = solver.get_model()
    if model:
        print(model)

except Exception as Error:
    print("Erro!")