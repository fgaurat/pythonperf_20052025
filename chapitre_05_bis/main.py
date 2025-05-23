from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo


def showSurface(o:ICalcGeo):
    print("showSurface",o.surface)

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

    showSurface(c)
    showSurface(ce)

if __name__ == '__main__':
    main()