import pickle
import os

class Emp:
    def __init__(self, eid=0, ename="", basic=0):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def getdata(self):
        self.eid = int(input("Enter Employee ID: "))
        self.ename = input("Enter Employee Name: ")
        self.basic = float(input("Enter Basic Salary: "))

    def display(self):
        print(self.eid, self.ename, self.basic)
