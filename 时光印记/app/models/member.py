
from sqlalchemy import Column,Integer,ForeignKey,Date,String
from sqlalchemy.orm import relationship
from app.models.users import User
from . import Base
class Member(Base):
    __tablename__ = "members"
    id = Column(Integer,primary_key=True,index = True)
    name =Column(String(20),nullable=False)
    birthday = Column(Date,nullable = False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable =False)
    owner = relationship("User",back_populates= "member")
    story = relationship("Story",back_populates= "owner")
     #ForeignKey 外键关联别的user.id 关联的表名要小写
 