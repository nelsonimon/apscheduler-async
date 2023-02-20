from pytz import utc
from time import sleep
import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.triggers.interval import IntervalTrigger

logging.basicConfig(format='\n%(asctime)s\n   %(levelname)s\n   %(funcName)s(%(lineno)d)\n      %(message)s',
                    filename='job_log.txt')
logging.getLogger('apscheduler').setLevel(logging.WARNING)

jobstores = {'default': SQLAlchemyJobStore(url='sqlite:///jobs.db')}
executors = {'default': ThreadPoolExecutor(20), 'processpool': ProcessPoolExecutor(1)}
job_defaults = {'coalesce': False, 'max_instances': 1}
scheduler = AsyncIOScheduler(executors=executors,
                            job_defaults=job_defaults,
                            jobstores=jobstores,
                            timezone=utc)

async def myfunc_async():
    print('my func start ASYNC')
    await asyncio.sleep(2)    
    print('my func end ASYNC')
    return 1

@scheduler.scheduled_job(IntervalTrigger(seconds=2),id="funcOne")
def funcOne():
    print('funcOne - start')
    sleep(10)
    result = asyncio.run(myfunc_async())
    print(f'funcOne - end = {result}')

@scheduler.scheduled_job(IntervalTrigger(seconds=2),id="funcTwo")
def funcTwo():
    print('funcTwo - start')
    sleep(1)
    #asyncio.run(myfunc_async())
    print('funcTwo - end')

async def run():
    print(f'################## JOB STARTED #######################')
    #JobLogger.log.info('################## JOB STARTED #######################')
    scheduler.start()

    #asyncio.get_event_loop_policy().get_event_loop().run_forever()
    #asyncio.get_event_loop_policy().get_event_loop().run_forever()
    #asyncio.get_event_loop_policy().get_event_loop().run_forever()

    

    