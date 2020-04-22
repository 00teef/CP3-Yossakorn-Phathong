username = "owner"
password = "555"
print("Welcome to 7-11=-4 Shop")
Account_already = input("1.for login 2.for singup: ")
if   Account_already    == "1" :
    print("please enter your usename and password")
    userlongin = input("username: ")
    passwordlogin   = input("password: ")
    if userlongin == username and passwordlogin == password:
        print("Our Products")
        print("1.Banana:" , 9  ,"THB")
        print("2.Rice  :" , 15 ,"THB")
        print("3.Milk  :" , 12 ,"THB")
        buy = input("select product: ")
        if   buy == "1":
             piece = int(input("Banana: "))
             result = 9*piece
             buymore = int(input("press 1.for buymore 2.for not: "))
             if buymore == 1:
                buy = input("select product 1.for rice 2.for milk: ")
                if   buy == "1":
                 piece2 = int(input("Rice: "))
                 result += 15 * piece2
                 buymore2 = int(input("press 1.for buy milk 2.for not: "))
                 if buymore2 == 1:
                     piece = int(input("Milk: "))
                     result += 12*piece
                     print("Total: ",result,"THB")
                 else:
                     print("Total: ",result,"THB")
                elif buy == "2":
                    piece2 = int(input("Milk: "))
                    result += 15 * piece2
                    buymore2 = int(input("press 1.for buy rice 2.for not: "))
                    if buymore2 == 1:
                        piece = int(input("Rice: "))
                        result += 15 * piece
                        print("Total: ", result, "THB")
                    else:
                        print("Total: ", result, "THB")
                else:
                    print("Total: ",result,"THB")
             else:
                 print("Total: ",result,"THB")
        elif buy == "2":
            piece = int(input("Rice: "))
            result = 15 * piece
            buymore = int(input("press 1.for buymore 2.for not: "))
            if buymore == 1:
                buy = input("select product 1.for banana 2.for milk: ")
                if buy == "1":
                    piece2 = int(input("Banana: "))
                    result += 9 * piece2
                    buymore2 = int(input("press 1.for buy milk 2.for not: "))
                    if buymore2 == 1:
                        piece = int(input("Milk: "))
                        result += 12 * piece
                        print("Total: ", result, "THB")
                    else:
                        print("Total: ", result, "THB")
                elif buy == "2":
                    piece2 = int(input("Milk: "))
                    result += 15 * piece2
                    buymore2 = int(input("press 1.for buy rice 2.for not: "))
                    if buymore2 == 1:
                        piece = int(input("Rice: "))
                        result += 15 * piece
                        print("Total: ", result, "THB")
                    else:
                        print("Total: ", result, "THB")
                else:
                    print("Total: ", result, "THB")
            else:
                print("Total: ", result, "THB")
        elif buy == "3":
            piece = int(input("Milk: "))
            result = 12 * piece
            buymore = int(input("press 1.for buymore 2.for not: "))
            if buymore == 1:
                buy = input("select product 1.for rice 2.for banana: ")
                if buy == "1":
                    piece2 = int(input("Rice: "))
                    result += 15 * piece2
                    buymore2 = int(input("press 1.for buy banana 2.for not: "))
                    if buymore2 == 1:
                        piece = int(input("Banana: "))
                        result += 9 * piece
                        print("Total: ", result, "THB")
                    else:
                        print("Total: ", result, "THB")
                elif buy == "2":
                    piece2 = int(input("Banana: "))
                    result += 9 * piece2
                    buymore2 = int(input("press 1.for buy rice 2.for not: "))
                    if buymore2 == 1:
                        piece = int(input("Rice: "))
                        result += 15 * piece
                        print("Total: ", result, "THB")
                    else:
                        print("Total: ", result, "THB")
                else:
                    print("Total: ", result, "THB")
            else:
                print("Total: ", result, "THB")

    else:
        print("Incorrect username or password")
