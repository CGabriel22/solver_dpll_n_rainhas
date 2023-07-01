n = int(input().strip())
entry = [list(map(int, input().strip().split())) for _ in range(n)]  

row_checked = [sum(row) for row in entry] == [1]*n
col_checked = [sum(col) for col in list(zip(*entry))] == [1]*n
primary_diag_check = max([sum([entry[i][j] for i in range(n) for j in range(n) if i+j == diag]) for diag in range(2*n-1)]) <=1
secondary_diag_check = max([sum([entry[i][j] for i in range(n) for j in range(n) if i-j == diag]) for diag in range(-n+1,n)]) <=1

valid_solution = row_checked and col_checked and primary_diag_check and secondary_diag_check
print("SOLUÇÃO VALIDA") if valid_solution else print("SOLUÇÃO INVALIDA") 