

class Rectangle:
    __slots__ = ("__longueur", "__largeur")

    #static
    __cpt = 0

    def __init__(self,longueur:int=1,largeur:int=1) -> None:
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle.__cpt+=1

    @classmethod
    def buildFromStr(cls,value):
        a,b = [int(v) for v in value.split(";")]
        return cls(a,b)

    @staticmethod
    def get_cpt():        
        return Rectangle.__cpt
    
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

    # def __int__(self):
    #     return self.surface