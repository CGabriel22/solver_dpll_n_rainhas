class Solver:
    def __init__(self):
        self.solution, self.clauses = [], []

    def add_clause(self, clause):
        self.clauses.append(clause)

    def simplify(self, formula):
        while True:
            unit_clause = next((clause[0] for clause in formula if len(clause) == 1), None)
            if unit_clause is None:
                break
            self.solution.append(unit_clause)
            formula = [c for c in formula if unit_clause not in c]
            formula = [[l for l in c if l != -unit_clause] for c in formula]
        return formula

    def dpll(self, formula):
        simplified_formula = self.simplify(formula)

        if not simplified_formula:
            return True
        if [] in simplified_formula:
            return False

        literal = simplified_formula[0][0]

        if self.dpll(simplified_formula + [[literal]]):
            return True
        if self.dpll(simplified_formula + [[-literal]]):
            return True

        return False

    @staticmethod
    def find_literals(lst):
        if isinstance(lst[0], int):
            positive_list = [abs(number) for number in lst]
        else:
            flattened_list = [element for sublist in lst for element in sublist]
            positive_list = [abs(number) for number in flattened_list]

        no_duplicates_list = list(set(positive_list))
        return no_duplicates_list

    @staticmethod
    def check_missing_values(l1, l2):
        missing_values = []

        for value in l1:
            if value not in l2:
                missing_values.append(value)

        return missing_values

    def get_model(self):
        result = self.dpll(self.clauses)
        if not result:
            return "Insatisfazível!"
        if self.clauses == []:
            return "Informe as clausulas!"
        
        literals = self.find_literals(self.clauses)
        solution_literals = self.find_literals(self.solution)
        missing_values = self.check_missing_values(literals, solution_literals)

        self.solution += missing_values
        sorted_list = sorted(self.solution, key=abs)

        last_occurrence = {}

        for i in sorted_list:
            last_occurrence[abs(i)] = i
            new_list = [last_occurrence[j]
                        for j in range(1, len(last_occurrence) + 1)]

        return new_list