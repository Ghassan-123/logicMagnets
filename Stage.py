class Stage:
    def __init__(self, stage_number):
        self.number = stage_number

    def ChooseStage(self):
        Matrix = [[0 for x in range(10)] for y in range(10)]
        if 1 <= self.number <= 25:
            match self.number:
                case 1:
                    return {
                        "row": 3,
                        "col": 4,
                        "purplePieces": [(2, 0)],
                        "redPieces": [],
                        "whitePieces": [(1, 1), (1, 3)],
                        "steelPieces": [(1, 2)],
                    }

                case 2:
                    return {
                        "row": 5,
                        "col": 5,
                        "purplePieces": [(4, 0)],
                        "redPieces": [],
                        "whitePieces": [(0, 2), (2, 0), (2, 2), (2, 4), (4, 2)],
                        "steelPieces": [(1, 2), (2, 1), (2, 3), (3, 2)],
                    }

                case 3:
                    return {
                        "row": 3,
                        "col": 4,
                        "purplePieces": [(2, 0)],
                        "redPieces": [],
                        "whitePieces": [(0, 3), (2, 3)],
                        "steelPieces": [(1, 2)],
                    }

                case 4:
                    return {
                        "row": 5,
                        "col": 3,
                        "purplePieces": [(2, 0)],
                        "redPieces": [],
                        "whitePieces": [(0, 0), (0, 2), (4, 1)],
                        "steelPieces": [(1, 1), (3, 1)],
                    }

                case 5:
                    return {
                        "row": 4,
                        "col": 3,
                        "purplePieces": [(3, 1)],
                        "redPieces": [],
                        "whitePieces": [(0, 0), (1, 0), (3, 0), (0, 2), (1, 2)],
                        "steelPieces": [(1, 0), (1, 2), (2, 0), (2, 2)],
                    }

                case 6:
                    return {
                        "row": 3,
                        "col": 5,
                        "purplePieces": [(2, 0)],
                        "redPieces": [],
                        "whitePieces": [(1, 2), (0, 3), (2, 3)],
                        "steelPieces": [(1, 1), (1, 3)],
                    }

                case 7:
                    return {
                        "row": 5,
                        "col": 4,
                        "purplePieces": [(2, 1)],
                        "redPieces": [],
                        "whitePieces": [(0, 0), (1, 0), (2, 3), (3, 2), (4, 3)],
                        "steelPieces": [(1, 0), (2, 0), (3, 1), (3, 2)],
                    }

                case 8:
                    return {
                        "row": 3,
                        "col": 4,
                        "purplePieces": [(2, 0)],
                        "redPieces": [],
                        "whitePieces": [(0, 0), (0, 2), (2, 2)],
                        "steelPieces": [(1, 1), (1, 2)],
                    }

                case 9:
                    return {
                        "row": 1,
                        "col": 7,
                        "purplePieces": [(0, 0)],
                        "redPieces": [],
                        "whitePieces": [(0, 1), (0, 3), (0, 6)],
                        "steelPieces": [(0, 3), (0, 5)],
                    }

                case 10:
                    return {
                        "row": 4,
                        "col": 4,
                        "purplePieces": [(0, 0)],
                        "redPieces": [],
                        "whitePieces": [(1, 1), (1, 3), (3, 0), (3, 3)],
                        "steelPieces": [(2, 2), (2, 3), (3, 1)],
                    }

                case 11:
                    return {
                        "row": 2,
                        "col": 5,
                        "purplePieces": [],
                        "redPieces": [(1, 2)],
                        "whitePieces": [(0, 1), (0, 2), (0, 3)],
                        "steelPieces": [(0, 0), (0, 4)],
                    }

                case 12:
                    return {
                        "row": 5,
                        "col": 4,
                        "purplePieces": [],
                        "redPieces": [(3, 1)],
                        "whitePieces": [(1, 0), (2, 0), (4, 0), (4, 2)],
                        "steelPieces": [(0, 0), (1, 0), (4, 3)],
                    }

                case 13:
                    return {
                        "row": 3,
                        "col": 6,
                        "purplePieces": [],
                        "redPieces": [(2, 3)],
                        "whitePieces": [(0, 3), (2, 1), (1, 1), (0, 4)],
                        "steelPieces": [(0, 0), (0, 4), (0, 5)],
                    }

                case 14:
                    return {
                        "row": 4,
                        "col": 4,
                        "purplePieces": [],
                        "redPieces": [(3, 3)],
                        "whitePieces": [(1, 0), (1, 2), (2, 2), (2, 1)],
                        "steelPieces": [(0, 3), (2, 0), (3, 0)],
                    }

                case 15:
                    return {
                        "row": 3,
                        "col": 5,
                        "purplePieces": [(1, 2)],
                        "redPieces": [(2, 2)],
                        "whitePieces": [(1, 4), (0, 0), (0, 2), (2, 4)],
                        "steelPieces": [(0, 3), (0, 1)],
                    }

                case 16:
                    return {
                        "row": 5,
                        "col": 5,
                        "purplePieces": [(2, 4)],
                        "redPieces": [(2, 0)],
                        "whitePieces": [(0, 3), (0, 4), (4, 3), (4, 0)],
                        "steelPieces": [(1, 2), (3, 2)],
                    }

                case 17:
                    return {
                        "row": 4,
                        "col": 4,
                        "purplePieces": [(3, 3)],
                        "redPieces": [(0, 0)],
                        "whitePieces": [(1, 1), (1, 3), (2, 2), (3, 1)],
                        "steelPieces": [(0, 2), (2, 0)],
                    }

                case 18:
                    return {
                        "row": 5,
                        "col": 6,
                        "purplePieces": [(4, 3)],
                        "redPieces": [(4, 2)],
                        "whitePieces": [(2, 3), (2, 1), (2, 2), (2, 5), (1, 3)],
                        "steelPieces": [(2, 0), (0, 3), (2, 5)],
                    }

                case 19:
                    return {
                        "row": 5,
                        "col": 5,
                        "purplePieces": [(0, 2)],
                        "redPieces": [(2, 2)],
                        "whitePieces": [(1, 0), (3, 0), (2, 1), (3, 2), (3, 4), (1, 4)],
                        "steelPieces": [(0, 3), (0, 1), (4, 1), (4, 3)],
                    }

                case 20:
                    return {
                        "row": 5,
                        "col": 4,
                        "purplePieces": [(4, 2)],
                        "redPieces": [(4, 3)],
                        "whitePieces": [(0, 1), (0, 3), (1, 0), (2, 0), (3, 0)],
                        "steelPieces": [(0, 1), (0, 2), (4, 0)],
                    }

                case 21:
                    return {
                        "row": 3,
                        "col": 4,
                        "purplePieces": [(2, 0)],
                        "redPieces": [(2, 3)],
                        "whitePieces": [(1, 0), (1, 1), (0, 2), (2, 0), (2, 1)],
                        "steelPieces": [(0, 1), (1, 1), (1, 2)],
                    }

                case 22:
                    return {
                        "row": 4,
                        "col": 5,
                        "purplePieces": [(0, 0)],
                        "redPieces": [(3, 2)],
                        "whitePieces": [(0, 1), (0, 3), (1, 0), (1, 4), (2, 1)],
                        "steelPieces": [(0, 3), (0, 4), (3, 0)],
                    }

                case 23:
                    return {
                        "row": 4,
                        "col": 5,
                        "purplePieces": [(3, 4)],
                        "redPieces": [(3, 2)],
                        "whitePieces": [(0, 2), (2, 1), (2, 2), (2, 3), (3, 2)],
                        "steelPieces": [(0, 3), (1, 4), (2, 0)],
                    }

                case 24:
                    return {
                        "row": 5,
                        "col": 5,
                        "purplePieces": [(1, 4)],
                        "redPieces": [(3, 0)],
                        "whitePieces": [(0, 3), (2, 1), (2, 3), (4, 1), (4, 2)],
                        "steelPieces": [(0, 1), (1, 3), (3, 4)],
                    }

                case 25:
                    return {
                        "row": 5,
                        "col": 4,
                        "purplePieces": [(4, 0)],
                        "redPieces": [(0, 3)],
                        "whitePieces": [(0, 0), (0, 3), (2, 0), (4, 0), (4, 1), (4, 2)],
                        "steelPieces": [(0, 0), (1, 2), (3, 2), (4, 3)],
                    }

        else:
            print("There is only 25 levels\n")
