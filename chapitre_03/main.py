import traceback

def div(a,b):
    return a/b

def call_div(a,b):
    r = div(a,b)
    print(r)
    return r

def main():

    try:
        a = 2
        # b = int(input('b: '))
        b = 0
        # c = a/b
        c = call_div(a,b)
        print(c)
    # except ZeroDivisionError as e:
    #     print('ZeroDivisionError',e)
    #     # traceback.print_exc()
    # except TypeError as e:
    #     print('TypeError',e)
    # except ValueError as e:
    #     print('ValueError',e)
    except Exception as e:
        print('Exception',e,type(e))
    else:
        print("pas d'erreur")
    finally:
        print("finally")

    print("fin du code")
if __name__ == '__main__':
    main()
