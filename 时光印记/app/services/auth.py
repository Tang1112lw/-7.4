

from passlib.context import CryptContext
#passlib 提供的专业工具专门用来加密校验密码的底层调用bcryot算法
pwd_context =CryptContext(schemes=["bcrypt"],deprecated ="auto")
def hash_password(password :str): #hash加密密码函数
    return pwd_context.hash(password)
#
def verify_password(plain_password:str,hash_password:str):
    return pwd_context.verify(plain_password,hash_password)
