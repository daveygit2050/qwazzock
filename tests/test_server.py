import pytest

from qwazzock import get_socketio_and_app


@pytest.fixture
def socketio_test_client():
    socketio, app = get_socketio_and_app()
    socketio_test_client = socketio.test_client(app=app)
    yield socketio_test_client


def test_get_socketio_and_app_ok():
    socketio, app = get_socketio_and_app()
    assert "/pass_socket" in list(socketio.server.handlers.keys())
    assert app.name == "qwazzock.server"


def test_get_root_ok(socketio_test_client, mocker):
    mock_render_template = mocker.patch("qwazzock.server.render_template")
    socketio_test_client.app.test_client().get("/")
    mock_render_template.assert_called_once_with("player_client.html")


def test_get_admin_ok(socketio_test_client, mocker):
    mock_render_template = mocker.patch("qwazzock.server.render_template")
    socketio_test_client.app.test_client().get("/admin")
    mock_render_template.assert_called_once_with("admin.html")


def test_post_buzz_ok(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    socketio_test_client.app.test_client().post("/buzz", data={"name": "foo-name"})
    mock_socketio_emit.assert_called_once_with(
        "buzz_data", {"player_in_hotseat": "foo-name"}, namespace="/buzz_data_socket",
    )


def test_connect_buzz_data_socket(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    socketio_test_client.connect(namespace="/buzz_data_socket")
    mock_socketio_emit.assert_called_once_with(
        "buzz_data", {"player_in_hotseat": "Pending"}, namespace="/buzz_data_socket",
    )


def test_send_pass_socket(socketio_test_client, mocker):
    mock_socketio_emit = mocker.patch("qwazzock.server.SocketIO.emit")
    socketio_test_client.connect(namespace="/pass_socket")
    socketio_test_client.emit(namespace="/pass_socket", event="pass")
    mock_socketio_emit.assert_called_once_with(
        "buzz_data", {"player_in_hotseat": "Pending"}, namespace="/buzz_data_socket",
    )
