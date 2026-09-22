# Python 包的使用

# 1. 从包导入特定函数
from my_package import add, multiply

# 2. 导入整个包
import my_package

# 3. 从子模块导入
from my_package.string_utils import capitalize

print(add(5, 3))
print(my_package.multiply(4, 2))
print(capitalize("hello"))
