from Board import Board
from Stage import Stage
from GameLogic import GameLogic
from Algorithms import Algorithms


class Game:
    def __init__(self):

        stage = input("Choose a stage from 1 to 25\n")
        stage = int(stage)
        self.Stage = Stage(stage)
        self.Stage = self.Stage.ChooseStage()
        self.Board = Board(self.Stage)
        self.GameLogic = GameLogic()
        self.Algorithms = Algorithms(self.GameLogic)
        self.Algorithms.bfs(self.Board)
        # self.GameLogic.inputGame(self.Board)


if __name__ == "__main__":
    Game()
