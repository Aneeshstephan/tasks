#5 class Person:

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Doctor(Person):
    def __init__(self, name, age, gender, specialization, hospital):
        super().__init__(name, age, gender)
        self.specialization = specialization
        self.hospital = hospital

    def display_details(self):
        super().display_details()
        print(f"Specialization: {self.specialization}")
        print(f"Hospital: {self.hospital}")


class Patient(Person):
    def __init__(self, name, age, gender, ailment, doctor):
        super().__init__(name, age, gender)
        self.ailment = ailment
        self.doctor = doctor

    def display_details(self):
        super().display_details()
        print(f"Ailment: {self.ailment}")
        print(f"Consulting Doctor: {self.doctor}")

doctor = Doctor("Dr. Smith", 45, "Male", "Cardiology", "City Hospital")
patient = Patient("Jane Doe", 32, "Female", "Heart Condition", "Dr. Smith")

print("Doctor Details:")
doctor.display_details()
print("\nPatient Details:")
patient.display_details()
