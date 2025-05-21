import calc
import types
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Appel de {func.__name__} avec {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Résultat de {func.__name__} = {result}")
        return result
    return wrapper


def main():
    
    # Décoration dynamique de toutes les fonctions du module
    for nom, obj in vars(calc).items():
        if isinstance(obj, types.FunctionType):
            setattr(calc, nom, log(obj))
    
    calc.addition(2, 3)
    calc.multiplication(4, 5)
if __name__ == '__main__':
    main()