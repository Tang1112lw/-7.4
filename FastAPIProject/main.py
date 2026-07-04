from fastapi import FastAPI
from routers.news import router as news_router
from routers.users import router as users_router
app = FastAPI()
app.include_router(news_router)
app.include_router(users_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": "fuck you"}
