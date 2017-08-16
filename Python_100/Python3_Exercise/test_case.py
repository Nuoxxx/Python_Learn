# coding = utf-8
import os
#运行程序并将运行的日志保存在log.txt中
caselist = os.listdir("D:\\unittest")
for a in caselist:
    s = a.split('.')[1]
    if s == 'py':
        # os.system('D:\\unittest\\%s 1>>log.txt 2>&1' %a)
        os.system('D:\\unittest\\%s' % a)
