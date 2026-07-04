from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .import Base  #当前项目目录下面导入用点
class User(Base):
    __tablename__ = "users" #表的名字
    id = Column(Integer, primary_key=True, index=True) #列，整数 设置主键 创建目录加速查询
    username = Column(String(20),unique= True,nullable=False)
    password = Column(String(255),nullable =False)
    member =relationship("Member",back_populates="owner")




    
    
