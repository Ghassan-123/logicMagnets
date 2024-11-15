from GameLogic import GameLogic
import copy


class Algorithms:
    def __init__(self, GameLogic):
        self.visited = []
        self.queue = []
        self.Gamelogic = GameLogic

    def bfs(self, Board):
        row = Board.row
        col = Board.col
        if self.Gamelogic.Checkwin(Board):
            print("won")
            return
        self.visited.append(copy.deepcopy(Board))
        for i in range(row):
            for j in range(col):
                if Board.Matrix[i][j].type == "🟣" or Board.Matrix[i][j].type == "⭕":
                    for k in range(row):
                        for l in range(col):
                            temp = copy.deepcopy(Board)
                            if (
                                temp.Matrix[k][l].type == "⚪"
                                or temp.Matrix[k][l].type == "🔵"
                            ):
                                temp.Matrix[k][l].type = temp.Matrix[i][j].type
                                temp.Matrix[i][j].type = temp.Matrix[i][j].initialType

                                if temp.Matrix[k][l].type == "🟣":
                                    self.Gamelogic.PMoves(temp, k, l)
                                elif temp.Matrix[k][l].type == "⭕":
                                    self.Gamelogic.RMoves(temp, k, l)
                                if temp not in self.visited:
                                    self.queue.append(temp)
        headBoard = self.queue.pop(0)
        print(headBoard)
        self.bfs(headBoard)

    def dfs(self, Board):
        row = Board.row
        col = Board.col
        self.visited.append(copy.deepcopy(Board))

        if self.Gamelogic.Checkwin(Board):
            print("won")
            return True
        if Board.moves <= 0:
            return False

        for i in range(row):
            for j in range(col):
                if Board.Matrix[i][j].type == "🟣" or Board.Matrix[i][j].type == "⭕":
                    for k in range(row):
                        for l in range(col):
                            temp = copy.deepcopy(Board)
                            if (
                                temp.Matrix[k][l].type == "⚪"
                                or temp.Matrix[k][l].type == "🔵"
                            ):
                                temp.Matrix[k][l].type = temp.Matrix[i][j].type
                                temp.Matrix[i][j].type = temp.Matrix[i][j].initialType

                                if temp.Matrix[k][l].type == "🟣":
                                    self.Gamelogic.PMoves(temp, k, l)
                                elif temp.Matrix[k][l].type == "⭕":
                                    self.Gamelogic.RMoves(temp, k, l)
                                if temp not in self.visited:
                                    temp.moves -= 1
                                    print(temp)
                                    if self.dfs(temp):
                                        return True
        return False


