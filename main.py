import os

print("----------------------------------------------------------------")
print("Program Written by Junsup Lee naya6408 on github")
print("Welcome to EPL Chant Generator of season 2019-2020")
print("Here are the instructions")
print("This program allows users to generate epl chants of any given team of 2019-2020 season")
print("Here are the list of teams that are available")


newdir = os.chdir("/Users/Junsup/Desktop/eplsongsGenerator/Teams")
teamList =os.listdir()


teamName = input("Please enter the name of the team you would like to view the chant of:  \n")

if(teamName in teamList):
    print("Correct Input. Thank you for the input")
else:
    print("Wrong input")
