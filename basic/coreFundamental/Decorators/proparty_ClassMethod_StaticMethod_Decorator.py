# -*- coding: utf-8 -*-
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    @property
    def msg(self):
        return self.name + " got grade " + self.grade
   
    @msg.setter 
    def msg(self,msg):
        sent = msg.split(" ")
        print(sent)
        self.name = sent[0]
        self.grade = sent[-1]
        
std1 = Student("Rasid", "B")
std1.msg = "Rakib got grade A"
print("name", std1.name)
print("grade", std1.grade)
print(std1.msg)

