# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oos8bV9SzdnkqD4cs1bruifaeOSxwqN_
"""

First_name = input("Please enter your name:")
Last_name = input("Please enter your last name:")
Age = int(input("Please enter your age:"))
Date_of_birth = int(input("Please enter your year of birth:"))

mylist = [First_name,Last_name,Age,Date_of_birth]
 
for i in mylist:
  print(i)
  
if Age < 18 :
  print("You can't go out because it's too dangerous")

else:
  8print("You can go out to the street")