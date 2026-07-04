from starlette.requests import Request
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates 
from app.config import key
from contextlib import asynccontextmanager

@asynccontextmanager  #生命周期函数
async def startup(app : FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=startup)    
app.add_middleware(SessionMiddleware,secret_key = key)
templates =Jinja2Templates(directory= "app/templates")

from app.routers import auth
from app.routers import member
#from app.routers import story
app.include_router(auth.router)
app.include_router(member.router)
#app.include_router(story.router)
from app.databases import engine
from app.models import Base

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request,"index.html",{"request": request})



