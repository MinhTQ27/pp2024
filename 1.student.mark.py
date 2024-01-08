def StudentInfor():
    student_dict={'StudentID': 0, 'StudentName': 0, 'DoB': 0}
    for j in student_dict.keys():
        print(f"Please input {j}...")
        student_dict[f'{j}'] = input()
    return student_dict

def InputStudent():
    lst_student = []
    while True:
        num_of_student = int(input("Please enter number of students in your class..."))
        if num_of_student >= 0:
            break
        else:
            print("Please enter an interger that bigger than or equal 0.")
            print("")
    for i in range(num_of_student):
        lst_student.append(StudentInfor())
    return lst_student


def ShowStudent(lst_student):
    print("Your student list:")
    for i in lst_student:
        print(f"ID:{i['StudentID']}-{i['StudentName']}-{i['DoB']}")

def CourseInfor():
    course_dict={'CourseID': 0, 'CourseName': 0}
    for j in course_dict.keys():
            print(f"Please input {j}...")
            course_dict[f'{j}'] = input()
    return course_dict

def InputCourse():
    lst_course = []
    while True:
        num_of_course = int(input("Please enter number of courses..."))
        if num_of_course >= 0:
            break
        else:
            print("Please enter an interger that bigger than or equal 0.")
            print("")
    for i in range(num_of_course):
        lst_course.append(CourseInfor())
    return lst_course

def ShowCourse(lst_course):
    print("Your course list:")
    for i in lst_course:
        print(f"ID:{i['CourseID']}-{i['CourseName']}| ")

def MarkInfo(lst_course, lst_student):
    mark_dict = {'CourseName': 0, 'CourseID': 0, 'StudentName': 0, 'StudentID': 0, 'Mark': 0}
    mark_dict["CourseName"] = lst_course["CourseName"]
    mark_dict["CourseID"] = lst_course["CourseID"]
    mark_dict["StudentName"] = lst_student["StudentName"]
    mark_dict["StudentID"] = lst_student["StudentID"]
    mark_dict["Mark"] = input()
    return mark_dict

def InputMark(lst_course, lst_student):
    lst_mark = []
    for i in lst_course:
        for j in lst_student:
            print(f'Please input the mark in course {i["CourseName"]}-ID:{i["CourseID"]} for student {j["StudentName"]}-ID:{j["StudentID"]}...')
            lst_mark.append(MarkInfo(i, j))
    return lst_mark

def ShowMark(lst_mark):
    print("Your mark list:")
    for i in lst_mark:
        print(f"{i['CourseID']}: {i['CourseName']}__ {i['StudentID']} {i['StudentName']}__ Mark: {i['Mark']}")

            
lst_student = InputStudent()
lst_course = InputCourse()
lst_mark = InputMark(lst_course, lst_student)

ShowStudent(lst_student)
ShowCourse(lst_course)
ShowMark(lst_mark)







        
