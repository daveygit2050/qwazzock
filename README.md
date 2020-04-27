
# qwazzock

An app for hosting quizes remotely.

## Installing

`pip install qwazzock`

## Usage

Place certificates in the local directory for the SSL public and private keys, named `cert.pem` and `key.pem` accordingly.

Start an instance of the app using:

`qwazzock`

Create a route to localhost:5000 using a hostname included in the SSL certificate.

Instruct players to navigate to the site's root address (e.g. https://qwazzock.randall.lol). They can then enter their name, team name and buzz when they know the answer. Note that players to be on the same team, their team names must match exactly (including case). 

As a host, you can then navigate to the `/host` path (e.g. https://qwazzock.randall.lol/host) in order to see who has buzzed first and to mark their answer. You can respond with the following:

- `pass` can be used when no one wants to buzz in who still can, as they don't know the answer. It clears the hotseat if occupied (e.g if someone buzzed accidentally), and any locked out teams become unlocked.
- `right` clears the hotseat, any locked out teams and awards the team a point.
- `wrong` places the team who answered onto a "locked out" list, preventing them from buzzing in until the current question completed.

You can also use `reset` to wipe all data for the in progress game and start a new one.

### Routing

Getting around the useless Virgin Media Business' routers ability to only port foward to the same port:

```
iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 5000
```

### Certbot

If working at an unroutable location, the below can be used to generate the required ssl key files:

```sudo certbot certonly --manual --preferred-challenges dns```

## Development

### Initialise development environment

`make init`

### Standup a local dev server

`make dev`

The server will be accessible at https://0.0.0.0:5000.

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

### Release version

Local repo must be clean.

`make release`

## Todo

### Features
- Allow player to select existing teams from a list or enter a new team name.
- Allow player to customise client (e.g. different button shapes).
- Give player feedback when they buzzed successfully.
- Give player feedback when they didn't buzz in time.
- Give host audible feedback that someone has buzz.
- Allow players to see live team scores.

### Bug fixes
- Prevent player from buzzing without a name, as this sets player_in_hostseat to empty.
- Remove trailing spaces from player name and team name.
- Only allow letters, numbers and spaces in team name.
- Improve reliability of buzzer send events.
- Stop text/button on buzzer from being selectable.
- Make buzzer slightly smaller to allow screen to be scrolled if necessary.

### Project improvements
- Selenium based journey testing.
- Automatic versioning, changelogs and documentation.
- Type hinting and checking.
- Publish built python wheel to PyPi.
- Implement continuous integration process.
- Implement pull request building.
