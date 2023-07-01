solution = []
clausulas = []


def add_clause(clausula):
    clausulas.append(clausula)
    return clausulas


def Simplifica(formula):
    while True:
        clausula_unitaria = None
        for clausula in formula:
            if len(clausula) == 1:
                clausula_unitaria = clausula[0]
                break
        if clausula_unitaria is None:
            break
        # print(clausula_unitaria)
        solution.append(clausula_unitaria)
        # print(formula)
        formula = [c for c in formula if clausula_unitaria not in c]
        # print(formula)
        formula = [[l for l in c if l != -clausula_unitaria] for c in formula]
        # print(formula)
    return formula


def DPLL(formula):
    formula_simplificada = Simplifica(formula)

    if not formula_simplificada:
        return True
    if [] in formula_simplificada:
        return False

    literal = formula_simplificada[0][0]

    if DPLL(formula_simplificada + [[literal]]):
        return True
    if DPLL(formula_simplificada + [[-literal]]):
        return True

    return False


def solve():
    if DPLL(clausulas):
        return True
    else:
        return False


def processar_lista(lista):
    if isinstance(lista[0], int):
        # Se for uma lista de inteiros simples
        lista_positivos = [abs(numero) for numero in lista]
    else:
        # Se for uma lista de listas
        lista_unica = [elemento for sublist in lista for elemento in sublist]
        lista_positivos = [abs(numero) for numero in lista_unica]

    lista_sem_repeticoes = list(set(lista_positivos))
    return lista_sem_repeticoes


def verificar_valores_faltantes(l1, l2):
    valores_faltantes = []

    for valor in l1:
        if valor not in l2:
            valores_faltantes.append(-valor)

    return valores_faltantes


def montar_solution(solution):
    literais = processar_lista(clausulas)
    solutions_literais = processar_lista(solution)
    valores_faltantes = verificar_valores_faltantes(
        literais, solutions_literais)

    # print(solution)
    solution += valores_faltantes
    lista_ordenada = sorted(solution, key=abs)

    # criar lista com as ultimas ocorrencias

    ultima_ocorrencia = {}

    for i in lista_ordenada:
        ultima_ocorrencia[abs(i)] = i
        nova_lista = [ultima_ocorrencia[j]
                      for j in range(1, len(ultima_ocorrencia) + 1)]

    return nova_lista


def get_model():
    return montar_solution(solution)
