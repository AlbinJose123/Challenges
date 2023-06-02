class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
student = Student()
student.setName("Albin")
student.setRollNumber("20212")

name = student.getName()
rollNumber = student.getRollNumber()
print(name) 
print(rollNumber)  
