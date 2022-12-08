# 使用异常避免崩溃，处理ZeroDivisionError异常
print("input two numbers,and divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond_number:")
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can not divide by 0!")
    else:
        print(answer)
