import operator
import os
import random

from qwazzock import logger


class Game:
    def __init__(self, content_path=None):
        self.content_path = content_path
        self.reset()

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

    def next_question(self):
        if self.question_type == "picture":
            self.selected_image_index += 1
            try:
                self.selected_image = self.question_images[self.selected_image_index]
            except IndexError:
                logger.info(
                    "No more picture questions available. Reverting to standard question type."
                )
                self.question_type = "standard"
                self.prepare_picture_round()

    def prepare_picture_round(self):
        self.selected_image_index = None
        try:
            self.question_images = os.listdir(f"{self.content_path}/questions")
        except FileNotFoundError:
            logger.warning(
                f"Could not find questions folder in content directory ({self.content_path}). Picture question type will not be available."
            )
            return
        if self.question_images:
            random.shuffle(self.question_images)
            self.selected_image = self.question_images[0]
        else:
            logger.warning(
                f"No question images available in content directory ({self.content_path}/questions). Picture question type will not be available."
            )
            return
        self.selected_image_index = 0

    def reset(self):
        self.clear_hotseat()
        self.scores = {}
        self.locked_out_teams = []
        self.question_type = "standard"
        self.prepare_picture_round()

    def right_answer(self, score_value=1):
        self.scores[self.team_in_hotseat] = (
            self.scores.get(self.team_in_hotseat, 0) + score_value
        )
        self.sort_scores()
        self.locked_out_teams = []
        self.clear_hotseat()

    def sort_scores(self):
        self.scores = dict(
            sorted(self.scores.items(), key=operator.itemgetter(1), reverse=True)
        )

    def wrong_answer(self, wrong_answer_penalty=0):
        self.scores[self.team_in_hotseat] = (
            self.scores.get(self.team_in_hotseat, 0) - wrong_answer_penalty
        )
        self.locked_out_teams.append(self.team_in_hotseat)
        self.sort_scores()
        self.clear_hotseat()
