from functools import wraps

def do_log(file_log):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"LOG to {file_log}",args,kwargs)
            r = func(*args, **kwargs)
            print(f"LOG to {file_log} return",r)
            return r

        return wrapper
    return decorator

# @do_log
# def add(a,b):
#     return a+b

@do_log('file.log')
def say_hello(name:str)->str:
    """
    Dire bonjour à name
    """
    s = f"Bonjour {name}"
    return s

def main():
    h = say_hello("Fred")
    print(h)
    print(say_hello.__name__)
    print(say_hello.__doc__)

if __name__ == '__main__':
    main()