import sys

def main():
    print(sys.getrefcount(254325342345353498))
    
    a = 254325342345353498
    print(sys.getrefcount(254325342345353498))
    # b = 2
    # c = 2
    # d = 2

    # print(hex(id(a)))
    # print(hex(id(b)))
    # print(hex(id(c)))
    # print(hex(id(d)))

    # a = 3
    # print(hex(id(a)))


if __name__ == '__main__':
    main()
