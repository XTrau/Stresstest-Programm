import random
from os import popen, system

system('g++ slow.cpp -o slow.exe')
system('g++ fast.cpp -o fast.exe')

while True:
    n = random.randint(1, 100)

    # ...

    test = str(n) + '\n'
    slow = popen("echo {} | slow.exe".format(test)).read()
    fast = popen("echo {} | fast.exe".format(test)).read()

    if slow == fast:
        print("OK\n", slow, fast, sep='')
        # print("test:\n", test, sep='')
    else:
        print("FAIL")
        print("test:\n", test, sep='')
        print("slow:\n", slow, sep='')
        print("fast:\n", fast, sep='')
        break
