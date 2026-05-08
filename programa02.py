#-*-coding:utf8;-*-

import os
import time

x = 0
buffer = "°....................."
while(x < 1000):
    for i in range(len(buffer)):
        n = buffer.index("°")
        print(n)
        buffer = buffer.replace("°",".")[1]
        buffer = "°" + buffer[n:]
        #os.system("clear")
        print(buffer+"  ",end="",flush=True)
        time.sleep(0.1)

    """
    os.system("clear")
    print(".°.  ",end="",flush=True)
    time.sleep(0.1)
    os.system("clear")
    print("..°  ",end="",flush=True)
    time.sleep(0.1)
    os.system("clear")
    print("...  ",end="",flush=True)
    """

    x = x + 1
