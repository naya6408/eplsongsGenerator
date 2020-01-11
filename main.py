import os
import pprint

def setteamDirectory(teamName):
    '''
    changing our current working directory to the
    team folder that we want to grab our chants
    '''
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

tempTeamlist = [x.lower() for x in teamList] #putting all the team into lower cases for consistency


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(tempTeamlist)


teamName = input("Please enter the name of the team you would like to view the chant of:  \n")

if(teamName.lower() in tempTeamlist):
    print("Correct Input. Thank you for the input")
    ourteamDir = setteamDirectory(teamName)
else:
    print(teamName, " is a wrong input. Please check your input")
    print("please refer to the list of teams above.")

teamDirectory = setteamDirectory(tea)