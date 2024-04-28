import random
from os import popen, system

while True:
    n = random.randint(1, 100)

    # ...

    test = str(n) + '\n'
    slow = popen("echo {} | python slow.py".format(test)).read()
    fast = popen("echo {} | python fast.py".format(test)).read()

    if slow == fast:
        print("test:")
        print(test)
        print("OK")
        print("fast: ")
        print(fast, end='')
        print("slow: ")
        print(slow, end='')
        print()
    else:
        print("test:")
        print(test)
        print("FAIL")
        print("fast: ")
        print(fast, end='')
        print("slow: ")
        print(slow, end='')
        print()
        break
