#from gauss_jacobi import metodo_jacobi
from gauss_seidel import metodo_seidel

tol = float(input(f'Digite o valor da tolerância (ex: 1e-6): '))
max_iter = int(input('Digite o máximo de iterações: '))
num_linhas, num_colunas = map(int, input(f'Digite o formato da matriz separados por x (ex: 3x3): ').split('x'))


A = []
for i in range(num_linhas):
    linha1 = input(f'Digite os {num_colunas} elementos da linha atual. Após isso, aperte Enter: ').split()
    linha = [float(x) for x in linha1]
    A.append(linha)
    if len(linha1) != num_colunas:
        exit('O número de elementos digitados não confere com a quantidade informada de colunas.')

print()

print('Aqui está sua matriz:')
for l in range(len(A)):
    for c in range(len(A[0])):
        print(A[l][c], end=' ')
    print()

print()

b = [int(i) for i in input("Digite os valores de b separados por espaço: ").split()]

print()
'''def metodo_jacobi(A, b, tol, max_iter):
    n = len(A)
    x = [0] * n  # Inicializa o vetor de soluções com zeros

    for _ in range(max_iter):
        x_old = x.copy()  # Cria uma cópia do vetor de soluções anterior

        for i in range(n):
            s = sum(A[i][j] * x_old[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]  # Atualiza o valor de x[i] usando os valores antigos

        # Verifica a convergência
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            return x

    print("O método de Gauss-Jacobi não convergiu após", max_iter, "iterações.")
    return None'''

'''def metodo_seidel(A, b, tol, max_iter):
    n = len(A)
    x = [0] * n  # Inicializa o vetor de soluções com zeros

    for _ in range(max_iter):
        x_old = x.copy()  # Cria uma cópia do vetor de soluções anterior

        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]  # Atualiza o valor de x[i]

        # Verifica a convergência
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            return x

    print("O método de Gauss-Seidel não convergiu após", max_iter, "iterações.")
    return None
'''

def determinante(matrix):
    num_lin, num_col = len(matrix), len(matrix[0])

    if num_lin != num_col:
        raise ValueError("A matriz não é quadrada. O determinante não pode ser calculado.")

    if num_lin == 1:
        return matrix[0][0]

    if num_lin == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for j in range(num_col):
        cofactor = (-1) ** j * matrix[0][j]
        submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += cofactor * determinante(submatrix)

    return det

if determinante(A) != 0:
    print(f'O determinante da matriz é diferente de 0, portanto, ela possui solução única.')
else:
    print(f'O determinante da matriz é igual a 0, portanto não possui solução única.')

print()

def verifica_convergencia_sassenfeld(matriz):
    n = len(matriz)

    # Cálculo dos fatores de ponderação
    lista = []
    for i in range(n):
        soma_abs = sum([abs(matriz[i][j]) for j in range(n) if j != i])  #comprehension: [append for >cond< if >cond<]
        elemento_diagonal = abs(matriz[i][i])
        fator_ponderacao = soma_abs / elemento_diagonal
        lista.append(fator_ponderacao)

    # Verificação da convergência
    maior_fator_ponderacao = max(lista)
    if maior_fator_ponderacao < 1:
        return True
    else:
        return False


if verifica_convergencia_sassenfeld(A):
    print('Os valores das variáveis através dos métodos de Gauss-Seidel e Gauss-Jacobi convergem pelo método de Sassenfeld.')
else:
    print('Os valores das variáveis através dos métodos de Gauss-Seidel e Gauss-Jacobi não convergem pelo método de Sassenfeld.')

print()
solucao_jacobi = metodo_jacobi(A, b, tol, max_iter)
solucao_seidel = metodo_seidel(A, b, tol, max_iter)


lista_x = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
print(f'Os valores aproximados calculados pelo método de Gauss-Seidel das variáveis do sistema linear apresentado são: ')
for xn in range(num_colunas):
    print(f'{lista_x[xn]}:{solucao_seidel[xn]}')

print()

print(f'Os valores aproximados calculados pelo método de Gauss-Jacobi das variáveis do sistema linear apresentado são: ')
for xm in range(num_colunas):
    print(f'{lista_x[xm]}:{solucao_jacobi[xm]}')

