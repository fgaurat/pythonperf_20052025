def main():
    l = [10,20,30,40,50]
    to_find =300

    # found = False

    for i in l:
        print(i)
        if i == to_find:
            print("ok")
            found = True
            break
    else:
        print("pas ok")
    
    
    # if found:
    #     print("trouvé")
    # else:
    #     print("pas trouvé")

if __name__ == '__main__':
    main()