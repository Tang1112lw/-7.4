from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
from sqlalchemy.orm import sessionmaker

db_URL= "mysql+aiomysql://tang:tang1314520@localhost:3306?charset=utf8mb4"

async_engine = create_async_engine(
    db_URL,
    echo=False,
    pool_size=10,
    max_overflow=20,
)
async_session = sessionmaker(

)