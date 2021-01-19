# BoardGameTimerDesktop

It is a desktop application designed to support time counting while playing board games.<br>

### About

Application:

- code is written with python 3.8
- is written with PyQt5 framework
- ui is generated from .ui files, made in QtDesigner
- is connected to sqlite3 database, db file kept locally
- uses DAO design pattern
- is tested with unittest package including patch and MagicMock
- code passes 10/10 pylint with several pylint recommendations disabled
- can be run as docker image using host tool XQartz.

### Run app:

1. Copy this repository.
2. Go to folder with repo and execute:

```sh
$ python3 board_game_timer_app.py
```

### Run app with docker (on MacOs):

1. Execute in terminal:

```sh
$ brew install --cask xquartz 
$ brew install --cask docker
```

2. Open XQartz app.

```sh
$ open -a XQuartz
```

3. In XQartz mark in security tab:
    - “Allow connections from network clients”

4. Restart computer.

5. Open XQartz and run docker, copy this repository.

6. Go to folder with repo and execute:

```sh
$ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
$ xhost + $IP
$ docker build -t bgt:1.0 .
$ docker-compose up -d
```

#### Helpful commands:

1. Convert ui files into python class:

```sh
$ pyuic5 src/resources/ui/main.ui -o src/resources/ui/main.py
$ pyuic5 src/resources/ui/manage_game.ui -o src/resources/ui/manage_game.py
$ pyuic5 src/resources/ui/play_game.ui -o src/resources/ui/play_game.py
```

2. Run tests:

```sh
$ python -m unittest discover -s src/tests -p 'test_*.py'
```

3. Run pylint on directory with application code:

```sh
$ pylint src/main
``` 

4. requirements.txt file

```sh
$ pip freeze > requirements.txt
$ pip install requiremenets.txt
```
