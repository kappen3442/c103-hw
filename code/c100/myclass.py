class Student:
    def __init__(self,name,rollnumber,grade,age):
        self.name=name
        self.rollnumber=rollnumber
        self.grade=grade
        self.age=age

    def displaymarks(self):
        print("these are my marks")
    def displaygrade(self):
        print("grades displayed")

aaron=Student(name="Aaron",rollnumber=7,grade=9,age=14)
print(aaron.name)
print(aaron.rollnumber)
print(aaron.grade)
print(aaron.age)

aaron.displaymarks()
aaron.displaygrade()