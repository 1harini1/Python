print("----------------------------")
print("|---------CAMPUSPULSE--------|")
print("----------------------------")
students=[]
students_ids=set()
while True:
    print("1. Add Student")
    print("2. View All Students")
    print("3. Student Report")
    print("4. Class Statistics")
    print("5. Exit")
    option = input("Select an option (1-5): ")

    if option == "1":
        print("---------- Add Student ----------")
        student_ID=int(input("Enter Student ID: "))
        if student_ID in students_ids:
            print("\nStudent ID already exists\n")
            continue
        name=input("Enter students Name: ")
        number_of_subjects=int(input("Number of Subjects: "))
        subjects={}
        for i in range(number_of_subjects):
            subject=input(f"enter Subject {i+1}: ")
            marks=int(input(f"Enter {subject} Marks: "))
            subjects[subject]=marks
        student={"id":student_ID, "name": name, "subjects":subjects}
        students.append(student)
        students_ids.add(student_ID)
        print("\n Student added Successfully!")
    elif option=="2":
        print("--------- All Students ----------")
        if len(students)==0:
            print("No students have been added yet.")
        else:
            for student in students:
                total=0
                for marks in student["subjects"].values():
                    total+=marks
                average=total/len(student["subjects"])
                print(f"ID:{student['id']} | "
                      f"Name: {student['name']} |" 
                      f"Average: {average:.2f}")
    elif option =="3":
        print("\n-----------student Report-------------")
        search_ID=int(input("Enter Student ID: "))
        found=False
        for student in students:
            if student["id"]==search_ID:
                found=True
                print("\nStudent ID: ",student["id"])
                print("Name: ",student["name"])
                print("\nsubjects")
                print("--------------")
                total=0
                highest_subject=None
                highest_marks=-1
                lowest_subject=None
                lowest_marks=101
                for subject, marks in student["subjects"].items():
                    print(f"{subject:<15}: {marks}")
                    total+=marks
                    if marks > highest_marks:
                        highest_marks=marks
                        highest_subject=subject
                    if marks < lowest_marks:
                        lowest_marks=marks
                        lowest_subject=subject
                average=total/len(student["subjects"])
                print("\n----------------------")
                print(f"Average : {average:.2f}")
                print(f"Highest : {highest_subject} ({highest_marks})")
                print(f"Lowest : {lowest_subject} ({lowest_marks})")
                if average >=90:
                    performance="Outstanding"
                elif average>=75:
                    performance="Good"
                elif average>=60:
                    performance="Average"
                elif average>=40:
                    performance="Needs Improvement"
                else:
                    performance="At risk"
                print("Performace: ",performance)
                break
        if not found:
            print("Student not Found!")

    elif option=="4":
        print("\n-------------Class Statistics-------------")
        if len(students)==0:
            print("No students have been added yet")
            continue
        total_class_marks=0
        total_subjects_count=0
        top_student=None
        top_average=-1
        for student in students:
            student_total=0
            for marks in student["subjects"].values():
                student_total+=marks
                total_class_marks+=marks
                total_subjects_count+=1
            average=student_total/len(student["subjects"])
            if average>top_average:
                top_average=average
                top_student=student
        class_average=total_class_marks/total_subjects_count
        unique_subjects=set()
        for student in students:
            for subject in student["subjects"]:
                unique_subjects.add(subject)
        print("\nTotal Students: ",len(students))
        print(f"Class Average: {class_average:.2f}")
        print("\nTop Student")
        print(f"{top_student['name']}" f"({top_average:.2f})")
        print("\nUnique Subjects: ",len(unique_subjects))
        for subject in unique_subjects:
            print("-",subject)

    elif option=="5":
        print("\nThankyou for using CampusPulse!")
        break
    else:
        print("\nInvalid Option. please select 1-5.\n")

        


