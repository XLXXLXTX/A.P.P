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

    def error_handler():
        print("Action not supported")

    option = int(input("Enter an option between 1 and 5: "))

    actions = {1 : fun_one, 2 : fun_two, 3 : fun_three, 4 : fun_four, 5 : fun_five}

    action = actions.get(option, error_handler)
    action()