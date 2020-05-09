import operator


class Game:
    def __init__(self):
        self.scores = {}
        self.locked_out_teams = []
        self.clear_hotseat()
        self.score_value = 1

    def update_hotseat(self, player_name, team_name):
        player_name = player_name.strip()
        team_name = team_name.strip()
        if (
            self.player_in_hotseat == "Pending"
            and team_name not in self.locked_out_teams
        ):
            self.player_in_hotseat = player_name
            self.team_in_hotseat = team_name

    def clear_hotseat(self):
        self.player_in_hotseat = "Pending"
        self.team_in_hotseat = "Pending"

    def reset(self):
        self.clear_hotseat()
        self.scores = {}
        self.locked_out_teams = []

    def right_answer(self):
        self.scores[self.team_in_hotseat] = (
            self.scores.get(self.team_in_hotseat, 0) + self.score_value
        )
        self.scores = dict(
            sorted(self.scores.items(), key=operator.itemgetter(1), reverse=True)
        )
        self.locked_out_teams = []
        self.clear_hotseat()

    def wrong_answer(self):
        self.locked_out_teams.append(self.team_in_hotseat)
        self.clear_hotseat()
