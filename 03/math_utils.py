def add(a, b):
    """加法函数"""
    return a + b


def multiply(a, b):
    """乘法函数"""
    return a * b


PI = 3.14159

# Python没有默认导出的概念，但可以定义__all__来控制from module import * 的行为
__all__ = ["add", "multiply", "PI"]
