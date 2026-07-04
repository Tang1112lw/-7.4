from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
     pass
from app.models.story import Story 
from .invitation import Invitation