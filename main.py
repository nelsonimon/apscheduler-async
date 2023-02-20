import asyncio
import scheduler as JobManager
from api import app as api
import uvicorn

class Server(uvicorn.Server):
    def handle_exit(self, sig: int, frame) -> None:
        return super().handle_exit(sig, frame)

async def main():  

    server = Server(config=uvicorn.Config(app=api, host='127.0.0.1', port=80))

    loop = asyncio.get_event_loop_policy().get_event_loop()
    tasks = loop.create_task(JobManager.run())
    fastapi = loop.create_task(server.serve())

    await asyncio.wait([tasks,fastapi])

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.ensure_future(main(), loop=loop)
    loop.run_forever()
