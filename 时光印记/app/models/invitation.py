from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from .import Base
from datetime import datetime


class Invitation(Base):
    __tablename__ ="invcitations"
    id =Column(Integer,primary_key=True,index=True)
    from_user =Column(Integer,ForeignKey("users.id"),nullable=False)
    to_user = Column(Integer,ForeignKey("users.id"),nullable=False)
    status =Column(String(20),default="pending")
    created_at =Column(DateTime,default=datetime.now)
