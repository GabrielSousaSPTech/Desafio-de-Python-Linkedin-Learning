class Sudoku:
    def resolverSudoku(self, sudoku  = [[]]):

        for indice ,grade in enumerate(sudoku):
            for indiceGrade, subgrade in enumerate(grade):
                for indiceSubgrade, conteudoSubgrade in enumerate(subgrade):
                    num = 1
                    if(conteudoSubgrade ==0 and subgrade == num):
                        conteudoSubgrade = num

                print(subgrade)







s = Sudoku()
s.resolverSudoku([
 [[5, 3, 0],
 [7, 0, 0],
 [0, 0, 0]],
 [[6, 0, 1],
 [9, 5, 0],
 [0, 0, 0]],
 [[0, 9, 8],
 [0, 0, 0],
 [0, 6, 0]],
 [[8, 0, 0],
 [0, 6, 0],
 [0, 0, 3]],
 [[4, 0, 0],
 [8, 0, 3],
 [0, 0, 1]],
 [[7, 0, 0],
 [0, 2, 0],
 [0, 0, 6]],
 [[0, 6, 0],
 [0, 0, 0],
 [2, 8, 0]],
 [[0, 0, 0],
 [4, 1, 9],
 [0, 0, 0]],
 [[0, 0, 0],
 [0, 8, 0],
 [0, 0, 7]]

])