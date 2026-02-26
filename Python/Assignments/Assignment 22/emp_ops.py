import pickle
import os
from emp import Emp

FILENAME = "emp.txt"


def add_record():
    f = open(FILENAME, "ab")
    e = Emp()
    e.getdata()
    pickle.dump(e, f)
    f.close()
    print("Record added successfully")


def search_record():
    found = False
    eid = int(input("Enter Employee ID to search: "))
    f = open(FILENAME, "rb")

    try:
        while True:
            e = pickle.load(f)
            if e.eid == eid:
                e.display()
                found = True
                break
    except EOFError:
        pass

    f.close()
    if not found:
        print("Record not found")


def delete_record():
    eid = int(input("Enter Employee ID to delete: "))
    found = False
    f = open(FILENAME, "rb")
    temp = open("temp.dat", "wb")

    try:
        while True:
            e = pickle.load(f)
            if e.eid != eid:
                pickle.dump(e, temp)
            else:
                found = True
    except EOFError:
        pass

    f.close()
    temp.close()

    os.remove(FILENAME)
    os.rename("temp.dat", FILENAME)

    if found:
        print("Record deleted successfully")
    else:
        print("Record not found")


def edit_record():
    eid = int(input("Enter Employee ID to edit: "))
    found = False
    f = open(FILENAME, "rb")
    temp = open("temp.dat", "wb")

    try:
        while True:
            e = pickle.load(f)
            if e.eid == eid:
                print("Enter new details:")
                e.getdata()
                found = True
            pickle.dump(e, temp)
    except EOFError:
        pass

    f.close()
    temp.close()

    os.remove(FILENAME)
    os.rename("temp.dat", FILENAME)

    if found:
        print("Record updated successfully")
    else:
        print("Record not found")


def display_all():
    f = open(FILENAME, "rb")
    print("\nEID\tName\tBasic")

    try:
        while True:
            e = pickle.load(f)
            e.display()
    except EOFError:
        pass

    f.close()
