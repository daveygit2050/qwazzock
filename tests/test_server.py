from unittest import mock

import pytest

from qwazzock import Game
from qwazzock import get_socketio_and_app


@pytest.fixture
def game():
    mock_game = mock.MagicMock(autospec=Game)
    mock_game.player_in_hotseat = "Pending"
    mock_game.team_in_hotseat = "Pending"
    return mock_game


@pytest.fixture
def socketio_test_client(mocker):
    def _socketio_test_client(game):
        socketio, app = get_socketio_and_app(game=game)
        return socketio.test_client(app=app)

    return _socketio_test_client


def test_get_socketio_and_app_ok():
    socketio, app = get_socketio_and_app(game=mock.MagicMock())
    assert "/host_client_socket" in list(socketio.server.handlers.keys())
    assert "/player_client_socket" in list(socketio.server.handlers.keys())
    assert app.name == "qwazzock.server"


def test_get_root_ok(socketio_test_client, mocker):
    mock_render_template = mocker.patch("qwazzock.server.render_template")
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.app.test_client().get("/")
    mock_render_template.assert_called_once_with(
        "player_client.html", page_name="player_client"
    )


def test_get_host_ok(socketio_test_client, game, mocker):
    mock_render_template = mocker.patch("qwazzock.server.render_template")
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.app.test_client().get("/host")
    mock_render_template.assert_called_once_with(
        "host_client.html", page_name="host_client"
    )


def test_host_client_socket_connect_ok(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    game = Game()
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.connect(namespace="/host_client_socket")
    assert len(mock_socketio_emit.mock_calls) == 2


def test_host_client_socket_pass_event_ok(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    game = Game()
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.connect(namespace="/host_client_socket")
    socketio_test_client_under_test.emit(namespace="/host_client_socket", event="pass")
    assert len(mock_socketio_emit.mock_calls) == 4


def test_host_client_socket_reset_event_ok(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    game = mock.MagicMock()
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.connect(namespace="/host_client_socket")
    socketio_test_client_under_test.emit(namespace="/host_client_socket", event="reset")
    assert len(mock_socketio_emit.mock_calls) == 4
    game.reset.assert_called_once()


def test_host_client_socket_right_event_ok(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    game = Game()
    game.team_in_hotseat = "Oxford"
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.connect(namespace="/host_client_socket")
    socketio_test_client_under_test.emit(namespace="/host_client_socket", event="right")
    assert len(mock_socketio_emit.mock_calls) == 4


def test_host_client_socket_wrong_event_ok(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    game = Game()
    game.team_in_hotseat = "Oxford"
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.connect(namespace="/host_client_socket")
    socketio_test_client_under_test.emit(namespace="/host_client_socket", event="wrong")
    assert len(mock_socketio_emit.mock_calls) == 4


def test_player_client_socket_connect_ok(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    game = Game()
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.connect(namespace="/player_client_socket")
    assert len(mock_socketio_emit.mock_calls) == 2


def test_player_client_socket_buzz_event_ok(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    game = Game()
    socketio_test_client_under_test = socketio_test_client(game)
    socketio_test_client_under_test.connect(namespace="/player_client_socket")
    socketio_test_client_under_test.emit(
        "buzz",
        {"player_name": "foo-name", "team_name": "foo-team"},
        namespace="/player_client_socket",
    )
    assert len(mock_socketio_emit.mock_calls) == 4
