import json


def write(student):
    with open("student.txt", "w") as file:
       file.writelines(student)


def read():
    with open("student.txt", "r") as file:
        return file.readlines()