elif Account_already    == "2" :
    username = input("create your username: ")
    password = input("create your password: ")
    print("Done !"
          "your username is: ", username,
          "your password is :", password, )
    print("Please enter your username and password")
    userlongin = input("username: ")
    passwordlogin = input("password: ")
    if userlongin == username and passwordlogin == password:
        print("please enter your usename and password")
        userlongin = input("username: ")
        passwordlogin = input("password: ")
        if userlongin == username and passwordlogin == password:
            print("Our Products")
            print("1.Banana:", 9, "THB")
            print("2.Rice  :", 15, "THB")
            print("3.Milk  :", 12, "THB")
            buy = input("select product: ")
            if buy == "1":
                piece = int(input("Banana: "))
                result = 9 * piece
                buymore = int(input("press 1.for buymore 2.for not: "))
                if buymore == 1:
                    buy = input("select product 1.for rice 2.for milk: ")
                    if buy == "1":
                        piece2 = int(input("Rice: "))
                        result += 15 * piece2
                        buymore2 = int(input("press 1.for buy milk 2.for not: "))
                        if buymore2 == 1:
                            piece = int(input("Milk: "))
                            result += 12 * piece
                            print("Total: ", result, "THB")
                        else:
                            print("Total: ", result, "THB")
                    elif buy == "2":
                        piece2 = int(input("Milk: "))
                        result += 15 * piece2
                        buymore2 = int(input("press 1.for buy rice 2.for not: "))
                        if buymore2 == 1:
                            piece = int(input("Rice: "))
                            result += 15 * piece
                            print("Total: ", result, "THB")
                        else:
                            print("Total: ", result, "THB")
                    else:
                        print("Total: ", result, "THB")
                else:
                    print("Total: ", result, "THB")
            elif buy == "2":
                piece = int(input("Rice: "))
                result = 15 * piece
                buymore = int(input("press 1.for buymore 2.for not: "))
                if buymore == 1:
                    buy = input("select product 1.for banana 2.for milk: ")
                    if buy == "1":
                        piece2 = int(input("Banana: "))
                        result += 9 * piece2
                        buymore2 = int(input("press 1.for buy milk 2.for not: "))
                        if buymore2 == 1:
                            piece = int(input("Milk: "))
                            result += 12 * piece
                            print("Total: ", result, "THB")
                        else:
                            print("Total: ", result, "THB")
                    elif buy == "2":
                        piece2 = int(input("Milk: "))
                        result += 15 * piece2
                        buymore2 = int(input("press 1.for buy rice 2.for not: "))
                        if buymore2 == 1:
                            piece = int(input("Rice: "))
                            result += 15 * piece
                            print("Total: ", result, "THB")
                        else:
                            print("Total: ", result, "THB")
                    else:
                        print("Total: ", result, "THB")
                else:
                    print("Total: ", result, "THB")
            elif buy == "3":
                piece = int(input("Milk: "))
                result = 12 * piece
                buymore = int(input("press 1.for buymore 2.for not: "))
                if buymore == 1:
                    buy = input("select product 1.for rice 2.for banana: ")
                    if buy == "1":
                        piece2 = int(input("Rice: "))
                        result += 15 * piece2
                        buymore2 = int(input("press 1.for buy banana 2.for not: "))
                        if buymore2 == 1:
                            piece = int(input("Banana: "))
                            result += 9 * piece
                            print("Total: ", result, "THB")
                        else:
                            print("Total: ", result, "THB")
                    elif buy == "2":
                        piece2 = int(input("Banana: "))
                        result += 9 * piece2
                        buymore2 = int(input("press 1.for buy rice 2.for not: "))
                        if buymore2 == 1:
                            piece = int(input("Rice: "))
                            result += 15 * piece
                            print("Total: ", result, "THB")
                        else:
                            print("Total: ", result, "THB")
                    else:
                        print("Total: ", result, "THB")
                else:
                    print("Total: ", result, "THB")

        else:
            print("Incorrect username or password")
    else:
        ("Error: Incorrect username or password")
else:
    print("Error: Please press only 1 or 2")