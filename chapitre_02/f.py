
def creerFonction():
    name = "Fred"
    
    def afficheNom():
        print(name)

    def calc():
        print(name)

    return afficheNom,calc


f,c = creerFonction() #     def afficheNom():
                    #       print(name)
f()
