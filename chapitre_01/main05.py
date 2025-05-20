# HelloWorld => PascalCase, UpperCamelCase
# helloWorld => camelCase 
# hello_world => snake_case
# hello-world => kebab-case, train-case, spin-case




# a, b sont positionnels
def f(a,b): 
    print(a,b)


f(4,5)
f(a=4,b=5) # a,b sont passés par keywords
f(b=5,a=4) # a,b sont passés par keywords


def add(*the_list): # the_list est un tuple qui rassemble les paramètres passés par position
    result = 0
    print(the_list)
    for num in the_list:
        result += num

    # # result = sum(the_list))
    return result


# def hello(name:str,first_name:str)->None:
def hello(**d)->None: # d est un dictionnaire qui rassemble les paramètres passés par keywords
    """
    Ceci est un docstring
    sur plusieurs lignes
    """
    print(d['name'],d['first_name'])

def main():
    # region test args
    # AAA

    # Arrange
    l = [10,20,30,40,50]
    
    # Act
    # result = add(l)
    
    # Assert
    # assert result == 151
    # print(result) # 150

    # Act
    # result = add(10,20,30,40,50)
    result = add(*l)
    print(result)
    # print("toto")
    # print("toto",123)
    # print("toto",123,False)

    a,*c = [1,2,3,4,5,6,7,8,9]
    
    print(a,c)
    print(*c,sep="-")
    
    #L_VALUE a = 1 # R_VALUE
    #endregion


    d = {
        "first_name":"Fred",
        "name":"GAURAT"
    }
    # hello("GAURAT","Fred")
    hello(**d)
    hello(first_name="Fred",name="GAURAT")


if __name__ == '__main__':
    main()