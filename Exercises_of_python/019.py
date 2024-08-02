# Write a program that randomizes a student to go to the blackboard and show how is.
import random

s1 = input("Write the name of student: ")
s2 = input("Write the name of student: ")
s3 = input("Write the name of student: ")
s4 = input("Write the name of student: ")
list = [s1,s2,s3,s4]
print("The students choice is {}.".format(random.choice(list)))