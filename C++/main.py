import random
from os import popen, system

system('g++ slow.cpp -o slow.exe')
system('g++ fast.cpp -o fast.exe')

while True:
    n = random.randint(1, int(1e1))
    arr = ''
    for i in range(n):
        arr = arr + str(random.randint(-100, 100)) + ' '

    test = str(n) + '\n' + arr
    slow = popen("echo {} | slow.exe".format(test)).read()
    fast = popen("echo {} | fast.exe".format(test)).read()

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
