
___
[![Maintainability](https://api.codeclimate.com/v1/badges/525d61f31b03d1faf110/maintainability)](https://codeclimate.com/github/DmGorokhov/assigment-Bewise/maintainability)
### Main stack:
*FastAPI (v.0.103.2), SQLAlchemy2.0, Pydantic2.0, Alembic, Postresql, Asyncpg*
___
### Installing and running the app
___
#### Requirements:

* Docker compose V2
* Poetry >1.2.2
* Make (is used to run shortcut console-command)

**Poetry** is setup by the commands:

**Linux, macOS, Windows (WSL):**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Details on installing and using the **Poetry** package are available in [official documentation](https://python-poetry.org/docs/).

To install **Poetry** you need **Python 3.7+** use the information from the official website [python.org](https://www.python.org/downloads/)

To install **Docker**, use the information from the official website [docs.docker.com](https://docs.docker.com/engine/install/)

---

### Installation

Cloning the repository and installing dependencies

```bash
git clone git@github.com:DmGorokhov/assigment-Bewise.git
```

Activate virtual environment

```bash
poetry shell
```
*Create .env file and set environment variables using file .env.example as example.
For development purposes you can leave that variables as suggested in example.*

Setup app
```bash
make setup
```
___
#### *Usage*

```
make start-dev   # starts  web server, database and pgadmin docker containers
```
Open your browser at http://127.0.0.1:8000/docs.
You will see the automatic interactive API documentation.
Try api endpoint [/api/v1/questions/add]()
___
On new tab of you browser open http://127.0.0.1:5050/. You will see pgadmin panel.
Input you PGADMIN_MAIL and PGADMIN_PW variables from your .env file.
Now you can make connection to database and check data.
