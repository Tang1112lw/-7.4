# ============================================================
# Python 就业学习 — 知识点回顾 + 错题本
# ============================================================
# 整合自全部学习记录，含 21 道错题 + 核心知识点速查
# 复习方式：盖住 ✅ 部分，只看 ❌ 和题目
# ============================================================


########## 第一部分：核心知识点速查 ##########

"""
【1. 变量与类型】
- 变量命名：字母/下划线开头，不能是关键字，区分大小写
- 四类型：int(整数)  float(小数)  str(字符串)  bool(True/False)
- type(x) 查类型，int()/str()/float() 转换类型
- f-string：f"你好{name}"  用花括号嵌入变量

【2. 运算符】
- 算术：+ - * /（普通除） //（整除） %（取余） **（幂）
- 比较：== != > < >= <=
- 逻辑：and（与） or（或） not（非）
- 链式比较：90 <= a <= 100

【3. 条件判断】
- if 条件: / elif 条件: / else:
- 缩进必须一致（4个空格）

【4. 循环】
- for i in range(start, end):   # end不包含
- for item in 列表:             # 遍历列表
- while 条件:                   # 条件真就一直执行
- break：直接跳出循环
- continue：跳过本次，继续下一次

【5. 列表 list — []】
- 索引：list[0](第一个)  list[-1](倒数第一)
- 切片：list[start:end:step]  冒号分隔，end不包含
- 增：append(值)末尾加  insert(位置,值)指定位置插入
- 删：remove(值)按值删  pop(位置)按位置删
- 改：list[索引] = 新值
- 查：len()  in  count()
- 排序：sort() 升序  reverse() 反转

【6. 字典 dict — {key: value}】
- 取值：dict["键"] 或 dict.get("键", 默认值)  ← .get()更安全
- 增/改：dict["键"] = 值
- 删：dict.pop("键")
- 遍历：.keys()  .values()  .items()
- 查键： "键" in dict

【7. 元组 tuple — ()  不可修改】
【8. 集合 set — {}  无序、不重复、去重专用】
【9. 列表推导式 — [表达式 for x in 序列 if 条件]】

【10. 函数】
- 定义：def 函数名(参数):
- return：把值传回调用处（重要！不是print）
- print：只在屏幕显示，不传回值
- 默认参数：def f(name, age=18):   # age有默认值
- *args：接收不定数量的参数，函数内是元组

【11. lambda — 匿名函数】
- 格式：lambda 参数: 返回值（自动return，不用写return）
- 场景：配合 map/filter/max/min/sorted 的 key 参数

【12. 内置函数】
- map(函数, 列表)：对每个元素做同样操作 → 用list()转
- filter(函数, 列表)：筛选符合条件的元素 → 用list()转
- enumerate(列表, start=1)：遍历带序号
- zip(列表1, 列表2)：配对遍历

【13. 文件操作】
- 写：with open("文件","w",encoding="utf-8") as f:
- 读：with open("文件","r",encoding="utf-8") as f:
- w 覆盖写，a 追加写，r 读

【14. 异常处理】
- try: ... except 异常类型: ... finally: ...（finally一定执行）
- 常见：ZeroDivisionError  ValueError  FileNotFoundError

【15. 面向对象】
- class 类名: 定义类（大驼峰命名）
- __init__(self, ...): 初始化方法，创建对象自动调用
- self 代表对象自身
- 对象.属性 = 值 → 动态添加属性
- 对象.__dict__ → 查看所有属性

【16. 作用域】
- 函数内变量是局部的，不影响外部同名变量
"""


########## 第二部分：错题本（21 道） ##########

# ===========================================
# 错题 1：取列表最后一个元素
# ===========================================
# ❌ l.append
# 原因：append 是添加方法，不是取元素
# ✅ l[-1]


# ===========================================
# 错题 2：列表索引从 0 开始
# ===========================================
# ❌ print(l[1])  以为取第一个
# 原因：索引从0开始，第一个是l[0]
# ✅ print(l[0])


# ===========================================
# 错题 3：变量名不能丢
# ===========================================
# ❌ print([-1])
# 原因：[-1] 是只含-1的列表，漏写了变量名
# ✅ print(l[-1])


# ===========================================
# 错题 4：insert() ≠ 赋值修改
# ===========================================
# ❌ fruits.insert(1, "草莓")  # 题目要求"改"香蕉为草莓
# 原因：insert 插入新元素，香蕉还在
# ✅ fruits[1] = "草莓"


# ===========================================
# 错题 5：切片用冒号不是逗号
# ===========================================
# ❌ nums[0,3]   nums[-3,0]   nums[2,5]
# 原因：切片语法是 [start:end:step]，用冒号分隔
# ✅ nums[:3]    nums[-3:]    nums[2:6]


