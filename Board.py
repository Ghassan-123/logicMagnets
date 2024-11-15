from Piece import Piece


class Board:
    def __init__(self, Stage):
        self.row = Stage["row"]
        self.col = Stage["col"]
        self.moves = Stage["moves"]
        self.white = Stage["whitePieces"]
        self.red = Stage["redPieces"]
        self.purple = Stage["purplePieces"]
        self.steel = Stage["steelPieces"]
        self.Matrix = [[Piece("🔵") for _ in range(self.col)] for _ in range(self.row)]
        for item in self.white:
            self.Matrix[item[0]][item[1]] = Piece("⚪")
        for item in self.red:
            if self.Matrix[item[0]][item[1]].initialType == "⚪":
                self.Matrix[item[0]][item[1]].type = "⭕"
            else:
                self.Matrix[item[0]][item[1]] = Piece("⭕")
        for item in self.purple:
            if self.Matrix[item[0]][item[1]].initialType == "⚪":
                self.Matrix[item[0]][item[1]].type = "🟣"
            else:
                self.Matrix[item[0]][item[1]] = Piece("🟣")
        for item in self.steel:
            if self.Matrix[item[0]][item[1]].initialType == "⚪":
                self.Matrix[item[0]][item[1]].type = "⚫"
            else:
                self.Matrix[item[0]][item[1]] = Piece("⚫")

    def __eq__(self, other):
        for i in range(self.row):
            for j in range(self.col):
                if self.Matrix[i][j].type != other.Matrix[i][j].type:
                    return False
        if self.moves == other.moves:
            return True
        else:
            return False

    def __str__(self):
        board = ""
        for i in range(self.row):
            board += "\n"
            for j in range(self.col):
                board += self.Matrix[i][j].type + " "
        return board
