class Game:
    def __init__(self):
        self.player_in_hotseat = "Pending"

    def buzz(self, player):
        if self.player_in_hotseat == "Pending":
            self.player_in_hotseat = player

    def clear_hotseat(self):
        self.player_in_hotseat = "Pending"
