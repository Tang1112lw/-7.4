
from app.models.users import User
from sqlalchemy import select,String
from fastapi import APIRouter,Form,Depends,Request
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
templates =Jinja2Templates(directory="app/templates")
from ..databases import get_db
from ..models.member import Member




router = APIRouter()
@router.get("/member") #用户登录第一界面
async def member_list(request:Request,session :AsyncSession = Depends(get_db)):
    user_id =request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login")
    result =await session.execute(select(Member).where(Member.user_id == user_id))
    members =result.scalars().all()

    return templates.TemplateResponse(request,"members.html",{"request":request,"members":members})


@router.get("/member/add")
async def add_member(request:Request):
    return templates.TemplateResponse("request",add_member.html,{"request":request})


@router.get("/member/search")
async def search_member(request:Request,search_user:str ="" ,session:AsyncSession =Depends(get_db)):

    result =await session.execute(select(User).where(User.username.contains(search_user))) #模糊匹配
    result2 =result.scalar_one_or_none()
    if not result2 == None:
        print("查询到用户可以添加")




    

#登陆界面 



    

