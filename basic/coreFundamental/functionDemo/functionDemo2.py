in3 = input("Enter 1 for triangle shape or press 2 for rectangle shape : ")
in3 = int(in3)


def calculate_triangle_area(a, b):
    area = (1 / 2) * a * b
    return area


def calculate_rectangle_area(a, b):
    area = a * b
    return area


if in3 == 1:
    in1 = int(input("Enter height : "))
    in2 = int(input("Enter weight : "))

    total = calculate_triangle_area(in1, in2)
    print("total triangle area : ", total)

elif in3 == 2:
    in1 = input("Enter height : ")
    in2 = input("Enter weight : ")
    in1 = int(in1)
    in2 = int(in2)

    total = calculate_rectangle_area(in1, in2)
    print("total rectangle area : ", total)

else:
    print("please type only 1 or 2 for specific perpase : ")
