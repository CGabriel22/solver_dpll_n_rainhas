# Solver DPLL e problema das N rainhas
Problema das N rainhas resolvido com um algoritmo que utiliza um solver baseado no algoritmo Davis-Putnam-Logemann-Loveland (DPLL) desenvolvido por nós.

O projeto foi desenvolvido para um trabalho da cadeira de Lógica da computação.

---

## Índice
1. [Pré-requisitos](#prerequisites)
2. [Construindo o projeto](#building)
3. [Executando o projeto](#running)
4. [Testando o resultado](#testing)
5. [Sobre o problema das N Rainhas](#n-queen)
6. [Sobre o algoritmo DPLL](#dpll)
7. [Sobre o Solver DPLL](#solver)
8. [Sobre o a utilização do Solver DPLL no problema das N Rainhas](#dpll-in-n-queen)
9. [Licença](#license)
10. [Autores](#authors)

## Pré-requisitos <a name="prerequisites"></a>
- python 3.11 ou superior [Download oficial](https://www.python.org)
- Testado no Windows 10 e 11

## Construindo o projeto <a name="building"></a>
Clonando o repositório
```bash
$ git clone https://github.com/CGabriel22/solver_dpll_n_rainhas
$ cd solver_dpll_n_rainhas
```

## Executando o projeto <a name="running"></a>
Execute o arquivo dpll.py com o python
```bash
$ python3 dpll.py
```
Será gerado um arquivo com o resultado do programa. 

No terminal também será apresentado: 
- as clausulas geradas pelo algoritmo das N Rainhas; 
- o modelo resultado gerado pelo solver que satisfaz as clausulas; 
- e por fim o resultado visual do tabuleiro. 

Se necessário, modifique a variável N na linha 15 para testar diferentes tamanhos de tabuleiro:
```python
N = 4
```

## Testando o resultado <a name="testing"></a>
Para testar o resultado foi disponibilizado pelo professor um verificador "nqueen_checker.py" para testar se o resultado atende aos requisitos do problema das N Rainhas.

Ao [executar o programa](#running) é gerado um arquivo "entrada.txt" semelhante a este:
```txt
4
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
```
Use-o para o teste da seguinte forma:
```bash
$ python3 nqueen_checker.py < entrada.txt
```
O verificador retornará no terminal se o resultado é válido ou não.
