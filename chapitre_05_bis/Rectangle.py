class Rectangle:

    def __init__(self,longueur,largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    @property
    def longueur(self):
        """
        Propriété longueur
        """
        return self.__longueur
    
    @longueur.setter
    def longueur(self,longueur):
        assert longueur >0
        self.__longueur = longueur

    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self,largeur):
        assert largeur >0
        self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__largeur * self.__longueur
    

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Rectangle):
            return NotImplemented

        return self.longueur == value.longueur and self.largeur == value.largeur

    def __str__(self):
        return f"{self.__class__.__name__} {self.longueur=}, {self.largeur=}"