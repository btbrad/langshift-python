# 基本错误处理
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError as e:
    print(f"发生错误：{e}")
except Exception as e:
    print(f"其他错误： {e}")
else:
    print("没有异常时执行")
finally:
    print("总是执行")


# 自定义异常
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# 抛出异常
def divide(a, b):
    if b == 0:
        raise CustomError("除数不能为零")
    return a / b


try:
    print(divide(10, 0))
except CustomError as e:
    print(f"除法错误：{e.message}")
