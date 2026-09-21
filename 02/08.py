# for循环
for i in range(5):
    print(i)

# 遍历列表
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# 遍历字典
person = {"name": "张三", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")

# 只遍历键
for key in person:
    print(key)

# 只遍历值
for value in person.values():
    print(value)

# while循环
count = 0
while count < 5:
    print(count)
    count += 1

# 列表推导式
squares = [x**2 for x in range(5)]
print(squares)
