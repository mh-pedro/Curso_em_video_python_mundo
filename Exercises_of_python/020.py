# Write a program that randomizes a student to go to the blackboard in a specific order.

import random

s1 = str(input("Write the name of student: "))
s2 = str(input("Write the name of student: "))
s3 = str(input("Write the name of student: "))
s4 = str(input("Write the name of student: "))
list = [s1,s2,s3,s4]
random.shuffle(list)
print("The first student is {}, the second is {}, the third is {} and the last is {}.".format(list[0],list[1],list[2],list[3]))
