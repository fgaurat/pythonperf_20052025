from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    r = Rectangle(100, 200) # création d'un objet
    r1 = Rectangle(100, 200) # création d'un objet
    r2 = Rectangle() # création d'un objet
    r3 = Rectangle.buildFromStr("3;5") # création d'un objet
    print(Rectangle.get_cpt()) # 2
    print(r.get_cpt()) # 2
    print(r1.get_cpt()) # 2
    # Rectangle.get_cpt() = 1000
    # print(Rectangle.get_cpt()) # 2
    # print(r.get_cpt()) # 2
    # print(r1.get_cpt()) # 2

    # print(r3)
    # r3.toto = "une valeur"
    # print(r3.toto)


def old_main():
    r = Rectangle(100, 200) # création d'un objet

    # region old
    # print(r.get_longueur()) # 100 # lectures des propriétés
    # r.set_longueur(12)
    # print(r.get_longueur()) # 12
    # print(r.get_surface()) # 2400

    # r.longueur = 12 # r.set_longueur(12)
    # print(r.longueur) # print(r.get_longueur()) 
    # endregion

    print(r.longueur)
    # r.longueur = -12
    print(r.surface)
    # r.surface = 45
    print(50*'-')
    dr = DataRectangle(2,3)
    print(dr.surface)
    print(50*'-')
    r = Rectangle(100, 200)
    r1 = Rectangle(100, 200)
    if r==r1:
        print("ok")
    else:
        print("ko")
    print(50*'-')
    dr = DataRectangle(2,3)
    dr1 = DataRectangle(2,3)
    if dr==dr1:
        print("ok")
    else:
        print("ko")
    print(50*'-')
    print(r)
    print(dr)


if __name__ == '__main__':
    main()