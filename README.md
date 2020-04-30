
# qwazzock

An app for hosting quizes remotely.

## Installing

`pip install qwazzock`

## Usage

Start an instance of the app using:

`qwazzock`

Create a route to localhost:5000 using a hostname included in the SSL certificate.

Instruct players to navigate to the site's root address (e.g. http://127.0.0.1:5000). They can then enter their name, team name and buzz when they know the answer. Note that players to be on the same team, their team names must match exactly (including case). 

As a host, you can then navigate to the `/host` path (e.g. http://127.0.0.1:5000/host) in order to see who has buzzed first and to mark their answer. You can respond with the following:

- `pass` can be used when no one wants to buzz in who still can, as they don't know the answer. It clears the hotseat if occupied (e.g if someone buzzed accidentally), and any locked out teams become unlocked.
- `right` clears the hotseat, any locked out teams and awards the team a point.
- `wrong` places the team who answered onto a "locked out" list, preventing them from buzzing in until the current question completed.

You can also use `reset` to wipe all data for the in progress game and start a new one.

### Environment variables

Behaviour of the application can be tweaked by setting the following environment variables:

|Name|Options|Default|Description|
|-|-|-|-|
|`QWAZZOCK_LOG_LEVEL`|`DEBUG`, `INFO`, `WARNING`, `ERROR`|`INFO`|Log application events at this level and above.|
|`QWAZZOCK_SOCKETIO_DEBUG_MODE`|Any|Not set|If set, access logs from socketio will be output.|

## Development

### Initialise development environment

`make init`

### Standup a local dev server

`make dev`

The server will be accessible at https://127.0.0.1:5000.

### Run all tests

`make test`

This includes:

- unit tests (`make unit_test`).
- static code analysis (`make bandit`).
- dependency vulnerability analysis (`make safety`).

### Build artefacts

`make build`

This includes:

- pip wheel (`make build_wheel`).
- docker image (`make build_image`).

### Standup a local container

`make run`

### Stop local containers

`make stop`

### Release version

Local repo must be clean.

`make release`

## Todo

### Features
- Allow player to select existing teams from a list or enter a new team name.
- Allow player to customise client (e.g. different button shapes).
- Give player feedback when they didn't buzz in time (kind of done, it says who did buzz successfully).
- Give host audible feedback that someone has buzzed (done for host).
- Allow players to see live team scores.

### Bug fixes
- Only allow letters, numbers and spaces in team name.
- Improve reliability of buzzer send events (possibly done).

### Project improvements
- Selenium based journey testing.
- Automatic versioning, changelogs and documentation.
- Type hinting and checking.
- Publish built python wheel to PyPi.
- Implement continuous integration process.
- Implement pull request building.
