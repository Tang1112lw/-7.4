
"""
Git 搭配Github
一、上传与拉取

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

6.新环境拉取
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
git push -u origin v7.4.2

7、已有文件更新
git switch main 回到主分支 默认文件打开的时候为游离状态
git pull 拉取
git tag 查看标签
git fetch --all 获取最新GitHub 
git reset --hard origin/main 更新为最新版本
git reset --hard 7.4.2 更新指定版本    
git log 查看当前版本




"""
