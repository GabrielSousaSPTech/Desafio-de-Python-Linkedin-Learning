from itertools import product

class Sudoku:
    def resolverSudoku(self, sudoku):
        for (linha, coluna) in product(range(0, 9), repeat=2):
            if sudoku[linha][coluna] == 0:  # Encontrar uma célula vazia
                for num in range(1, 10):  # Tentar números de 1 a 9
                    permitido = True
                    for i in range(0, 9):
                        if num in (sudoku[i][coluna], sudoku[linha][i]):
                            permitido = False
                            break
                    for (i, j) in product(range(0,3), repeat=2):
                        if sudoku[linha - linha%3 +1][coluna - coluna %3 +j] == num:
                            permitido = False
                            break
                    if permitido:
                        sudoku[linha][coluna] = num
                        if tentativa := self.resolverSudoku(sudoku):
                            return tentativa
                        sudoku[linha][coluna] = 0
                return False
        return sudoku

s = Sudoku()
sudoku = [
    [5, 3, 0, 7, 0, 0, 0, 0, 0],
    [6, 0, 1, 9, 5, 0, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 7]
]

resultado = s.resolverSudoku(sudoku)
if resultado:
    for linha in resultado:
        print(linha)
else:
    print("Sem solução")