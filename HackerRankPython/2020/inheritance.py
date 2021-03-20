class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, score):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        gpa = sum(self.scores) / len(scores)

        if 100 >= gpa >= 90:
            return 'O'
        elif 90 > gpa >= 80:
            return 'E'
        elif 80 > gpa >= 70:
            return 'A'
        elif 70 > gpa >= 55:
            return 'P'
        elif 55 > gpa >= 40:
            return 'D'
        elif 40 > gpa:
            return 'T'

line = ['Mike', 'H', '1234']
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = [100, 35, 0, 73]
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())