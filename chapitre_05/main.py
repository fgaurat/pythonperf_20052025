from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(2)
    print(c.cote)
    print(c)
    print(c.surface)
    c.cote = 4
    print(c.surface)
    print(50*'-')
    ce = Cercle(2)
    print(ce.surface)

if __name__ == '__main__':
    main()