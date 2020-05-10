import pytest

from qwazzock import Game


class TestGame:
    def test_game_init_ok(self, mocker):
        mock_clear_hotseat = mocker.patch("qwazzock.Game.clear_hotseat")
        game = Game()
        mock_clear_hotseat.assert_called_once()

    def test_game_update_hotseat_ok(self):
        game = Game()
        game.update_hotseat(player_name="Bob", team_name="Oxford")
        assert game.player_in_hotseat == "Bob"
        assert game.team_in_hotseat == "Oxford"

    def test_game_update_hotseat_locked_out(self):
        game = Game()
        game.locked_out_teams = ["Oxford"]
        game.update_hotseat(player_name="Bob", team_name="Oxford")
        assert game.team_in_hotseat == "Pending"

    def test_game_update_hotseat_trailing_spaces(self):
        game = Game()
        game.update_hotseat(player_name="Bob ", team_name="My Team  ")
        assert game.player_in_hotseat == "Bob"
        assert game.team_in_hotseat == "My Team"

    def test_game_clear_hotseat_ok(self):
        game = Game()
        game.player_in_hotseat = "Bob"
        game.team_in_hotseat = "Oxford"
        game.clear_hotseat()
        assert game.player_in_hotseat == "Pending"
        assert game.team_in_hotseat == "Pending"

    def test_game_reset_ok(self):
        game = Game()
        game.player_in_hotseat = "Bob"
        game.team_in_hotseat = "Oxford"
        game.locked_out_teams = ["Bristol"]
        game.scores = {"Oxford": 1, "Cambridge": 3}
        game.reset()
        assert game.player_in_hotseat == "Pending"
        assert game.team_in_hotseat == "Pending"
        assert game.locked_out_teams == []
        assert game.scores == {}

    def test_game_right_answer_ok(self, mocker):
        mock_clear_hotseat = mocker.patch("qwazzock.Game.clear_hotseat")
        game = Game()
        game.team_in_hotseat = "Oxford"
        game.scores = {"Oxford": 1, "Cambridge": 3}
        game.right_answer(5)
        assert game.scores == {"Oxford": 6, "Cambridge": 3}
        assert len(mock_clear_hotseat.mock_calls) == 2

    def test_game_wrong_answer_ok(self, mocker):
        mock_clear_hotseat = mocker.patch("qwazzock.Game.clear_hotseat")
        game = Game()
        game.team_in_hotseat = "Oxford"
        game.scores = {"Oxford": 1, "Cambridge": 3}
        game.locked_out_teams = ["Bristol"]
        game.wrong_answer()
        assert game.scores == {"Oxford": 1, "Cambridge": 3}
        assert game.locked_out_teams == ["Bristol", "Oxford"]
        assert len(mock_clear_hotseat.mock_calls) == 2
