
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey,String,Integer,Column,Date
from . import Base
class Story(Base):
    __tablename__ ="stories"
    id = Column(Integer,primary_key=True,index=True)
    member_id = Column(Integer,ForeignKey("members.id"),nullable=False)
    owner = relationship("Member",back_populates="story")
    content = Column(String(5000),nullable=False)
    title =Column(String(60),nullable =False)
    time =Column(Date,nullable =False)