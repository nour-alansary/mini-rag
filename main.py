from fastapi import FastAPI

app = FastAPI()


@app.get('/welcome')
async def hello():
    return ({'message': 'Hello World'})


