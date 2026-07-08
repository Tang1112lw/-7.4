f"""
orm
orm由
异步引擎  连接数据库的配置
会话工厂  生产session的工厂 目的是为设置为异步工厂以及规范会话等
模型类    继承基类作为能被识别为数据库的类
注入函数  一个能够将每次请求自动创建为session的函数 请求借宿自动关闭
session  会话函数session 也是通过session间接增删改查数据库

1.异步引擎engine
导入创建会话引擎函数
from sqlclchemy.ext.asyncio impotr async_creat_engine
engine = async_creat_engine(
url =mysql+aiomysql://tang:tang1314520@localhost:3306/timesprint, # 数据库+orm数据库驱动+账号+密码+地址+端口号+数据库（+可加指定格式）
echo =True           #sql语句输出
pool_size=5,         # 连接池大小，默认 5
max_overflow=10,     # 连接池溢出上限
pool_recycle=3600,   # 连接一小时后自动回收，防断开
pool_pre_ping=True,  # 每次取连接前先测试是否有效
 ))


2.会话工厂
会话工厂由异步会话引擎+异步会话类+异步会话工厂创建函数
from sqlclchemy.ext.asyncio import async_sessionmaker,Asyncsession
asyncsessionlocal= async_sessionmaker(engine,class_=Asyncsession,expire_on_commit=False)
expire_on_commit=False 表示 关闭临时数据过期==保存临时会话数据

3.注入函数由会话工厂组成
async def get_db():
    async with asyncsessionlocal() as session:
        yield session  返回给使用session的路由 使用后自动关闭

4.模型类
创建模型类之前需要导入创建基类Base
from sqlalchemy.orm import DeclarativeBase
class Base(Declarativebase):
    pass
定义的每一个模型类都需要继承Base类

定义自建表函数
async def init_db():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)
只要继承了基类 使用自建表函数即可自动创建表

lifesponse 自动建表





模型类 
from database import Base
from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

class User(Base):
    __tablename__ ="定义的每个模型类都需要定义表名users"
    id:Mapped[int] =mapped_column(Integer,primary_key=True,index=True) primary_key=True 主键 index=True 索引,增加查询效率
    task_id:Mapped[int] =mapped_column(Integer,ForeignKey("tasks.id"))
     # 外键 关联tasks表的id字段 当数据与关联字段的数据不一致的时候会报错
     # 关联relationship 后续补充
    name =
    age =

需要设置主键 或外键 或关联relationship 后续补充

5.增删改查
导入Depends注入函数,异步会话类,查询函数select
!!!!  注入函数Depends只能够在fastapi路由里面使用 

from fastapi import Depends
@router.get("/get")
async def get_db(name:str,id:int,session :Asyncsession=Depends(get_db)):#定义一个获取数据库函数

    5.1增
    原sql语句 insert info users (name,age) values("张三",22)
    orm语句 
    users =User(name ="小唐“,age=22)
    session.add(users)  添加user对象到会话队列
    session.flush()  刷新会话队列 用于操作多个对象
    await session.commit()  上传数据库 执行对应的sql语句
    await session.refresh(user) 拿到更新后的id =u=User.id
    return {"id":User.id,"name":User.name}


    5.2 查
    session.get(Model,id)

操作    : 查
ORM 写法: await session.get(Model, id)
SQL 写法: SELECT * FROM ... WHERE id = ?

操作    : 改
ORM 写法: obj.field = 新值 → await session.commit()
SQL 写法: UPDATE ... SET field = 值 WHERE id = ?

操作    : 删
ORM 写法: await session.delete(obj) → await session.commit()
SQL 写法: DELETE FROM ... WHERE id = ?


"""
"""
Git 搭配Github
一、上传、拉取与版本控制

1、下载git 配置信息
winget install --id Git.Git -e --source winget 下载或更新Git
到了新环境配置Git用户信息 做一次全局生效
git config --global user.name "tang1112lw"
git config --golbal user.email "1158920686@qq.com"

登录GitHub 创建仓库 创建仓库是.gitignore 勾选了 python时 需要先拉去再上传


2、创建仓库绑定Github 
cd切换到仓库目录，放入项目文件 
git init 初始化仓库
git add .  把所有文件加入暂存区 
git commit -m "7.4.0"  提交一次快照到本地，快照信息为7，4，1
git remote add origin https://github.com/Tang1112lw/-7.4.git 远程绑定仓库
git remote set-url origin https://github.com/Tang1112lw/-7.4.git 修改仓库绑定的文件地址
git remote -v  查看关联地址
origin  https://github.com/Tang1112lw/-.git (fetch)
origin  https://github.com/Tang1112lw/-.git (push)  
这就是关联的地址 push 代表从仓库上传到GitHub 
               fetch 代表下载GitHub数据到本地仓库



####.gitignore 可以先不看
git status  查看文件跟踪状态  绿色为跟踪 红色为未跟踪
echo ".idea/" > .gitignore  将运行代码产生的垃圾文件排除 避免代码上传传到垃圾文件
echo "__pycache__/" >> .gitignore 
git rm --cached -r FastAPIProject/.idea/ FastAPIProject/
__pycache__/ FastAPIProject/routers/__pycache__/     #移除跟踪列表中的垃圾文件 
再 git status 查看文件跟踪情况 
git add .gitignore  提交至暂存文件
git commit -m "时光印记"  提交暂存文件 并且创建项目快照 


3、上传与拉取
创建好之后回到终端 右上角点击Code 复制链接
git push -u origin main 上传到main分支，Github默认使用main分支上传与拉去
注意 本地初始化的仓库默认为master分支 需改名为main分支再来执行
git branch 查看仓库分支名称 
git branch -m master main 改名为main分支



4、上传
git branch 查看本地仓库分支 
git pull origin main --allow-unrelated-histories 拉去并合并 原因见1、
git push -u origin master:main 上传代码

<<<<<<< HEAD

 以后日常直接在Git仓库里面打开项目修改代码 修改了直接使用下面的代码进行上传和版本控制
 git add .           ← 把你改过的文件加入暂存区
 git commit -m "..."  ← 拍个快照，写上你改了啥
 git push             ← 推到 GitHub

5、版本控制
当更新了代码
git add .
git commit -m "更新笔记“
git tag v7.4.1 加上版本标签
git push origin v7.4.1 上传的同时上传标签


=======
<<<<<<< Updated upstream
git push — 推送/上传代码
-u — 记住这个搭配，以后直接用 git push 就行，不用再打 origin master
origin — 远程仓库的别名，就是你刚才关联的那个 GitHub 地址
master — 你本地要推的分支名
=======
>>>>>>> 618a6b8f2acf6348a4ff75056f05f32c0c5c592c

5、版本控制
当更新了代码
git add .
git commit -m "更新笔记“
git tag v7.4.1 加上版本标签
git push origin v7.4.1 上传的同时上传标签


>>>>>>> Stashed changes
0897654321=- 89605=- ，
下载Git
配置Git 
git config --global user.name
git config --global user.email

创建目录文件接受
cd Git
克隆GitHub上传的文件
git clone GitHub项目链接
cd 项目名称 7.4
git tag 查看标签

6、新环境拉去代码  
下载Git  配置name email
切换到Git 去GitHub复制连接  
git clone https://github.com/Tang1112lw/-.git  克隆仓库文件到本地仓库
打开项目编辑更新
来到项目Git 目录 
cd 到 -7.4

git switch main
git add .
git commit -m "更新了知识文档"
git tag v7.4.2
git push
git push  origin v7.4.2

7、已有文件更新
git switch main 回到主分支 默认文件打开的时候为游离状态
git pull 拉取
git tag 查看标签
git fetch --all 获取最新GitHub 
git reset --hard origin/main 更新为最新版本
git reset --hard 7.4.2 更新指定版本    
git log 查看当前版本




二、多人协作
 # === 入职 ===
 git clone https://github.com/Tang1112lw/-7.4.git
 cd -7.4

 # === 开发新功能 ===
 git switch -c feature-导出Excel
 # 改文件...
 git add .
 git commit -m "添加了导出Excel功能"
 git push -u origin feature-导出Excel
 # → 去 GitHub 提 PR

 # === 审查通过后 ===
 # → 在 GitHub 上点 Merge + Delete branch

 # === 本地同步 ===
 git switch main
 git pull

 # === 如果需要回退 ===
 git log --oneline -5
 git revert 复制的hash值
 git push

"""







"""
Redis


"""

