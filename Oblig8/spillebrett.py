from random import randint
from cell import Cell

class Spillebrett:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = []
        self.nCounter = 0
        self.gen = 0
        self.threatCounter = 0
        self.drawBoard()
        self.generate()

    def drawBoard(self):
        for x in range(self.rows):
            gridlist = []
            for antall in range(self.columns):
                cell = Cell()
                gridlist.append(cell)
            self.board.append(gridlist)

    def update(self):
        resurrect = []
        murder = []
        self.gen += 1
        for row in self.board:
            for cell in row:
                self.findNeigborFast(cell.x, cell.y)
                if cell.isAlive():
                    if self.nCounter < 2 or self.nCounter > 3:
                        murder.append(cell)
                elif not cell.isAlive():
                    if self.nCounter == 3:
                        resurrect.append(cell)
        for cell in resurrect:
            cell.live()
        for cell in murder:
            cell.kill()

    def genCounter(self):
        return self.gen

    def aliveCounter(self):
        aliveCount = 0
        for row in self.board:
            for cell in row:
                if cell.isAlive() or cell.isBad():
                    aliveCount += 1
        return aliveCount

    def generate(self) :
        y = 0
        for row in self.board:
            x = 0
            for cell in row:
                cell.x = x
                cell.y = y
                t = randint(1,3)
                f = randint(1,50)
                #if f == 1:
                    #cell.cannibal()
                if t == 1:
                    cell.live()
                x += 1
            y += 1

    def findNeigborFast(self, row, column):
        self.nCounter = 0
        for xx in (-1, 0, 1):
            for yy in (-1, 0, 1):
                x  = xx + column
                y = yy + row

                if (not (xx == 0 and yy == 0)) \
                and x >= 0 and y >= 0 \
                and x < self.rows and y < self.columns:
                    if self.board[x][y].isAlive():
                        self.nCounter += 1
        return self.nCounter

    def eatCell(self):
        pass


    def findThreat(self, row, column):
        self.threatCounter = 0
        for xx in (-1, 0, 1):
            for yy in (-1, 0, 1):
                x = xx + column
                y = yy + row

                if (not (xx == 0 and yy == 0)) \
                and x >= 0 and y >= 0 \
                and x < self.rows and y < self.columns:
                    if self.board[x][y].isBad():
                        self.threatCounter += 1
        return self.threatCounter

    def findNeigbor(self, row, column):
        cellblock = []
        self.nCounter = 0
        for xx in (-1, 0, 1):
            for yy in (-1, 0, 1):
                x  = xx + column
                y = yy + row

                if (not (xx == 0 and yy == 0)) \
                and x >= 0 and y >= 0 \
                and x < self.rows and y < self.columns:
                    cellblock.append(self.board[x][y].isAlive())
                    if self.board[x][y].isAlive():
                        self.nCounter += 1
        return cellblock

    def __str__(self):
        s = ""
        for g in self.board:
            for c in g:
                s += c.state()
            s += "\n"
        return s

if __name__ == "__main__":
    #import colorama
    import time
    #colorama.init()

    def move_cursor(x,y):
        print ("\x1b[{};{}H".format(y+1,x+1))

    def clear():
        print ("\x1b[2J")

    myBoard = Spillebrett(30,30)
    G = 20
    for gen in range(G):
        clear()
        move_cursor(0,0)
        if gen < G:
            print(myBoard, end="\r")
        print("Antall levende celler:", myBoard.aliveCounter(), "Generasjon:", myBoard.genCounter())
        time.sleep(0.5)
        myBoard.update()
