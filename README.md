# Game Night

## An place to schedule the best game nights with your friends :game_die::game_die:

# THIS REPOSITORY IS A WORKING PROJECT

### User cases:

- [ ] As a user i can register to the app.
- [ ] As a user i can login on my acount.
- [x] As a logged user I can see my list of Games.
- [x] As a logged user I can add a Game to my list.
- [x] As a logged user I can edit a Game on my list.
- [x] As a logged user I can delete a Game on my list.
- [ ] As a logged user I can create a Match.
- [ ] As a logged user I can delete a match that i create.
- [ ] As a logged user I can join a Match created by another user.
- [ ] As a logged user I can see the list of games on a match that i'd joined.
- [ ] As a logged user I can select a game to be played in a match that i'd joined.
- [ ] As a logged user I can select a game to be removed from a match that i'd joined.
- [ ] As a user i can see the select game to the match i'd joined.
- [ ] As a user I can put this app on my mobile home

### Stack solution:

- Server: Flask (Python)
- DB: Postgres
- Front: SSR Template with Flask
- Deploy: Google Cloud on App Engine Standard

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You'll need to install:

- Python >= 2.7
- Postgres
- virtualenv

### Installing

A step by step series of examples that tell you how to get a development env running

Clone this repo

```
git clone https://github.com/minggas/game-night.git
```

Move to the appropriate directory:

```
cd game-night
```

create a virtual env:

```
virtualenv env
```

and activate:

```
source env/bin/activate
```

then install the depedencies:

```
pip install -r requirements.txt
```

And run:

```
python main.py
```

## Running the tests

TODO

### Break down into end to end tests

TODO

### And coding style tests

TODO

## Deployment

TODO

## Authors

- **MInggas** - _Initial work_ - [minggas](https://github.com/minggas)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- **Billie Thompson** - _README Sample_ - [PurpleBooth](https://github.com/PurpleBooth)
