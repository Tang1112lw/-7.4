f"""
restful Api 接口协议
1、接口动作参数
@outer.get 查看资源
@router.post 添加资源
@rouer.put完整更新资源
@router.patch 更新部分资源
@router.delect 删除资源

2.重定向
导入 
from fastapi.response import RedirectResponse
return RedirectResponse(url ="路径?register=1",status_code=302) 302重定向状态码
?为参数 右边为/login路由参数 并且赋值 目的是为了给前端做判断
请看下方/login路由 
@router.get("/login")
async def login(request: Request, registered: str = None):
    return templates.TemplateResponse(request, "login.html",
        {"request": request, "registered": registered})

请看前端login.html判断
{% if registered %}
                <div class = "alter alter-success" role ="alter">
                    注册成功请登录 
                </div>

注意 重定向永远默认返回GET！！！！！


3.JSON API 模式
后端不再返回html 只返回统一json格式 前端采用JavaScript的fetch()来拿数据



















调用第三方api接口

导入第三方httpx
import httpx
设置url
url =”https://api.deepseek.com/chat/completions”
设置请求头
headers ={
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
}
设置请求体
data ={
    "model": "deepseek-v4-flash",
    "messages": [
        {
            "role": "user",
            "content": "你好"
        }
        {
            "role": "system",
            "content": "你是一个智商200的全领域专家叫小唐"
        }
    ]
    ,
    "timeout": 600, # 600秒超时
    "response_format": {
        "type": "json_object" # 返回json对象
    },
    "stream": True, # 流式返回


}

调用
response=httpx.post(url,headers=headers,json=data)
打印响应
print(response.json()) 

转化为json
import json
json_data = json.loads(response.json())



"""




"""
jinja2模板引擎
路由 = url路径 + http方法 + 处理函数

"""



 