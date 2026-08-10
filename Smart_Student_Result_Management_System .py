#Subjects List
subjects=["Eng","Math","Phy","Comp","Urdu"]
# Store Student Records
students=[]
# Count Students
student_count=0
# Function to Calculate Percentage
def calculate_percentage(total):
    percentage=(total/500)*100
    return percentage
# Function to Calculate Grade
def calculate_grade(percentage):
    if percentage>=85:
        grade="A"
    elif percentage >= 70:
        grade="B"
    elif percentage>=60:
        grade="C"
    elif percentage>=50:
        grade="D"
    else:
        grade="Fail"
    return grade
# Function to Enter Marks
def input_marks():
    marks=[]
    for subject in subjects:
        while True:
            mark=int(input("Enter "+subject+" Marks:"))
            if mark>=0 and mark<=100:
                marks=marks+[mark]
                break
            else:
                print("Invalid Marks! Enter marks between 0 and 100.")
    return marks
# Function to Add Student
def add_student():
    global students
    global student_count
    print("== Add Student ==")
# Enter Roll Number
    while True:
        roll_number=input("Enter Roll Number:")
        if roll_number=="":
            print("Roll Number cannot be empty.")
        else:
            break
# Enter Student Name
    while True:
        name=input("Enter Student Name: ")
        if name == "":
            print("Student Name cannot be empty.")
        else:
            break
# Enter Marks
    marks=input_marks()
# Calculations
    total=sum(marks)
    average=total/5
    percentage=calculate_percentage(total)
    grade=calculate_grade(percentage)
# Pass/Fail
    result="Pass"
    for mark in marks:
        if mark<50:
            result="Fail"
            break
# Strongest Subject
    highest=marks[0]
    strongest_subject=subjects[0]
    for i in range(5):
        if marks[i]>highest:
            highest=marks[i]
            strongest_subject=subjects[i]
# Weakest Subject
    lowest=marks[0]
    weakest_subject=subjects[0]
    for i in range(5):
        if marks[i]<lowest:
            lowest=marks[i]
            weakest_subject=subjects[i]
# Store Student Record
    student_record=[roll_number,name,marks,total,average,percentage,grade,result,strongest_subject,
                      weakest_subject]
    students=students+[student_record]
    student_count=student_count+1
    print("Student Added Successfully!")
   
# View Result Functions
# Function to Display Student Result
def display_result(student):
    print("=== STUDENT RESULT CARD ===")
    print("Roll Number:",student[0])
    print("Student Name:",student[1])
    print("Subject Marks")
    for i in range(5):
        print(subjects[i],":",student[2][i])
    print("Total Marks:",student[3],"/500")
    print("Average:",round(student[4],2))
    print("Percentage:",round(student[5],2),"%")
    print("Grade:",student[6])
    print("Result:",student[7])
    print("==Subject Performance==")
    for i in range(5):
        if student[2][i]>=85:
            performance="Excellent"
        elif student[2][i] >= 70:
            performance="Good"
        elif student[2][i]>=50:
            performance="Average"
        else:
            performance="Needs Improvement"
        print(subjects[i],":",performance)
    print("Strongest Subject:",student[8])
    print("Weakest Subject:",student[9])
# Function to Search Student
def search_student():
    roll_number=input("Enter Roll Number to Search: ")
    found=False
    for student in students:
        if student[0]==roll_number:
            display_result(student)
            found=True
            break
    if found==False:
        print("Student Not Found.")
# Function to View Student Result
def view_student_result():
    search_student()
# Function to View All Students
def view_all_students():
    if len(students)==0:
        print("No Student Record Available.")
    else:
        print("== ALL STUDENTS RECORD ==")
        for student in students:
            print("Roll Number:",student[0])
            print("Name:",student[1])
            print("Percentage:",round(student[5], 2), "%")
            print("Grade:",student[6])
            print("Result:",student[7])
# Main Program Menu
while True:
    print("=== SMART STUDENT RESULT MANAGEMENT SYSTEM ===")
    print("1.Add Student")
    print("2.View Student Result")
    print("3.View All Students")
    print("4.Search Student")
    print("5.Exit")
    choice = int(input("Enter your choice (1-5): "))
    match choice:
        case 1:
            add_student()
        case 2:
            view_student_result()
        case 3:
            view_all_students()
        case 4:
            search_student()
        case 5:
            print("Thank you for using the system.")
            print("Program Ended Successfully.")
            break
        case _:
            print("Invalid Choice! Please enter correct choice.")
