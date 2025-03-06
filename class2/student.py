#Create Student and Teacher classes 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class Teacher(Person):
    def __init__(self, name, age,):
        super().__init__(name, age)


student = Student("Alice", 20,)
teacher = Teacher("Bob", 45)
student.display()
teacher.display()
