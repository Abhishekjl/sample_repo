class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_grade(self):
        return sum(self.marks)/len(self.marks)






student = Student('Bob',[1,234,56,78])
print(student.average_grade())
print(student.name, student.marks)

# def average(sequence):
#     return sum(sequence)/len(sequence)



# print(average(student['grades']))    

