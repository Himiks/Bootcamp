from error_handler import error_handle
from student_operations import add_student, view_student, update_student, delete_student

Start = True
print("\n Welcome to Student Management System")

while Start:
    print("Please select: ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choose = input("Select: ")
    try:
        match choose:
            case '1':
                add_student()
            case '2':
                view_student()
            case '3':
                update_student()
            case '4':
                delete_student()
            case '5':
                Start = False
            case _:
                print("Invalid input try again please")
    except Exception as e:
        error_handle(e)
            
            
            
            
              