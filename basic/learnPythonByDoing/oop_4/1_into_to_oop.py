my_student = {
        'name' : 'Rakib Hasan',
        'greads' : [70,80,90,99]
        }

avrage_greads = sum(my_student['greads']) / 4
print('simple average grade : ', avrage_greads)


def average_grade(student):
    return sum(student['greads']) / len(student['greads'])
print(my_student['name'] , ' : ' , average_grade(my_student))



print("""
      """)



class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
        
    def average(self):
        return sum(self.grades) / len(self.grades)
    
student_one = Student('Rakib', [70,80,90,99])
student_two = Student('Rasid', [135,465,465,84,67,866,45])


print(student_one.name)
print(student_one.average())

print(student_two.name)
print(student_two.grades)
print(Student.average(student_two))


print("""
      """)


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
matrix = Movie('The Matrix', 1994)
print(matrix.name)


