inport time   #加载时间模块
date = time.localtime()   #加载日期
print(dete)  #打印date信息
x = input('请输入你想写入text txt的内容:')  #引导用户输入写入内容
with open('text.txt') as f:
    f.write(x)    #在文件中写入用户输入的内容
    f.seek(0) 
    break
print('文件写出成功，快去查看吧！')
    
    
