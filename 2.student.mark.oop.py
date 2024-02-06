class Student:
    def __init__(self, id , name , dob):
        self.__StudentID = id
        self.__StudentName = name
        self.__DoB = dob
    def getID(self):
        return self.__StudentID
    def getName(self):
        return self.__StudentName
    def getDoB(self):
        return self.__DoB

class Course:
    def __init__(self, id, name):
        self.__CourseID = id
        self.__CourseName = name
    def getID(self):
        return self.__CourseID    
    def getName(self):
        return self.__CourseName
    
class StudentList:
    def __init__(self):
        self.__lst_student = []
    def InputStudent(self):
        print("")
        num_of_student = int(input("Please enter number of students in your class..."))
        for i in range(num_of_student):
            print("")
            print(f"Student {i+1}:")
            id = str(input("Input StudentID: "))
            name = str(input("Input StudentName: "))
            dob = str(input("Input DoB: "))
            student = Student(id, name, dob)
            self.__lst_student.append(student)
        return self.__lst_student
    def ShowStudentList(self):
        # print(self.__lst_student)
        print("Your student list: ")
        for i in range(len(self.__lst_student)):
            # print(f"Student {i+1}: ")
            print(f"ID: {self.__lst_student[i].getID()} Name: {self.__lst_student[i].getName()} DoB: {self.__lst_student[i].getDoB()}")

class CourseList:
    def __init__(self):
        self.__lst_course = []
    def InputCourse(self):
        print("")
        num_of_course = int(input("Please enter number of courses..."))
        for i in range(num_of_course):
            print("")
            print(f"Course {i+1}:")
            id = str(input("Input CourseID: "))
            name = str(input("Input CourseName: "))
            course = Course(id, name)
            self.__lst_course.append(course)
        return self.__lst_course
    def ShowCourseList(self):
        # print(self.__lst_course)
        print("Your course list: ")
        for i in range(len(self.__lst_course)):
            print(f"Course {i+1}: ")
            print(f"ID: {self.__lst_course[i].getID()} Name: {self.__lst_course[i].getName()}")


def InputMark(lst_student, lst_course):
    mark_student_dict = {}
    for i in range(len(lst_student)):
        mark_course_dict = {}
        print(f"")
        for j in range(len(lst_course)):
            mark = float(input(f"Input the mark in {lst_course[j].getName()} for Student {i+1}..."))
            mark_course_dict[f"{lst_course[j].getName()}"] = mark
        lst_student[i].mark = mark_course_dict
    return lst_student

def ShowMark(lst_student):
    print("")
    for i in range(len(lst_student)):
        print(f"Student {i+1}")
        print(lst_student[i].mark)

studentList = StudentList()
courseList = CourseList()
numOfStudent = studentList.InputStudent()
numOfCourse = courseList.InputCourse()

student_mark = InputMark(numOfStudent, numOfCourse)
ShowMark(student_mark)


        




