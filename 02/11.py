# 创建列表
arr = [1, 2, 3, 4, 5]

# 添加元素
arr.append(6)  # 末尾添加
arr.insert(0, 0)  # 开头添加
arr.insert(2, 2.5)  # 中间插入

# 删除元素
arr.pop()  # 删除末尾
arr.pop(0)  # 删除指定位置
del arr[2]  # 删除指定位置
arr.remove(3)  # 删除指定值
arr.insert(2, 3)  # 中间插入

# 查找元素
index = arr.index(3)  # 查找索引
found = next((x for x in arr if x > 3), None)

# 列表推导式
doubled = [x * 2 for x in arr]
filtered = [x for x in arr if x > 2]
sum_result = sum(arr)

print("原列表", arr)
print("翻倍", doubled)
print("过滤", filtered)
print("求和", sum_result)
