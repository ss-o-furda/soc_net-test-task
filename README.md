# Test task: python developer

## Table of content

- [REST API task description](#django-app---social-network)
- [automated bot task description](#pure-python-app---automated-bot)
- [API docs](#api-docs)
- [How to run?](#how-to-run)
  - [general](#general)
  - [django app](#django-app)
    - [standard way](#standard-way)
    - [easy way](#easy-way)
  - [bot app](#bot-app)

## Django app - Social Network

Object of this task is to create a simple REST API. You can use one framework from this list (Django
Rest Framework, Flask or FastAPI) and all libraries which you are prefer to use with this frameworks.

Basic models:

- User
- Post (always made by a user)

Basic Features:

- user signup
- user login
- post creation
- post like
- post unlike
- analytics about how many likes was made. Example url
  `/api/analytics/?date_from=2020-02-02&date_to=2020-02-15`. API should return analytics aggregated by day.
- user activity an endpoint which will show when user was login last time and when he made a last request to the service.

Requirements:

- Implement token authentication (JWT is prefered)

## Pure Python app - Automated bot

Object of this bot demonstrate functionalities of the system according to defined rules. This bot
should read rules from a config file (in any format chosen by the candidate), but should have
following fields (all integers, candidate can rename as they see fit).

- number_of_users
- max_posts_per_user
- max_likes_per_user

Bot should read the configuration and create this activity:

- signup users (number provided in config)
- each user creates random number of posts with any content (up to max_posts_per_user)
- After creating the signup and posting activity, posts should be liked randomly, posts can be liked multiple times

Notes:

- ​Clean and usable REST API is important
- Bot this is just separate python script, not a django management command or etc.
- the project is not defined in detail, the candidate should use their best judgment for every non-specified requirements (including chosen tech, third party apps, etc)
- however every decision must be explained and backed by arguments in the interview
- Result should be sent by providing a Git url. This is a mandatory requirement.

## API docs

The project uses [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) for documentation.

The documentation can be found at [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

> analytics api can be called only by superuser

## How to run?

### general

```sh
git clone https://github.com/ss-o-furda/soc_net-test-task.git
cd soc_net-test-task
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Create an `.env` file and fill it with your data as in the [.env.example](./.env.example)

### django app

#### standard way

```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

#### easy way

```sh
. ./scripts/runserver.sh
```

### bot app

```sh
python main.py
```
