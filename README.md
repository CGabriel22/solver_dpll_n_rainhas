# Solver DPLL e problema das N rainhas
Problema das N rainhas resolvido com um algoritmo que utiliza um solver baseado no algoritmo Davis-Putnam-Logemann-Loveland (DPLL) desenvolvido por nós.

O projeto foi desenvolvido para um trabalho da cadeira de Lógica da computação.

---

## Índice
1. [Pré-requisitos](#prerequisites)
2. [Construindo o projeto](#building)
3. [Sobre o problema das N Rainhas](#n-queen)
4. [Sobre o algoritmo DPLL](#dpll)
5. [Sobre o Solver DPLL](#solver)
6. [Resolução do Problema de Satisfazibilidade com Entrada](#sat-problem)
7. [Resolução do Problema das N-Rainhas](#queen-problem)
8. [Testando o resultado](#testing)
9. [To-do](#to-do)
10. [Autores](#authors)

## Pré-requisitos <a name="prerequisites"></a>
- python 3.11 ou superior [Download oficial](https://www.python.org)
- Testado no Windows 10, 11 e Debian

## Construindo o projeto <a name="building"></a>
Clonando o repositório
```bash
$ git clone https://github.com/CGabriel22/solver_dpll_n_rainhas
$ cd solver_dpll_n_rainhas
```

## Sobre o problema das N-Rainhas <a name="n-queen"></a>
O problema das N-Rainhas consiste em elaborar uma solução para que, em um tabuleiro NxN (matriz quadrada) possamos posicionar, sem que se ataquem, a maior quantidade de rainhas possíveis. É um problema clássico e iremos utilizar nosso Solver para resolvê-lo.

<div style="display: flex; gap: 8px">
  <img src="./src/img/nqueens.png" width="128" height="128"/>
</div>

## Sobre o algoritmo DPLL <a name="dpll"></a>
O algoritmo DPLL (Davis-Putnam-Logemann-Loveland) é um algoritmo usado para resolver problemas de satisfatibilidade booleana (SAT), que envolvem determinar se uma fórmula booleana pode ser satisfeita por uma atribuição de valores verdadeiro/falso às suas variáveis. O DPLL é um dos algoritmos mais eficientes para resolver problemas SAT e é amplamente utilizado em verificação de hardware, inteligência artificial, otimização e outros campos.

O funcionamento do algoritmo DPLL é baseado em uma estratégia de busca em profundidade recursiva. Ele trabalha em duas fases principais: a fase de simplificação e a fase de busca.

Na fase de simplificação, o algoritmo tenta simplificar a fórmula booleana de entrada aplicando várias regras de inferência. Essas regras incluem a eliminação de cláusulas tautológicas (cláusulas que contêm uma variável e sua negação), a eliminação de cláusulas unitárias (cláusulas que contêm apenas uma variável) e a aplicação de regras de propagação de literais. Essas simplificações reduzem o tamanho do problema e ajudam a torná-lo mais fácil de resolver.

Na fase de busca, o algoritmo faz uma escolha não determinística de uma variável para atribuir um valor verdadeiro ou falso. Em seguida, ele recursivamente aplica a fase de simplificação atualizada à fórmula resultante. Se a fórmula se tornar insatisfatível (ou seja, não há mais atribuições que satisfaçam a fórmula), o algoritmo faz um retorno recursivo e faz uma escolha diferente. Se a fórmula se tornar uma cláusula vazia (ou seja, todas as variáveis foram atribuídas), o algoritmo encontrou uma atribuição satisfatível.

O algoritmo DPLL continua esse processo de busca e simplificação até que uma atribuição satisfatível seja encontrada ou todas as possibilidades tenham sido exploradas. Ele também pode usar heurísticas para guiar a escolha de variáveis, como a heurística de escolha de variável mais frequente ou a heurística de escolha de variável mais pura.

## Sobre o solver DPLL <a name="solver"></a>

<h3>Uso:</h3>

- Instancie o solver
- Adicione as cláusulas à serem satisfeitas usando o método 
- Cada cláusula é representada como uma lista de literais, onde cada literal é um número inteiro.

```python
solver = Solver() #instanciando o solver

solver.add_clause([1, 2, -3]) #adicionando as cláusulas
solver.add_clause([-1, 3])
solver.add_clause([-2, 4])

model = solver.get_model() #gerando modelo

print("Modelo:", model)
```

<h3>Métodos:</h3>

```python
add_clause(clause)
```
Este método adiciona uma cláusula ao solver. A cláusula é passada como uma lista de literais, onde cada literal é um número inteiro.

```python
get_model()
```

Este método retorna um modelo satisfatível para as cláusulas adicionadas anteriormente, se existir. O modelo é retornado como uma lista de atribuições de valores verdadeiro/falso para as variáveis.

Outros métodos

- simplify(formula): Simplifica a fórmula SAT através da aplicação de regras de inferência.
- dpll(formula): Algoritmo DPLL que resolve o problema SAT.
- find_literals(lst): Encontra os literais presentes na lista de cláusulas.
- check_missing_values(l1, l2): Verifica quais valores estão faltando em uma lista em relação à outra.
- get_model(): Obtém o modelo satisfatível para as cláusulas adicionadas.

Observações

- Se o método get_model() retornar "Insatisfazível!", significa que as cláusulas não têm uma atribuição que satisfaça todas elas.
- Se o método get_model() retornar "Informe as clausulas!", significa que nenhuma cláusula foi adicionada ao solver.
    
## Resolução do Problema de Satisfazibilidade com Entrada<a name="sat-problem"></a>

Podemos receber um arquivo de entrada com as fórmulas, através de um arquivo 'exemplo.txt' no seguinte formato: 

```txt
4 3
1 -2 3
-1 2 -3
-1 -2 3
1 2 3
```

- 4 representa o numero de clausulas; 
- 3 representa o número de átomos;
- As linhas abaixo representam as fórmulas;

Para executar, basta rodar o arquivo dpll_trabalho.py que será gerado um modelo caso satisfazível.

```bash
$ python3 dpll_trabalho.py
```

Caso os dados das clausulas e/ou átomos estejam inconsistentes, o mesmo será alertado através do terminal.

## Resolução do Problema das N-Rainhas<a name="queen-problem"></a>

Para o problema das N-Rainhas, não iremos adicionar manualmente clausulas, no arquivo n_queens.py existem diversas iterações onde nessas, adicionamos as clausulas automaticamente baseadas no problema das N-Rainhas, a seguir estão detalhes de como executar esse arquivo.

Execute o arquivo n_queens.py com o python
```bash
$ python3 n_queens.py
```
Será gerado um arquivo com o resultado do programa. 

No terminal também será apresentado: 
- as clausulas geradas pelo algoritmo das N Rainhas; 
- o modelo resultado gerado pelo solver que satisfaz as clausulas; 
- resultado visual do tabuleiro. 

Se necessário, modifique a variável N na linha 15 para testar diferentes tamanhos de tabuleiro:
```python
N = 4
```

## Testando o resultado <a name="testing"></a>
Para testar o resultado foi disponibilizado um verificador "nqueen_checker.py" para testar se o resultado atende aos requisitos do problema das N Rainhas.

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

## TO-DO <a name="to-do"></a>

- [ ] Criar Licença e Seção Licença
- [ ] Transformar em Pacote (definir framework [npm provavelmente])
- [ ] Release Final

## Autores <a name="authors"></a>
<div style="display: flex; gap: 8px">

  <img src="./src/collaborators/gabriel.png" width="128" height="128"/>
  <img src="./src/collaborators/icaro.png" width="128" height="128"/>
  <img src="./src/collaborators/vini.png" width="128" height="128"/>
  
</div>
