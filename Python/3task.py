





def upgrade_grade(name, students, grade):
    if name in students:
        students[name]['grade'] = grade
        print(f"Student {name} has an updated grade - {students[name]['grade']}")
    else:
        print(f"There is no such student with name {name}")
    


students = {
    "Andrew" : {"age": 19, "grade": 70},
    "Anna" : {"age": 20, "grade": 80},
    "Tom" : {"age": 25, "grade": 85}
    
}


upgrade_grade("Tom", students, 90)
upgrade_grade("Nik", students, 70)

