
def make_incrementor(i:int): # 10


    def the_function(v:int): #5
        return i+v
    
    return the_function



def main():
    do_inc = make_incrementor(10)
    r = do_inc(5)
    print(r) # 15

    r = do_inc(2)
    print(r) # 12



if __name__ == '__main__':
    main()