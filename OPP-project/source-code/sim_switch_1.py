if __name__ == "__main__":

    def fun_one():
        print("fun_one called")

    def fun_two():
        print("fun_two called")

    def fun_three():
        print("fun_three called")

    def fun_four():
        print("fun_four called")

    def fun_five():
        print("fun_five called")

    option = int(input("Enter an option between 1 and 5: "))

    if option == 1:
        fun_one()
    elif option == 2:
        fun_two()
    elif option == 3:
        fun_three()
    elif option == 4:
        fun_four()
    elif option == 5:
        fun_five()
    else:
        print("Action not supported")


