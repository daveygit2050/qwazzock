from unittest import mock

import pytest

import qwazzock


def test_run_ok(mocker):
    mock_socketio = mock.MagicMock()
    mock_app = mock.MagicMock()
    mocker.patch(
        "qwazzock.get_socketio_and_app", return_value=(mock_socketio, mock_app)
    )
    qwazzock.run()
    mock_socketio.run.assert_called_once_with(
        mock_app, host="0.0.0.0", ssl_context=("cert.pem", "key.pem")
    )
