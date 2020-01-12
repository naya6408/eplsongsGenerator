import os
import pprint
import sys

def setteamDirectory(teamName):
    '''
    changing our current working directory to the
    team folder that we want to grab our chants
    '''
    newteamDirectory = os.getcwd() + "/Teams/" + teamName
    return newteamDirectory

def createsongList(songtxtList):
    for i in range(len(songtxtList)):
        songtxtList[i] = songtxtList[i][0:len(songtxtList[i])-4]
        print(songtxtList)
    return songtxtList

def outputSong(filename, chantName):
    selectedChant = filename + ".txt"
    print("Here is the lyrics for ", filename)
    f = open(selectedChant, "r")
    print(f.read())

def main():
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

    while True:
        teamName = str(input("Please enter the name of the team you would like to view the chant of: "))
        teamName = teamName.lower().strip(" ")
        if(teamName in tempTeamlist):
            print("Correct Input. Thank you for the input")
            ourteamDir = setteamDirectory(teamName)
            break
        elif(teamName == "exit"):
            print("exiting program")
            sys.exit()
        else:
            print(teamName, " is a wrong input. Please check your input")
            print("please refer to the list of teams above.")
            print("press type exit if you would like to exit program")
            continue
    teamDirectory = setteamDirectory(teamName)
    os.chdir(teamDirectory)
    print("here are the available list of chants for " + teamName)
    songList = os.listdir(teamDirectory)
    songList = createsongList(songList)
    print("the list of songs are: ", songList)
    selectedChant = str(input("Please select your song from the list: "))
    outputSong(selectedChant, selectedChant)


if __name__ == "main":
    main()