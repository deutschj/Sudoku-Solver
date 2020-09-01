from tkinter import *

ft = ("Arial", 18)
bk_col = "lightgrey"

root = Tk()


class SudokuSolver:
    counter = 0

    def __init__(self):
        self.counter = 0
        self.setZero()
        self.solve()

    def setZero(self):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    savedNumbers[i][j].set(0)

    def possible(self, y, x, n):
        global grid
        for i in range(0, 9):
            if savedNumbers[y][i].get() == str(n):
                return False
        for i in range(0, 9):
            if savedNumbers[i][x].get() == str(n):
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if savedNumbers[y0 + i][x0 + j].get() == str(n):
                    return False
        return True

    def solve(self, i=0, j=0):
        self.counter += 1
        i, j = self.findNextCellToFill(i, j)

        if i == -1:
            return True

        for n in range(1, 10):
            if self.possible(i, j, n):
                savedNumbers[i][j].set(n)
                if self.solve(i, j):
                    return True
                savedNumbers[i][j].set(0)
        return False

        for x in range(9):
            for y in range(9):
                value = savedNumbers[x][y].get()
                print(value, end=" ")
            print()

    def findNextCellToFill(self, i, j):
        for x in range(i, 9):
            for y in range(j, 9):
                if savedNumbers[x][y].get() == '0':
                    return x, y

        for x in range(0, 9):
            for y in range(0, 9):
                if savedNumbers[x][y].get() == '0':
                    return x, y

        return -1, -1

    def print_counter(self):
        return self.counter


class GUI:
    # savedNumbers = None
    def __init__(self, master):
        self.master = master
        master.title('Solver Sudoku')

        self.__table = []
        for i in range(1, 10):
            self.__table += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # cmds from createGrid()
        for i in range(0, 9):
            for j in range(0, 9):
                    if grid[i][j] != 0:
                        savedNumbers[i][j].set(grid[i][j])

        self.fr = Frame(self.master, padx=5, pady=5)
        self.fr.grid(row=0, column=0, columnspan=4, sticky=W + E)

        for i in range(9):
            for j in range(9):
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    bk_col = 'lightgrey'
                elif i in [3, 4, 5] and j in [3, 4, 5]:
                    bk_col = 'lightgrey'
                else:
                    bk_col = 'white'

                self.__table[i][j] = Entry(self.fr, width=2, font=ft, bg=bk_col, textvar=savedNumbers[i][j])
                self.__table[i][j].grid(row=i, column=j)

        self.btn_help = Button(self.master, width=5, text="Help", fg="red", pady=5, padx=3)
        self.btn_help.grid(row=1, column=1)
        self.btn_solve = Button(self.master, width=5, text="Solve!", fg="red", pady=5, padx=3,
                                command=self.solveInput)
        self.btn_solve.grid(row=1, column=2, pady=10)

    def solveInput(self):
        solution = SudokuSolver()
        for i in range(9):
            for j in range(9):
                print(savedNumbers[i][j].get(), end=" ")
            print()

    def getTable(self):
        return self.__table


grid = [[0, 2, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 8, 1, 0, 0, 6, 0, 0],
        [0, 4, 0, 0, 0, 9, 8, 0, 0],
        [0, 0, 1, 0, 0, 5, 3, 0, 0],
        [9, 6, 0, 0, 8, 0, 0, 5, 1],
        [0, 0, 3, 2, 0, 0, 7, 0, 0],
        [0, 0, 4, 6, 0, 0, 0, 9, 0],
        [0, 1, 6, 0, 0, 8, 5, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 3, 0]]

savedNumbers = []
for i in range(1, 10):
    savedNumbers += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(0, 9):
    for j in range(0, 9):
        savedNumbers[i][j] = StringVar(root)

app = GUI(root)
root.mainloop()
