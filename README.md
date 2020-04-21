
# qwazzock

An app for hosting quizes remotely.

## Installing

`pip install qwazzock`

## Usage

Place certificates in the local directory for the SSL public and private keys, named `cert.pem` and `key.pem` accordingly.

Start an instance of the app using:

`qwazzock`

Create a route to localhost:5000 using a hostname included in the SSL certificate.

Instruct players to navigate to the site's root address (e.g. https://qwazzock.randall.lol). They can then enter their name and buzz when ready.

As an admin, you can then navigate to the `/admin` path (e.g. https://qwazzock.randall.lol/admin) in order to see who has buzzed first. You can use the `pass` button to clear the hotseat and allow another player to answer, or to move on to the next question.

### Routing

Getting around the useless Virgin Media Business' routers ability to only port foward to the same port:

```
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 5000
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

### Build package

`make build`

## Todo

- Building a docker image.
- Prevent player from buzzing without a name, as this sets player_in_hostseat to empty.
- Selenium based journey testing.
- Automatic versioning, changelogs and documentation.
- Type hinting and checking.
