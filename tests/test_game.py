import pytest

from qwazzock import Game


def test_game_init_ok():
    game = Game()
    assert game.player_in_hotseat == "Pending"


def test_game_buzz_ok():
    game = Game()
    game.buzz(player="Bob")
    assert game.player_in_hotseat == "Bob"


def test_game_clear_hotseat_ok():
    game = Game()
    game.player_in_hotseat == "Bob"
    game.clear_hotseat()
    assert game.player_in_hotseat == "Pending"
