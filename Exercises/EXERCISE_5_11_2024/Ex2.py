import random
def zad2():
    length = int(input("Input length: "))
    ll = []
    for i in range(length):
        num = random.randint(1, 10)
        ll.append(num)
    print(f"Original list : {ll}")

    new_list = list()
    for i in range(len(ll) - 1):
        new_list.append(ll[i])
        new_list.append(ll[i] + ll[i + 1])
    new_list.append(ll[-1])
    print(f"Modified list: {new_list}")

zad2()