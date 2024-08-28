'''Design a Python program to manage a student gradebook, providing functionality for
adding students, inputting their grades for various subjects, and calculating the average
grades for each student. Utilize dictionaries to store student information, including names
and corresponding lists to store grades for different subjects.'''

def addStudents(GradeBook):
    Student=dict()
    Student['name'] = input('enter the name of the student: ')
    Student['grades'] = list(map(int,input('enter student grades: ').strip()))
    print(Student['grades'])
    #Student['avggrade'] = sum(Student['grades'])/5
    GradeBook.append(Student)
GradeBook = []
while True:
    print("Welcome to Student GradeBooks")
    addStudents(GradeBook)
    ch = input("Do you want to continue entering Students?(y/n)")
    if ch=='n': break
    else: continue
print(GradeBook)
