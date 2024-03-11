import math
import numpy as np
import curses
from curses import wrapper

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
    def __init__(self, id, name, credits):
        self.__CourseID = id
        self.__CourseName = name
        self.__Credits = credits
    def getID(self):
        return self.__CourseID    
    def getName(self):
        return self.__CourseName
    def getCredits(self):
        return self.__Credits
    
class StudentList:
    def __init__(self): 
        self.__lst_student = []
    def InputStudent(self, stdscr):
        curses.echo()
        # stdscr.addstr("\n")
        stdscr.addstr("Please enter number of students in your class...", curses.color_pair(2))
        stdscr.refresh()
        num_of_student = stdscr.getstr(5)
        num_of_student = int(num_of_student)
        for i in range(num_of_student):
            stdscr.addstr("\n")
            stdscr.addstr(f"Student {i+1}:\n")

            stdscr.addstr("    Input StudentID: ")
            stdscr.refresh()
            id = stdscr.getstr(20) #.decode('utf-8')
            stdscr.addstr("\n")

            stdscr.addstr("    Input StudentName: ")
            stdscr.refresh()
            name = stdscr.getstr(30)#.decode('utf-8')
            stdscr.addstr("\n")

            stdscr.addstr("    Input DoB: ")
            stdscr.refresh()
            dob = stdscr.getstr(20) #.decode('utf-8')

            stdscr.clear()
            student = Student(id, name, dob)
            self.__lst_student.append(student)
        return self.__lst_student
    def ShowStudentList(self, stdscr):
        stdscr.addstr("Your student list: \n", curses.color_pair(2))
        for i in range(len(self.__lst_student)):
            stdscr.refresh()
            stdscr.addstr(f"    Student {i+1}:\n", curses.color_pair(1))
            stdscr.addstr(f"        ID: ", curses.color_pair(3))
            stdscr.addstr(f"{self.__lst_student[i].getID().decode('utf-8')}\n")
            stdscr.addstr(f"        Name: ", curses.color_pair(3))
            stdscr.addstr(f"{self.__lst_student[i].getName().decode('utf-8')}\n")
            stdscr.addstr(f"        DoB: ", curses.color_pair(3))
            stdscr.addstr(f"{self.__lst_student[i].getDoB().decode('utf-8')}\n")

class CourseList:
    def __init__(self):
        self.__lst_course = []
    def InputCourse(self, stdscr):
        curses.echo()
        stdscr.addstr("\n")
        stdscr.addstr("Please enter number of courses...", curses.color_pair(2))
        num_of_course = stdscr.getstr(5)
        num_of_course = int(num_of_course)
        for i in range(num_of_course):
            stdscr.addstr("\n")
            stdscr.addstr(f"Course {i+1}:\n")
            stdscr.addstr("    Input CourseID: ")
            stdscr.refresh()
            id = stdscr.getstr(10)
            stdscr.addstr("\n")

            stdscr.addstr("    Input CourseName: ")
            stdscr.refresh()
            name = stdscr.getstr(15)
            stdscr.addstr("\n")

            stdscr.addstr("    Input CourseCredits: ")
            stdscr.refresh()
            credits = int(stdscr.getstr(5))
            # stdscr.addstr("\n")
            stdscr.clear()
            course = Course(id, name, credits)
            self.__lst_course.append(course)
        return self.__lst_course
    def ShowCourseList(self, stdscr):
        stdscr.addstr("Your course list: \n", curses.color_pair(2))
        for i in range(len(self.__lst_course)):
            stdscr.addstr(f"    Course {i+1}: \n", curses.color_pair(1))
            stdscr.addstr("        ID: ", curses.color_pair(3)) 
            stdscr.addstr(f"{self.__lst_course[i].getID().decode('utf-8')}\n")
            stdscr.addstr("        Name: ", curses.color_pair(3))
            stdscr.addstr(f"{self.__lst_course[i].getName().decode('utf-8')}\n")
            stdscr.addstr("        Credits: ", curses.color_pair(3))
            stdscr.addstr(f"{self.__lst_course[i].getCredits()}\n")

def InputMark(stdscr, lst_student, lst_course):
    for i in range(len(lst_student)):
        mark_arr = np.array([])
        stdscr.addch("\n")
        for j in range(len(lst_course)):
            stdscr.addstr(f"Input the mark in {lst_course[j].getName().decode('utf-8')} for Student {i+1}...")
            mark = stdscr.getstr(5)
            mark = float(mark)
            mark_arr = np.append(mark_arr, (math.floor(mark)))       # use "math" module: floor() and use np.array
        lst_student[i].mark = mark_arr
        stdscr.clear()
    return lst_student

def ShowMark(stdscr, lst_student, lst_course):
    stdscr.addch("\n")
    stdscr.addstr("Your mark list:\n", curses.color_pair(2))
    stdscr.addstr(f"                ")
    for j in range(len(lst_course)):
        stdscr.addstr(f"{lst_course[j].getName().decode('utf-8')}      ", curses.color_pair(3))
    stdscr.addch("\n")
    for i in range(len(lst_student)):
        stdscr.addstr(f"    Student {i+1}:")
        # stdscr.addch("\n")
        for j in lst_student[i].mark:
            stdscr.addstr(f"  {str(j)}  ")

def CalculateGPA(lst_student, lst_course):
    for student in lst_student:
        total_mark = 0
        total_credits = 0
        i = 0
        for course in lst_course:
            total_mark = total_mark + (student.mark[i] * course.getCredits())
            total_credits = total_credits + course.getCredits()
            i = i + 1
        if total_credits != 0:
            student.GPA = total_mark / total_credits
        else:
            student.GPA = 0
    return lst_student

def ShowGPA(stdscr, lst_student):
    stdscr.addstr("\n")
    stdscr.addstr("\nStudents GPA: \n", curses.color_pair(2))
    for i in range(len(lst_student)):
        stdscr.addstr(f"    Student {i+1} GPA: {lst_student[i].GPA}")
        
def Display(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    studentList = StudentList()
    courseList = CourseList()

    Students = studentList.InputStudent(stdscr)
    Courses = courseList.InputCourse(stdscr)
    student_mark = InputMark(stdscr, Students, Courses)
    student_gpa = CalculateGPA(student_mark, Courses)

    studentList.ShowStudentList(stdscr)
    courseList.ShowCourseList(stdscr)
    ShowMark(stdscr, student_mark, Courses)
    ShowGPA(stdscr, student_gpa)

    stdscr.refresh()
    stdscr.getch()
wrapper(Display)