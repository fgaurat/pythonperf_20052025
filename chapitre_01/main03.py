import copy

def main():
    l = [10,20,30,40,50]

    # size = len(l)
    # print(l[size-1])
    # print(l[-1])


    print(l[2])
    print(l[2:4]) # [2:4[
    print(l[4:])
    # print(l[:5])
    print(l[:])
    print(l)
    # l1 = l
    # l[0]=1000
    # print(l)  #[1000,20,30,40,50]
    # print(l1) # [10? 1000? ,20,30,40,50] 3 1000 / 1 10

    # l1 = l.copy()
    # l1 = l[:]
    l1 = copy.copy(l)
    l[0]=1000
    print(l)
    print(l1)
    print(50*'-')
    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]

    l1 = l[:] # marche pas (shallow)
    l1 = l.copy() # marche pas (shallow)
    l1 = copy.deepcopy(l) # Marche !     
    
    l[1][1] = 5000

    print(l)
    print(l1)



if __name__ == '__main__':
    main()