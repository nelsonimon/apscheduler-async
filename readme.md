# Demo: APScheduler Async with FastAPI

This is a demo for creating a scheduler with an API.
I use [APScheudler](https://github.com/agronholm/apscheduler) for my scheduler and [FastAPI](https://fastapi.tiangolo.com/)
for our API.

This contains three source files:

- ``api.py``: FastAPI application
- ``scheduler.py``: APScheduler application (add your tasks herre)
- ``main.py``: Main launch script (modify as needed)

## Instalation

Clone this repository:
```console
git clone https://github.com/nelsonimon/apscheduler-async.git
```

Install the dependencies (This project was created in Python 3.10):
```console
pip install -r requirements.txt
```

## Running
```console
python app/main.py
```

## Observations:
 - ``jobs.db``: Contain the jobstores with nexts run time of each task
 - ``job_log.txt``: is create automatically and contain the logs of APScheduler

 Autor: [Nelson Imon](https://github.com/nelsonimon)