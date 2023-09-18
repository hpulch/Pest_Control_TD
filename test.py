class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = []
students_to_remove = []
print(students)

students.append(Student("Alex", 20))
students.append(Student("Bob", 21))
students.append(Student("Alex", 20))
students.append(Student("Bob", 21))

for person in students:
    student_to_remove = students_to_remove.append(person)


count = 0
for person in students_to_remove:
    count = count + 1
    print("loop number: {}".format(count))
    print("###")
    print("List length: {}".format(len(students_to_remove)))
    print("###")
    print(students)
    students.remove(person)
    print("###")
    print(students)
    print("###")
    print("-------------")



