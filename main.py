from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import delete_tables, create_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("base deleted")
    await create_tables()
    print('base success')
    yield
    print('base off')

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)