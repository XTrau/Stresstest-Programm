import random
from os import popen, system

while True:
    n = random.randint(1, 100)

    # ...

    test = str(n) + '\n'
    slow = popen("echo {} | slow.py".format(test)).read()
    fast = popen("echo {} | fast.py".format(test)).read()

    if slow == fast:
        print("OK\n", slow, fast, sep='')
        # print("test:\n", test, sep='')
    else:
        print("FAIL")
        print("test:\n", test, sep='')
        print("slow:\n", slow, sep='')
        print("fast:\n", fast, sep='')
        break
