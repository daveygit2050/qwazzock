
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

Clicking on the team's button will lock out that team until the end of the round. This can be useful for managing elimitator rounds and the like.

### Question Types

There are two "question types" you can select, `standard` or `picture`.

#### Standard

This is the default question type. It allows you to ask any question and decide if the answer is right or wrong.

#### Picture

When this quesiton type is selected, all players are presnted with a randomly selected image from the `questions` folder in the content directory (see below) as their buzzer image. You will be presented with the name of the image they are seeing.

The ordering of the images is random. Once you select `pass`, `right` or `wrong`, the next image in the list will be presented. This will continue until you change question type, or you run out of question images. If the latter occurs, the question type will automatically revery back to `standard`.

Should you not provide a content directory, the content directory does not contain a `questions` folder, or the `questions` folder is empty, then the question type will automatically revert back to `standard`.

### Environment variables

Behaviour of the application can be tweaked by setting the following environment variables:

|Name|Options|Default|Description|
|-|-|-|-|
|`QWAZZOCK_CONTENT_PATH`|A valid absolute path.|Not set|If set, additional content is loaded into qwazzock from this directory.|
|`QWAZZOCK_LOG_LEVEL`|`DEBUG`, `INFO`, `WARNING`, `ERROR`|`INFO`|Log application events at this level and above.|
|`QWAZZOCK_SOCKETIO_DEBUG_MODE`|Any|Not set|If set, access logs from socketio will be output.|

### Content Directory

For a more interactive experience, you can load custom content into a "content directory" and provide this to qwazzock using the `QWAZZOCK_CONTENT_PATH` environment variable.

Currently, the only supported custom content is images for use with the `picture` question type. These must be loaded into a `questions` folder within the content directory. The file name should be the answer as you wish it to appear to the host.

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

Tag the repository with the project version and publish the distributables to [PyPI](https://pypi.org/project/qwazzock/).

*Local repo must be clean.*

```
poetry config pypi-token.pypi ${your-pypi-token}
make release
```

