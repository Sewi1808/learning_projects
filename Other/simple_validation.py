z = []


def number_input():
    global a
    a = int(input("please provide number: \n"))
    if a in locals():
        print("no input detected \n")
        number_input()
    elif a == 0:
        print("provided number is 0, provide another one \n")
        number_input()
    else:
        return


def is_divided_by():
    b = int(a % 2)
    c = int(a % 5)
    d = int(a % 10)
    if b is 0:
        z.append("Is divided by 2")
    else:
        pass

    if c is 0:
        z.append("Is divided by 5")
    else:
        pass

    if d is 0:
        z.append("Is divided by 10")
    else:
        pass


def resolution():
    print(f"your number is:{a} and:\n {z}")


def execution():
    number_input()
    is_divided_by()
    resolution()


execution()
