import os
import pprint

def setteamDirectory(teamName):
    newDir = "/Users/junsuplee/Desktop/eplsongsGenerator/Teams" + "/" + teamName
    return newDir


print("----------------------------------------------------")
print("-Program Written by Junsup Lee (naya6408) on github-")
print("----------------------------------------------------")
print("Welcome to EPL Chant Generator of season 2019-2020")
print("This program allows users to generate epl chants of any given team of 2019-2020 season")
print("Here are the list of teams that are available")


currentDirectory = os.getcwd()
newDirectory = currentDirectory + "/Teams"
teamList =os.listdir(newDirectory)
tempTeamlist = [x.lower() for x in teamList]
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(tempTeamlist)


teamName = input("Please enter the name of the team you would like to view the chant of:  \n")

if(teamName.lower() in tempTeamlist):
    print("Correct Input. Thank you for the input")
    ourteamDir = setteamDirectory(teamName)
else:
    print("Wrong input. Please check your input")


print("our current working directory is:", ourteamDir)
