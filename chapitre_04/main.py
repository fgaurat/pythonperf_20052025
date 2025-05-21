from Rectangle import Rectangle

def main():
    r = Rectangle(100, 200) # création d'un objet


    print(r.get_longueur()) # 100 # lectures des propriétés
    r.set_longueur(12)
    print(r.get_longueur()) # 12
    print(r.get_surface()) # 2400



if __name__ == '__main__':
    main()