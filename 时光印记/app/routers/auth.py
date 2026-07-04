from starlette.requests import Request
from sqlalchemy import select
from fastapi import APIRouter, Form,Depends
from ..models.users import User
from ..services.auth import hash_password
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse
from ..services.auth import verify_password
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory = "app/templates")
from app.databases import get_db
router = APIRouter()

@router.post("/register") #注册账号密码函数
async def register( request:Request,username :str = Form(),password :str =Form(),session :AsyncSession =Depends(get_db)):
    result = await session.execute(select(User).where(User.username == username))
    result2 =result.scalar_one_or_none()
    if result2 == None:
        hash_pw = hash_password(password)
        new_user =User(username =username,password = hash_pw)
        session.add(new_user)
        await session.commit()
        return RedirectResponse(url="/login?registered=1")
    else:
        print("用户已存在")
        return templates.TemplateResponse(request,"register.html",{"request":request,"error":"请换个名字"})


#登录函数 
@router.post("/login")
async def login(request: Request,username :str= Form(),password :str = Form(),session : AsyncSession = Depends(get_db)):
    try:
        result = await session.execute(select(User).where(User.username == username)) #第一次取出对象集不仅包含一横排字段还包含影响的行数 列数
        user = result.scalar_one_or_none() #通过这个函数筛选出result 所有属性字段数据
        if user == None:
            print("用户不存在返回注册界面")
            return RedirectResponse(url ="/register")
    except:
        print("数据库查询错误")
    verify_pw =verify_password(password,user.password)
    if verify_pw:
        request.session["user_id"] = user.id
        return RedirectResponse(url="/member",status_code=302)
        
    else:
        print("密码错误")

@router.get("/login")
async def login(request :Request,registered: str =None):
    return templates.TemplateResponse(request,"login.html",{"request":request,"registered":registered})

@router.get("/register")
def register(request : Request):
    return templates.TemplateResponse(request,"register.html",{"request":request})



