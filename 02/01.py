# 直接赋值，无需声明关键字
name = "张三"
age = 25

# 解构赋值
first, second = 1, 2
user_info = {"name": "李四", "age": 30}
user_name, user_age = user_info["name"], user_info["age"]

# 更优雅的解构方式
user_info = {"name": "王五", "age": 28}
user_name, user_age = user_info.values()

# f-string
message = f"你好，{name}! 你今年{age}岁。"
print(message)
