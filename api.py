from time import sleep
from typing import Union
from fastapi import FastAPI
from scheduler import scheduler

app = FastAPI(title="FastAPI and Async APScheduler",docs_url="/")


@app.get("/list")
def list():
    jobs = scheduler.get_jobs()
    result = []
    for job in jobs:
        result.append({'job_id':job.id,
                        'trigger':str(job.trigger),
                        'next_run_time':str(job.next_run_time),
                        'pending':job.pending})
    return result

@app.get("/remove/{job_id}")
def remove(job_id: str):
    print(f'Removing job {job_id}')
    scheduler.remove_job(job_id=job_id)
    return f'job {job_id} removed'

@app.get("/pause/{job_id}")
def pause(job_id: str):
    print(f'Pausing job {job_id}')
    scheduler.pause_job(job_id=job_id)
    return f'job {job_id} paused'

@app.get("/resume/{job_id}")
def resume(job_id: str):
    print(f'Resuming job {job_id}')
    scheduler.resume_job(job_id=job_id, jobstore='default')
    return f'job {job_id} resumed'