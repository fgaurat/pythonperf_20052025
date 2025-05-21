

class Rectangle:


    def __init__(self,longueur,largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self,longueur):
        assert longueur >0
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self,largeur):
        assert largeur >0
        self.__largeur = largeur
    
    def get_surface(self):
        return self.__largeur * self.__longueur