class Class01:

    def __init__(self):
        print("Create an object on class01")


class Class02:

    def __init__(self):
        print("Create an object on class02")


# if __name__ == "__main__" can run only when you execute this modiul directly .
# this step cann't run if you import this modiul or you use this modiul other

def main():
    c1 = Class01()
    c2 = Class02()

if __name__ == "__main__":
    print("run current module directly.")
    main()
else:
    print("the module programe is imported in current directory.")

