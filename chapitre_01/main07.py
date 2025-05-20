def old_mult2(the_list):
    r = []
    for i in the_list:
        r.append(i*2)

    return r


def mult2(i):
    return i*2


def main():
    l = [10,20,30,40,50]

    # l2 = mult2(l)
    # l2 = map(mult2,l) # first class citizen
    
    l2 = list(map(lambda i:i*2,l)) # first class citizen
    
    print(l)
    print(l2)


if __name__ == '__main__':
    main()