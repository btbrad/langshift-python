# 创建字典
person = {"name": "张三", "age": 25}

# 访问属性
print(person["name"])
print(person.get("name"))  # 安全访问
print(person.get("city", "未知"))  # 默认值

# 添加/修改属性
person["city"] = "北京"
person["job"] = "程序员"

# 删除属性
del person["age"]
person.pop("age", None)  # 安全删除

# 遍历字典
for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():
    print(f"{key}: {person[key]}")

for value in person.values():
    print(value)
