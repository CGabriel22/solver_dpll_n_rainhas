from solver import Solver

solver = Solver()

while True:
    print("1 - Testar sem Clausulas")
    print("2 - Testar clausulas Unsat")
    print("3 - Testar Sat")
    escolha = int(input("Opção: \n"))

    if escolha == 1:
        model = solver.get_model()
        print(model)
        exit()
    elif escolha == 2:
        solver.add_clause([1,2])
        solver.add_clause([-1,2])
        solver.add_clause([1,-2])
        model = solver.get_model()
        print(model)
        exit()
    elif escolha == 3:
        clausulas = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [-1, -5], [-1, -9], [-1, -13], [-5, -1], [-5, -9], [-5, -13], [-9, -1], [-9, -5], [-9, -13], [-13, -1], [-13, -5], [-13, -9], [-2, -6], [-2, -10], [-2, -14], [-6, -2], [-6, -10], [-6, -14], [-10, -2], [-10, -6], [-10, -14], [-14, -2], [-14, -6], [-14, -10], [-3, -7], [-3, -11], [-3, -15], [-7, -3], [-7, -11], [-7, -15], [-11, -3], [-11, -7], [-11, -15], [-15, -3], [-15, -7], [-15, -11], [-4, -8], [-4, -12], [-4, -16], [-8, -4], [-8, -12], [-8, -16], [-12, -4], [-12, -8], [-12, -16], [-16, -4], [-16, -8], [-16, -12], [-3, -8], [-2, -7], [-2, -12], [-7, -12], [-1, -6], [-1, -11], [-1, -16], [-6, -11], [-6, -16], [-11, -16], [-5, -10], [-5, -15], [-10, -15], [-9, -14], [-2, -5], [-3, -6], [-3, -9], [-6, -9], [-4, -7], [-4, -10], [-4, -13], [-7, -10], [-7, -13], [-10, -13], [-8, -11], [-8, -14], [-11, -14], [-12, -15]]
        for clausula in clausulas:
            solver.add_clause(clausula)
        model = solver.get_model()
        print(model)
        exit()
    else:
        print("Escolha uma opção válida")