# ===========================================
# 错题 6：字典用方括号取值
# ===========================================
# ❌ student("姓名")
# 原因：字典用 [] 按键取值，() 是函数调用
# ✅ student["姓名"]


# ===========================================
# 错题 7：切片 end 不包含
# ===========================================
# ❌ nums[:2] 想取前3个
# 原因：[start:end] 中 end 不包含，取前3要写到索引3 → nums[:3]
# ✅ nums[:3]


# ===========================================
# 错题 8：索引与"第几个"的换算
# ===========================================
# ❌ nums[2:5] 想取"第3到第6个"
# 原因：第3个=索引2，第6个=索引5，想包含索引5要写到6
# 口诀：右边界 = 想要的最后一个索引 + 1
# ✅ nums[2:6]


# ===========================================
# 错题 9：列表是方括号，集合是花括号
# ===========================================
# ❌ names = {"Alice", "Bob", "Cindy"}
# 原因：{} 是集合(set)，无序不可重复；[] 才是列表(list)
# ✅ names = ["Alice", "Bob", "Cindy"]


# ===========================================
# 错题 10：用内置函数名做变量名
# ===========================================
# ❌ int = 10   float = 3.14   str = "hello"   bool = True
# 原因：覆盖了内置函数，之后无法用 int()、str() 等
# ✅ my_int = 10


# ===========================================
# 错题 11：type() 只能传一个参数
# ===========================================
# ❌ print(type(a, b, c, d))
# 原因：type() 一次只接受一个参数
# ✅ print(type(a), type(b), type(c), type(d))


# ===========================================
# 错题 12：f-string 括号不对
# ===========================================
# ❌ print(f"大家好，今年（{age}岁")
# 原因：中文括号多余，格式不对
# ✅ print(f"大家好，今年{age}岁")


# ===========================================
# 错题 13：while 循环累加逻辑
# ===========================================
# ❌
# i = 0; a = 0
# while i <= 100:
#     a = i + 1   # 每次覆盖，不是累加
#     i = i + 1
#
# ✅
# i = 1; total = 0
# while i <= 100:
#     total = total + i   # 累加
#     i = i + 1


# ===========================================
# 错题 14：input() 放在 while 循环外面
# ===========================================
# ❌ 猜数字只输入一次，后面死循环
# b = int(input("猜: "))
# while True: ...
#
# ✅ input 放进循环里面
# while True:
#     b = int(input("猜: "))


# ===========================================
# 错题 15：函数拼写错误
# ===========================================
# ❌ random.randit()   for i in tange()
# ✅ random.randint()   for i in range()


# ===========================================
# 错题 16：print 和 return 混用
# ===========================================
# ❌ 函数内用 print() 而非 return
# 原因：print 只显示不传值；return 把值传回调用处，外面可以接着用
# |        | print         | return        |
# |--------|---------------|---------------|
# | 作用   | 屏幕显示      | 值传回调用处   |
# | x=f()  | x = None      | x = 值        |
# ✅ 函数内用 return


# ===========================================
# 错题 17：*args 返回了元组而非结果
# ===========================================
# ❌ def sum_all(*args): return args   # 返回元组
# ✅ def sum_all(*args): return sum(args)


# ===========================================
# 错题 18：作用域 — 函数内赋值不影响全局
# ===========================================
# x = 10
# def change(): x = 20
# change()
# print(x)   # 10，不是 20！
# 原因：函数内 x=20 创建局部变量，外部 x 不变


# ===========================================
# 错题 19：列表嵌套字典的数据结构
# ===========================================
# ❌ [{ "name":"张三","score":88, "name":"李四","score":95 }]
# 原因：一个字典里键重复会覆盖，只剩最后一个人
# ✅ [
#     {"name":"张三","score":88},
#     {"name":"李四","score":95},
# ]


# ===========================================
# 错题 20：map 返回对象需 list() 转换
# ===========================================
# ❌ map(lambda x:x*2, nums) → 得到 map 对象
# ✅ list(map(lambda x:x*2, nums))


# ===========================================
# 错题 21：filter 条件写反了
# ===========================================
# ❌ filter(lambda x:x%2, nums)  → x%2 非零为真，筛出的竟是奇数
# ✅ filter(lambda x:x%2==0, nums) → 明确写出条件


# ===========================================
# 错题 22：enumerate 解包取错
# ===========================================
# ❌ b = enumerate(names); for i in b: print(b)
# 原因：enumerate 每次给 (索引, 值) 元组，需解包
# ✅ for idx, name in enumerate(names, start=1): print(f"{idx}. {name}")


# ===========================================
# 错题 23：__init__ 拼写错误
# ===========================================
# ❌ def __int__(self):  或  def --init--(self):
# 原因：__init__ 是双下划线 init 双下划线，不是 int，也不是 --
# ✅ def __init__(self, ...):


