from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from app.config import url

engine =create_async_engine(url,echo=True)#创建异步数据库引擎
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)#创建异步会话工厂
#expire_on_commit=False 关闭对象数据销毁 临时存储在内存中 
async def get_db():
    async with SessionLocal() as session:
        yield session #将会话定义为路由函数  
        