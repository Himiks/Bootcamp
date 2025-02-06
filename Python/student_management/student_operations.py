from file_handler import write, read


def add_student():
    print("Please enter student credentials: ")
    student_id = input("Id: ")
    name = input("Name: ")
    phone = input("Phone: ")
    student = f"{student_id},{name},{phone}\n"
    students = read()  
    students.append(student)  
    write(students) 
    
    
def view_student():
        students = read()
        for student in students:
            student_data = student.strip().split(',')
            print("\t".join(student_data))
            
            


def update_student():
    print("Enter an id of student you would like to change: ")
    id = input("Id:")
    students = read()
    for i, student in enumerate(students):
        info = student.strip().split(',')
        if info[0] == id:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            students[i] = f"{id},{name},{phone}\n"
            write(students)
            print("Success")
            return
    print(f"There is no student with such id - {id}")
 
 
def delete_student():
    id = input("Enter a student id to delete ")
    students = read()
    for i, student in enumerate(students):
        info = student.strip().split(',')
        if info[0] == id:
            students.pop(i)
            write(students)
            print("Success")
            return
    print(f"There is no student with such id - {id}")
               
                
                
           
        
        