# ===========================================
# 错题 24：类中方法忘记 self
# ===========================================
# ❌ def running():    # 忘记 self
# 原因：实例方法第一个参数必须是 self，才能访问实例属性
# ✅ def running(self):


########## 第三部分：面向对象 & FastAPI & 数据库 知识点 ##########

"""
【17. 面向对象核心概念】
- 类(class)：对象的模板，定义属性和方法
- 对象(实例)：根据类创建的具体实体
- self：代表实例自身，实例方法的第一个参数
- __init__：初始化方法，创建对象时自动调用（不是构造函数！）

【18. 类属性 vs 实例属性】
- 实例属性：__init__ 中用 self.xxx 定义，每个对象独立
- 类属性：直接定义在 class 下，所有对象共享同一份

【19. 常用魔术方法】
- __init__(self, ...)：初始化
- __str__(self)：print(对象) 时调用的字符串表示

【20. FastAPI 核心概念】
- 路径参数：@app.get("/book/{id}")，函数参数 id 自动提取
- 查询参数：?one=1&two=2，函数参数名匹配即可
- Path()：路径参数校验（ge, le, min_length 等）
- Query()：查询参数校验（default, ge, le）

【21. Pydantic 数据模型】
- class User(BaseModel)：定义请求/响应数据结构
- Field()：添加校验和描述
- FastAPI 自动校验 POST 请求体的 JSON

【22. 依赖注入 Depends】
- async def common_params(...): 定义可复用的参数逻辑
- Depends(common_params) 注入到路由，避免代码重复

！！！orm全流程
1.前推
首先需要创建会话工厂 会话工厂由引擎，异步会话类 AsyncSession,异步会话工厂创造函数async_sessionmaker,
构成结构如下
sessionlocal =async_sessionmaker(engine,class_ =AsyncSession,expire_on_commit=False) 
expire_on_commit=False ：会话已加载对象数据不会过期

引擎engine 由异步会话引擎创造函数创造 结构如下
engine = creat_async_engine(url,echo =True)

url指连接数据库地址格式如下
首先需要url 数据库连接地址 url = “dialect+driver://user:password@host:port/database”












ss

















【23. 中间件 Middleware】
- @app.middleware("http")：在请求前后执行
- request → 中间件1 → 中间件2 → 路由 → 中间件2 → 中间件1 → response

【24. SQLAlchemy 异步 ORM】
- create_async_engine()：创建异步数据库引擎
- DeclarativeBase：ORM 基类
- Mapped / mapped_column：类型安全的列定义
- pool_size / max_overflow：连接池配置

【25. 迭代器 Iterator】☆☆☆ 新增
- 核心：for 循环的底层就是 iter() + next() + StopIteration
- iter(对象)：把可迭代对象变成迭代器，内部调 __iter__()
- next(迭代器)：取下一个元素，内部调 __next__()
- StopIteration：特殊的"信号异常"，告诉 for 循环"到头了"，不是真正的错误

【26. for 循环的底层真相】
  for x in obj:          ← 你写的
      print(x)
  
  等价于：
  it = iter(obj)         ← 调 __iter__()
  while True:
      try:
          x = next(it)   ← 反复调 __next__()
          print(x)
      except StopIteration:  ← 收到信号就停
          break

  关键结论：for 循环没有自己的专属通道，底层就是反复调 next()

【27. 自定义迭代器 — 类中实现两个魔术方法】
  class Counter:
      def __init__(self, start, end):
          self.current = start
          self.end = end

      def __iter__(self):
          return self          # 返回迭代器，通常就是自己

      def __next__(self):
          if self.current > self.end:   # 到头了
              raise StopIteration       # 发信号给 for
          result = self.current
          self.current += 1
          return result

  for n in Counter(1, 5): print(n)  # 1 2 3 4 5

【28. 迭代器执行流程图】
  创建对象 Counter(1,5) → 仅触发 __init__
         ↓
  for 循环开始 → 自动调 iter() → 触发 __iter__() → 返回 self
         ↓
  第1次循环 → 调 next() → 触发 __next__() → 返回 1, current=2
  第2次循环 → 调 next() → 触发 __next__() → 返回 2, current=3
  ...
  第6次循环 → 调 next() → 触发 __next__() → current>end → raise StopIteration
         ↓
  for 收到 StopIteration → 安静结束，不报错

【29. break vs raise StopIteration】
  - break：只能从所在循环跳出，__next__ 里没有循环，不能用 break
  - raise StopIteration：往"外面"抛信号，让调用者（for 循环）自己停
  - 本质：一个管"内部跳出"，一个管"跨层通信"

【30. 魔术方法调用时机总结】
  | 你写的代码   | Python 背后做的    | 什么时候触发            |
  |-------------|-------------------|----------------------|
  | obj = C(1,5)| __init__(obj,1,5) | 创建对象时             |
  | iter(obj)   | obj.__iter__()    | for开始 / 手动调iter() |
  | next(obj)   | obj.__next__()    | for每次循环 / 手动调next() |
  ★ 魔术方法不是"自动跑"，而是"某操作触发后Python去找它"

【31. 外键 ForeignKey — 数据库层面的关联】
- ForeignKey("users.id")：规定本表的某个字段值，必须是另一张表里存在的 id
- 格式：Column(Integer, ForeignKey("表名.字段名"))
- "users.id" 是字符串，表名来自 __tablename__，不是类名
- 作用：防乱填，保证数据完整性
- 例子：user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

【32. relationship — Python 层面的快捷通道】
- 外键是"地基"，relationship 是"电梯"——两者配合使用
- 格式：变量名 = relationship("模型类名", back_populates="对面的变量名")
- "User" 是模型类名（大写），不是表名（小写）
- 双向绑定：两张表各写一个 relationship，用 back_populates 连起来
- 例子：
  # member.py 里
  owner = relationship("User", back_populates="members")
  
  # users.py 里
  members = relationship("Member", back_populates="owner")

【33. filter + first — 查询数据】
- query(模型).filter(条件).first() 执行流程：
  ① query(Member)  → 查 members 表
  ② .filter(Member.id == 1)  → 条件：id 等于 1
  ③ .first()  → 真正执行查询，返回第一条结果（或 None）
- filter() 只是准备查询，还没执行
- first() 才真正跑数据库，取一条
- all() 取全部，返回列表

【34. 外键 ForeignKey 必须指向主键】
- 外键只能指向对方表的主键（通常是 id），不能指向 name 等其他字段
- 原因：主键唯一（不会重复）且不变（不改名），外键关系不会断裂
- 例子：member_id = Column(Integer, ForeignKey("members.id")) ✅
- 错误：name = Column(Integer, ForeignKey("users.name")) ❌ — 名字可能重名或改名

【35. back_populates — 双向关联的"对讲机"】
- back_populates 指向的是对面模型的 relationship 属性名，不是 Column 字段名
- Column（字段）= 数据
- relationship（绳子）= 快捷通道
- 例子：
  # user.py
  member = relationship("Member", back_populates="owner")  # 去 Member 找叫 owner 的绳子
  
  # member.py
  owner = relationship("User", back_populates="member")     # 去 User 找叫 member 的绳子
- 只有两边都写了 relationship + back_populates，才算双向绑定

【36. select + where — 新式查询语法】
- select(模型).where(模型.字段 == 值) 相当于 SQL: SELECT * FROM 表 WHERE 字段 = 值
- select(User) 查的是整行（所有字段），不是单个字段
- 查到的结果用 .scalar_one_or_none() 提取：
  → 查到 → 返回一个模型对象（如 User 对象，有 .id .username .password）
  → 没查到 → 返回 None
- await session.execute(...) 把查询发给数据库并等待结果

【37. 字段名要见名知义】
- 存什么就叫什么：
  - member_id → 存的是 member 的 id ✅
  - name → 一看以为是名字，但存的是数字 ❌
  - title → 故事的标题 ✅
  - created_at → 发布时间 ✅

【38. bcrypt 密码哈希与 verify 原理】
- hash_password("123456") 每次生成的结果都不同（因为加了随机盐值）
- verify_password(明文, hash) 内部流程：
  ① 从 hash 里提取盐值
  ② 用该盐值重新加密明文
  ③ 比对新的 hash 跟数据库存的 hash 是否一致
- 本质上就是"重新加密一次再比对"
- 返回 True（匹配）或 False（不匹配）

【39. Depends 依赖注入】
- Depends(函数) = 让 FastAPI 自动调用该函数，把返回值注入到路由参数
- 用于注入数据库会话：session: AsyncSession = Depends(get_db)
- 不需要手动 async with SessionLocal()
- FastAPI 自动管理：请求来 → 调 get_db() → yield session → 路由用 → 自动关闭

【40. 注册/登录流程】
- 注册：查用户 → 不存在 → hash_password → create User → session.add → commit → 跳转
- 登录：查用户 → 没找到 → "用户不存在" → 找到了 → verify_password → 不对 → "密码错误" → 对了 → 存 session → 跳转


print("=" * 50)
print("知识点速查 + 错题本(24道) 整合完毕")
print("包含：基础语法 → 数据结构 → 函数 → lambda/文件 → 面向对象 → 迭代器 → FastAPI → 数据库 → ORM外键 → 路由与认证")
print("=" * 50)
"""
