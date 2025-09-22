from fastapi import FastAPI , APIRouter
import os

app_name = os.environ['APP_NAME']
app_version = os.environ['APP_VERSION']


base_router = APIRouter(prefix='/api/v1',
                        tags=['/api/v1'])


@base_router.get('/')
def hello():
    return {
        'message' : app_name,
        'message1' : app_version
    }