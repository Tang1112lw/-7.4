
"""
Git 搭配Github
一、上传与拉取
1、配置信息 
winget install --id Git.Git -e --source winget 下载或更新Git
git config --global user.name "tang1112lw"
git config --golbal user.email "1158920686@qq.com"

2、创建Git仓库文件目录 
cd切换到目录，放入项目文件 
git add .  跟踪文件 
git status  查看文件跟踪状态  绿色为跟踪 红色为未跟踪
echo ".idea/" > .gitignore  将运行代码产生的垃圾文件排除 避免代码上传传到垃圾文件
echo "__pycache__/" >> .gitignore 
git rm --cached -r FastAPIProject/.idea/ FastAPIProject/
__pycache__/ FastAPIProject/routers/__pycache__/     #移除跟踪列表中的垃圾文件 
再 git status 查看文件跟踪情况 
git add .gitignore  提交至暂存文件
git commit -m "时光印记"  提交暂存文件 并且创建项目快照 

3、关联GitHub 
创建好之后回到终端 右上角点击Code 复制链接
git remote add origin https://github.com/Tang1112lw/-.git 关联仓库
git remote -v 查看关联地址 
origin  https://github.com/Tang1112lw/-.git (fetch)
origin  https://github.com/Tang1112lw/-.git (push)  
这就是关联的地址 push 代表从仓库上传到GitHub 
               fetch 代表下载GitHub数据到本地仓库

4、上传拉取代码
git branch 查看本地仓库分支 
git push -u origin master:main 上传代码

git push — 推送/上传代码
-u — 记住这个搭配，以后直接用 git push 就行，不用再打 origin master
origin — 远程仓库的别名，就是你刚才关联的那个 GitHub 地址
master — 你本地要推的分支名

5、分支管理 
git branch -m master main 改名master 分支为main分支
git push origin main 暂存main分支
git push -u origin main -f  强制覆盖提交main分支 


6、新环境拉去代码  
下载Git  配置name email
切换到Git 去GitHub复制连接  
git clone https://github.com/Tang1112lw/-.git  克隆仓库文件到本地仓库

"""

"""
二、版本控制 
1.git log --oneline --graph  #查看提交历史 压缩成行 分支图

"""