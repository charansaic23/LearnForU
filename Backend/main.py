import logging
import sys

from fastapi import FastAPI, status
from api_routers.learning_path_router import router as learning_path_router
from orm_dto.db_connection import engine,Base

app = FastAPI(title="LearnForU", version="0.1.0")

Base.metadata.create_all(bind=engine)

def init_log():
    """
    Initialize the logger.

    :return:
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
    )
    log = logging.getLogger("API Main Logger")
    return log


@app.on_event("startup")
async def init_conns():
    """
    Init external connections & middlewares.

    All clients will be initialized once only as Singletons.

    :return:
    """
    api_log = init_log()
    api_log.info("Placeholder to init any dependencies")

@app.get('/health', status_code=status.HTTP_200_OK)
def health_check():
    return {'health': 'ok'}

app.include_router(learning_path_router, tags=["Learning Path"], prefix="/learning-path")
