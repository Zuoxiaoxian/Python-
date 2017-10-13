#-*-coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import os
print '打印 文件路径..'

for root,dirs,files in os.walk("C:\Users\Administrator\Desktop\spider\\"):

    for name in files:
        print '文件名:', name
        print '文件路径:', (os.path.join(root,name))

