# 使用try-except代码块，处理ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print('you can not divide by zero!')