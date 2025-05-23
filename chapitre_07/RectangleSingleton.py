

from typing import Any


class RectangleSingleton:
    
    instance = None
    
    def __new__(cls,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self,longueur:int=1,largeur:int=1) -> None:
        self.__longueur = longueur
        self.__largeur = largeur
    

    def __call__(self) -> Any:
        print("__call__")


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
        if not isinstance(value, RectangleSingleton):
            return NotImplemented

        return self.longueur == value.longueur and self.largeur == value.largeur

    def __str__(self):
        return f"{self.__class__.__name__} {self.longueur=}, {self.largeur=}"