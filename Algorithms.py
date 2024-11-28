from GameLogic import GameLogic
from heapq import heappush, heappop
import math
import random
import copy


class Algorithms:
    def __init__(self, GameLogic):
        self.visited = []
        self.queue = []
        self.winpath = []
        self.Gamelogic = GameLogic

    def bfs(self, Board):
        row = Board.row
        col = Board.col
        if self.Gamelogic.Checkwin(Board):
            for p in self.printPath(Board):
                print(p)
            print("won")
            return
        self.visited.append(copy.deepcopy(Board))
        for i in range(row):
            for j in range(col):
                if Board.Matrix[i][j].type == "🟣" or Board.Matrix[i][j].type == "⭕":
                    for k in range(row):
                        for l in range(col):
                            temp = copy.deepcopy(Board)
                            temp.parent = Board
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
        self.bfs(headBoard)

    def dfs(self, Board):
        row = Board.row
        col = Board.col
        self.visited.append(copy.deepcopy(Board))

        if self.Gamelogic.Checkwin(Board):
            for p in self.printPath(Board):
                print(p)
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
                            temp.parent = Board
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
                                    if self.dfs(temp):
                                        return True
        return False

    def printPath(self, Board):
        current = Board
        myPath = []
        while current != None:
            myPath.append(current)
            current = current.parent
        myPath.reverse()
        return myPath

    def ucscost(self, currentMoves):
        return currentMoves + 1

    def ucs(self, Board, moves):
        row = Board.row
        col = Board.col
        heappush(self.queue, (moves, Board))
        while self.queue:
            current_cost, current_board = heappop(self.queue)
            for i in range(row):
                for j in range(col):
                    if (
                        current_board.Matrix[i][j].type == "🟣"
                        or current_board.Matrix[i][j].type == "⭕"
                    ):
                        for k in range(row):
                            for l in range(col):
                                temp = copy.deepcopy(current_board)
                                temp.parent = current_board
                                if (
                                    temp.Matrix[k][l].type == "⚪"
                                    or temp.Matrix[k][l].type == "🔵"
                                ):
                                    temp.Matrix[k][l].type = temp.Matrix[i][j].type
                                    temp.Matrix[i][j].type = temp.Matrix[i][
                                        j
                                    ].initialType

                                    if temp.Matrix[k][l].type == "🟣":
                                        self.Gamelogic.PMoves(temp, k, l)
                                    elif temp.Matrix[k][l].type == "⭕":
                                        self.Gamelogic.RMoves(temp, k, l)

                                    cost = self.ucscost(moves)
                                    total_cost = current_cost + cost

                                    if self.Gamelogic.Checkwin(temp):
                                        for p in self.printPath(temp):
                                            print(p)
                                        print("won")
                                        return

                                    if (total_cost, temp) not in self.queue:
                                        heappush(self.queue, (total_cost, temp))

    def heuristic(self, Board):
        row = Board.row
        col = Board.col
        cost = 0
        for i in range(row):
            for j in range(col):
                if Board.Matrix[i][j].type == "⚫":
                    testarr = []
                    for l in range(len(Board.white)):
                        newi = abs(i - Board.white[l][0])
                        newj = abs(j - Board.white[l][1])
                        costy = newi + newj
                        testarr.append(costy)
                    costfor1 = min(testarr)
                    cost += costfor1
                else:
                    if (
                        Board.Matrix[i][j].type == "⭕"
                        or Board.Matrix[i][j].type == "🟣"
                    ):
                        if Board.Matrix[i][j].initialType == "⚪":
                            cost += 0
                        else:
                            cost += 1
        return cost

    def hillclimb(self, Board):
        row = Board.row
        col = Board.col
        costs = self.heuristic(Board)
        print(costs)
        self.visited.append(copy.deepcopy(Board))
        print(Board)

        while True:
            turncosts = []
            for i in range(row):
                for j in range(col):
                    if (
                        Board.Matrix[i][j].type == "🟣"
                        or Board.Matrix[i][j].type == "⭕"
                    ):
                        for k in range(row):
                            for l in range(col):
                                temp = copy.deepcopy(Board)
                                if (
                                    temp.Matrix[k][l].type == "⚪"
                                    or temp.Matrix[k][l].type == "🔵"
                                ):
                                    temp.Matrix[k][l].type = temp.Matrix[i][j].type
                                    temp.Matrix[i][j].type = temp.Matrix[i][
                                        j
                                    ].initialType

                                    if temp.Matrix[k][l].type == "🟣":
                                        self.Gamelogic.PMoves(temp, k, l)
                                    elif temp.Matrix[k][l].type == "⭕":
                                        self.Gamelogic.RMoves(temp, k, l)
                                    turncosts.append((self.heuristic(temp), temp))
            mincost = min(turncosts, key=lambda turncost: turncost[0])
            if mincost[0] >= costs:
                return (mincost[0], mincost[1])
            else:
                costs = mincost[0]
                Board = mincost[1]
                print(Board, f"cost is: {mincost[0]}")
