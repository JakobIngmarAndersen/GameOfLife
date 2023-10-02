class Cell:
    def __init__(self):
        self.status = "dead"
        self.x = 0
        self.y = 0

    def kill(self):
        self.status = "dead"

    def live(self):
        self.status = "alive"

    def rampage(self):
        self.status = "cannibal"

    def isBad(self):
        if self.status == "cannibal":
            return True
        else :
            return False

    def isAlive(self):
        if self.status == "alive":
            return True
        else :
            return False

    def state(self):
        if self.status == "alive":
            return "O"
        elif self.status == "cannibal":
            return "X"
        else :
            return "."
