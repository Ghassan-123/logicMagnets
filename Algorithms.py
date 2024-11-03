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
                                    self.PMoves(temp, k, l)
                                elif temp.Matrix[k][l].type == "⭕":
                                    self.Gamelogic.RMoves(temp, k, l)
                                if temp not in self.visited:
                                    self.queue.append(temp)
        headBoard = self.queue.pop(0)
        print(headBoard)
        self.bfs(headBoard)

    def PMoves(self, Board, p_x, p_y):
        row = Board.row
        col = Board.col
        # right
        for i in range(col - 1, p_y, -1):
            if (
                self.InGrid(p_x, i, row, col)
                and (
                    Board.Matrix[p_x][i].type == "⭕"
                    or Board.Matrix[p_x][i].type == "🟣"
                    or Board.Matrix[p_x][i].type == "⚫"
                )
                and (
                    self.InGrid(p_x, i + 1, row, col)
                    and (
                        Board.Matrix[p_x][i + 1].type == "⚪"
                        or Board.Matrix[p_x][i + 1].type == "🔵"
                    )
                )
            ):
                Board.Matrix[p_x][i + 1].type = Board.Matrix[p_x][i].type
                Board.Matrix[p_x][i].type = Board.Matrix[p_x][i].initialType

        # left
        for j in range(1, p_y, +1):
            if (
                self.InGrid(p_x, j, row, col)
                and (
                    Board.Matrix[p_x][j].type == "⭕"
                    or Board.Matrix[p_x][j].type == "🟣"
                    or Board.Matrix[p_x][j].type == "⚫"
                )
                and (
                    self.InGrid(p_x, j - 1, row, col)
                    and (
                        Board.Matrix[p_x][j - 1].type == "⚪"
                        or Board.Matrix[p_x][j - 1].type == "🔵"
                    )
                )
            ):
                Board.Matrix[p_x][j - 1].type = Board.Matrix[p_x][j].type
                Board.Matrix[p_x][j].type = Board.Matrix[p_x][j].initialType

        # up
        for k in range(1, p_x, +1):
            if (
                self.InGrid(k, p_y, row, col)
                and (
                    Board.Matrix[k][p_y].type == "⭕"
                    or Board.Matrix[k][p_y].type == "🟣"
                    or Board.Matrix[k][p_y].type == "⚫"
                )
                and (
                    self.InGrid(k - 1, p_y, row, col)
                    and (
                        Board.Matrix[k - 1][p_y].type == "⚪"
                        or Board.Matrix[k - 1][p_y].type == "🔵"
                    )
                )
            ):
                Board.Matrix[k - 1][p_y].type = Board.Matrix[k][p_y].type
                Board.Matrix[k][p_y].type = Board.Matrix[k][p_y].initialType

        # bottom
        for l in range(row - 1, p_x, -1):
            if (
                self.InGrid(l, p_y, row, col)
                and (
                    Board.Matrix[l][p_y].type == "⭕"
                    or Board.Matrix[l][p_y].type == "🟣"
                    or Board.Matrix[l][p_y].type == "⚫"
                )
                and (
                    self.InGrid(l + 1, p_y, row, col)
                    and (
                        Board.Matrix[l + 1][p_y].type == "⚪"
                        or Board.Matrix[l + 1][p_y].type == "🔵"
                    )
                )
            ):
                Board.Matrix[l + 1][p_y].type = Board.Matrix[l][p_y].type
                Board.Matrix[l][p_y].type = Board.Matrix[l][p_y].initialType

    def InGrid(self, x, y, row, col):
        if 0 <= x < row and 0 <= y < col:
            return True
        else:
            return False
