class GameLogic:
    import copy

    boardarray = []

    def __init__(self):
        pass

    def inputGame(self, Board):
        self.boardarray.append(self.copy.deepcopy(Board))
        while self.Checkwin(Board) != True:
            print(Board)
            fp_x = input("Choose moving piece row\n")
            fp_y = input("Choose moving piece column\n")
            fp_x = int(fp_x) - 1
            fp_y = int(fp_y) - 1
            if 0 <= fp_x <= Board.row and 0 <= fp_y <= Board.col:
                if Board.Matrix[fp_x][fp_y].type == "🟣":
                    print("you choosed   P")

                    lp_x = input("Choose taget piece row\n")
                    lp_y = input("Choose taget piece column\n")
                    lp_x = int(lp_x) - 1
                    lp_y = int(lp_y) - 1
                    if 0 <= lp_x < Board.row and 0 <= lp_y < Board.col:
                        if self.Isblank(Board.Matrix[lp_x][lp_y]):
                            Board.Matrix[fp_x][fp_y].type = Board.Matrix[fp_x][
                                fp_y
                            ].initialType
                            Board.Matrix[lp_x][lp_y].type = "🟣"
                            self.PMoves(Board, lp_x, lp_y)
                            self.boardarray.append(self.copy.deepcopy(Board))

                        else:
                            print("you can only move into a blank or white spot")
                    else:
                        print(
                            "the board is a"
                            + Board.row
                            + "*"
                            + Board.col
                            + "board starts with row(column) 0 to 4"
                        )
                elif Board.Matrix[fp_x][fp_y].type == "⭕":
                    print("you choosed   R")
                    lp_x = input("Choose taget piece row\n")
                    lp_y = input("Choose target piece column\n")
                    lp_x = int(lp_x) - 1
                    lp_y = int(lp_y) - 1
                    if 0 <= lp_x < Board.row and 0 <= lp_y < Board.col:
                        if self.Isblank(Board.Matrix[lp_x][lp_y]):
                            Board.Matrix[fp_x][fp_y].type = Board.Matrix[fp_x][
                                fp_y
                            ].initialType
                            Board.Matrix[lp_x][lp_y].type = "⭕"
                            self.RMoves(Board, lp_x, lp_y)
                            self.boardarray.append(self.copy.deepcopy(Board))

                        else:
                            print("you can only move into a blank or white spot")
                    else:
                        print("the board is a 5*5 board starts with row(column) 0 to 4")
                else:
                    print("you have to choose a purple or red magnet first")
            else:
                print("the board is a 5*5 board starts with row(column) 0 to 4")
        else:
            print(Board)
            print("you won :)\n")
            counter = 0
            for board in self.boardarray:
                print(f"step {counter}{board}\n")
                counter += 1

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

    def RMoves(self, Board, r_x, r_y):
        row = Board.row
        col = Board.col
        # right
        for i in range(r_y + 1, col, 1):
            if (
                self.InGrid(r_x, i, row, col)
                and (
                    Board.Matrix[r_x][i].type == "⭕"
                    or Board.Matrix[r_x][i].type == "🟣"
                    or Board.Matrix[r_x][i].type == "⚫"
                )
                and (
                    self.InGrid(r_x, i - 1, row, col)
                    and (
                        Board.Matrix[r_x][i - 1].type == "⚪"
                        or Board.Matrix[r_x][i - 1].type == "🔵"
                    )
                )
            ):
                Board.Matrix[r_x][i - 1].type = Board.Matrix[r_x][i].type
                Board.Matrix[r_x][i].type = Board.Matrix[r_x][i].initialType

        # left
        for j in range(r_y - 1, -1, -1):
            if (
                self.InGrid(r_x, j, row, col)
                and (
                    Board.Matrix[r_x][j].type == "⭕"
                    or Board.Matrix[r_x][j].type == "🟣"
                    or Board.Matrix[r_x][j].type == "⚫"
                )
                and (
                    self.InGrid(r_x, j + 1, row, col)
                    and (
                        Board.Matrix[r_x][j + 1].type == "⚪"
                        or Board.Matrix[r_x][j + 1].type == "🔵"
                    )
                )
            ):
                Board.Matrix[r_x][j + 1].type = Board.Matrix[r_x][j].type
                Board.Matrix[r_x][j].type = Board.Matrix[r_x][j].initialType

        # up
        for k in range(r_x - 1, -1, -1):
            if (
                self.InGrid(k, r_y, row, col)
                and (
                    Board.Matrix[k][r_y].type == "⭕"
                    or Board.Matrix[k][r_y].type == "🟣"
                    or Board.Matrix[k][r_y].type == "⚫"
                )
                and (
                    self.InGrid(k + 1, r_y, row, col)
                    and (
                        Board.Matrix[k + 1][r_y].type == "⚪"
                        or Board.Matrix[k + 1][r_y].type == "🔵"
                    )
                )
            ):
                Board.Matrix[k + 1][r_y].type = Board.Matrix[k][r_y].type
                Board.Matrix[k][r_y].type = Board.Matrix[k][r_y].initialType

        # bottom
        for l in range(r_x + 1, row, 1):
            if (
                self.InGrid(l, r_y, row, col)
                and (
                    Board.Matrix[l][r_y].type == "⭕"
                    or Board.Matrix[l][r_y].type == "🟣"
                    or Board.Matrix[l][r_y].type == "⚫"
                )
                and (
                    self.InGrid(l - 1, r_y, row, col)
                    and (
                        Board.Matrix[l - 1][r_y].type == "⚪"
                        or Board.Matrix[l - 1][r_y].type == "🔵"
                    )
                )
            ):
                Board.Matrix[l - 1][r_y].type = Board.Matrix[l][r_y].type
                Board.Matrix[l][r_y].type = Board.Matrix[l][r_y].initialType

    def InGrid(self, x, y, row, col):
        if 0 <= x < row and 0 <= y < col:
            return True
        else:
            return False

    def Isblank(self, piece):
        if piece.type != "🟣" and piece.type != "⭕" and piece.type != "⚫":
            return True
        else:
            return False

    def Checkwin(self, Board):
        counter = 0
        for i in range(Board.row):
            for j in range(Board.col):
                if Board.Matrix[i][j].type == "⚪":
                    counter += 1
        if counter == 0:
            return True
        else:
            return False
