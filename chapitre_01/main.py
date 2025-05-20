


def add(the_list):
    result = 0
    for num in the_list:
        result += num
    return result


def main():
    # AAA

    # Arrange
    l = [10,20,30,40,50]
    
    # Act
    result = add(l)
    
    # Assert
    print(result) # 150

if __name__ == '__main__':
    main()