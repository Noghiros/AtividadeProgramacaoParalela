"""
Atividade de Código Paralelo
Disciplina: Sistemas Distribuídos
Autor: Stefano Calheiros Stringhini
Matrícula: 2312123

Descrição:
Exercício do livro Fundamentos de Sistemas Operacionais de A. Silberschatz, P. Galvin, G. Gagne página 110.

Um quebra-cabeça Sudoku usa um grid de 9x9 em que cada coluna e cada linha, 
assim como cada um dos nove subgrids 3x3 devem conter todos os dígitos 1...9. 
Esse exercício consiste na elaboração de uma aplicação com múltiplos threads que determine se a solução para um quebra-cabeça Sudoku é válida.
A estratégia sugerida é criar threads em Java/Python que verifiquem os critérios a seguir:
- Um thread para verificar se cada coluna contém os dígitos de 1 a 9
- Um thread para verifica se cada linha contém os dígitos de 1 a 9
- Nove threads para verificar se cada um dos subgrids 3x3 contém os dígitos de 1 a 9
Isso resultaria em um total de onze threads separados para a validação de um quebra-cabeça Sudoku. 
No entanto, você é incentivado a criar ainda mais threads para o exercício. 
Por exemplo, pode-se criar nove threads separados e fazer cada um verificar uma coluna.
"""

import threading

# MATRIZ DO SUDOKU 
sudoku = [
    [2, 3, 7, 8, 4, 1, 5, 6, 9],
    [1, 8, 6, 7, 9, 5, 2, 4, 3],
    [5, 9, 4, 3, 2, 6, 7, 1, 8],
    [3, 1, 5, 6, 7, 4, 8, 9, 2],
    [4, 6, 9, 5, 8, 2, 1, 3, 7],
    [7, 2, 8, 1, 3, 9, 4, 5, 6],
    [6, 4, 2, 9, 1, 8, 3, 7, 5],
    [8, 5, 3, 4, 6, 7, 9, 2, 1],
    [9, 7, 1, 2, 5, 3, 6, 8, 4]
]

# Lista para armazenar o resultado de cada verificação
# resultados[0] -> linhas
# resultados[1] -> colunas
# resultados[2..10] -> subgrades
resultados = [True] * 11


def verificar_linhas():
    print("Thread Linhas iniciada...")
    for i, linha in enumerate(sudoku):
        if sorted(linha) != list(range(1, 10)):
            print(f"Erro na linha: {i+1}")
            resultados[0] = False
            return
    print("Linhas verificadas com sucesso!")


def verificar_colunas():
    print("Thread Colunas iniciada...")
    for c in range(9):
        coluna = [sudoku[l][c] for l in range(9)]
        if sorted(coluna) != list(range(1, 10)):
            print(f"Erro na coluna: {c+1}")
            resultados[1] = False
            return
    print("Colunas verificadas com sucesso!")


def verificar_subgrade(indice, linha_inicial, coluna_inicial):
    print(f"Thread Subgrade ({linha_inicial},{coluna_inicial}) iniciada...")
    numeros = []
    for i in range(3):
        for j in range(3):
            numeros.append(sudoku[linha_inicial + i][coluna_inicial + j])
    if sorted(numeros) != list(range(1, 10)):
        print(f"Erro na subgrade iniciando em ({linha_inicial}, {coluna_inicial})")
        resultados[indice] = False
        return
    print(f"Subgrade iniciando em ({linha_inicial},{coluna_inicial}) verificada!")


threads = []
threads.append(threading.Thread(target=verificar_linhas))
threads.append(threading.Thread(target=verificar_colunas))

indice = 2
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        t = threading.Thread(target=verificar_subgrade, args=(indice, i, j))
        threads.append(t)
        indice += 1


print("Iniciando verificação do Sudoku...\n")
for t in threads:
    t.start()
for t in threads:
    t.join()


print("RESULTADO FINAL:")
if all(resultados):
    print("Sudoku VÁLIDO")
else:
    print("Sudoku INVÁLIDO")

