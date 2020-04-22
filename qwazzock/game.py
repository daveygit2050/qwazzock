class Game:
    def __init__(self):
        self.clear_hotseat()

    def update_hotseat(self, player_name, team_name):
        if self.player_in_hotseat == "Pending":
            self.player_in_hotseat = player_name
            self.team_in_hotseat = team_name

    def clear_hotseat(self):
        self.player_in_hotseat = "Pending"
        self.team_in_hotseat = "Pending"
