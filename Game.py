from Board import Board
from Stage import Stage
from GameLogic import GameLogic
from Algorithms import Algorithms


class Game:
    def __init__(self):

        try:
            stage = input("Choose a stage from 1 to 25\n")
            stage = int(stage)
            self.Stage = Stage(stage)
            self.Stage = self.Stage.ChooseStage()
            self.Board = Board(self.Stage)
            self.GameLogic = GameLogic()
            self.Algorithms = Algorithms(self.GameLogic)
            gamemode = input("input the algorithm name or 0 to play yourself\n")
            match gamemode:
                case "bfs":
                    self.Algorithms.bfs(self.Board)
                case "dfs":
                    self.Algorithms.dfs(self.Board)
                case "ucs":
                    self.Algorithms.ucs(self.Board, 0)
                case "hillclimb":
                    self.Algorithms.hillclimb(self.Board)
                case "a*":
                    self.Algorithms.aStar(self.Board, 0)
                case "0":
                    self.GameLogic.inputGame(self.Board)
                case default:
                    print("you have to enter a valid algo name or 0")
        except:
            print("exited the game")


if __name__ == "__main__":
    Game()
