filename= 'alice.txt'
with open(filename,'w') as f_obj:
    f_obj.write("Alice in wonderland")

try:
    with open(filename) as f_obj2:
        contents=f_obj2.read()
except FileNotFoundError:
    msg=("Sorry, the file "+filename+" does not exist!")
    print(msg)
else:
    # 计算文件包含多少个单词
    words=contents.split()   # split()以空格为分隔符，将字符串分拆，创建一个列表，
    num_words=len(words)
    print(num_words)