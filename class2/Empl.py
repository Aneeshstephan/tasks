#Employee 
class Employee:
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department 

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

    def manage_team(self):
        print(f"{self.name} is managing the {self.department} department")


class Developer(Employee):
    def __init__(self, name, employee_id,programming_language):
        super().__init__(name, employee_id)
        self.programming_language=programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}")


developer = Developer("aneesh", "D12345", "Python")
manager = Manager("john snow", "M12345", "Sales")

developer.display_details()
developer.write_code()

manager.display_details()
manager.manage_team()
