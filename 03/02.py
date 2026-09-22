# Python模块特殊变量

# 当前文件路径
print(__file__)

# 模块名称
print(__name__)

# 模块文档字符串
print(__doc__)

# 控制 from module import * 的行为
# print(__all__)

# 判断是否为直接运行的文件
if __name__ == "__main__":
    print("这个文件被直接运行了")
else:
    print("这个文件被作为模块导入")
