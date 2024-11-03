class Piece:
    def __init__(self, type):
        self.type = type
        if type == "⚪":
            self.initialType = "⚪"
        else:
            self.initialType = "🔵"

    def __str__(self):
        return self.type
