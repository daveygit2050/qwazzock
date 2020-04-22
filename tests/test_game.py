import pytest

from qwazzock import Game


def test_game_init_ok(mocker):
    mock_clear_hotseat = mocker.patch("qwazzock.Game.clear_hotseat")
    game = Game()
    mock_clear_hotseat.assert_called_once()


def test_game_update_hotseat_ok():
    game = Game()
    game.update_hotseat(player_name="Bob", team_name="Oxford")
    assert game.player_in_hotseat == "Bob"
    assert game.team_in_hotseat == "Oxford"


def test_game_clear_hotseat_ok():
    game = Game()
    game.player_in_hotseat = "Bob"
    game.team_in_hotseat = "Oxford"
    game.clear_hotseat()
    assert game.player_in_hotseat == "Pending"
    assert game.team_in_hotseat == "Pending"
