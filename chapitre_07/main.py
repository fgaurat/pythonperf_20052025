from Rectangle import Rectangle
from RectangleSingleton import RectangleSingleton

def main():

    r1 = RectangleSingleton(1,2)
    print(r1)

    r2 = RectangleSingleton(3,4)
    print(r2)

    print(hex(id(r1)))
    print(hex(id(r2)))


    r1()
    r2()
    print(50*'------')
    r = Rectangle(1,2)
    r1 = Rectangle(3,4)
    # print(type(r))
    # print(type(Rectangle))
    print(hex(id(r)))
    print(hex(id(r1)))

if __name__ == '__main__':
    main()