'''
Created on Feb 3, 2014

@author: JustinC
'''

import csv
from random import choice


class DebateTabulation(object):
    
    def __init__(self):
        self.roundnum = 1
        self.getdata()
     
    def getdata(self): #takes data off of a csv file with team names/records
        scoresheetname = "Hanover Filled Sheet.csv"
        
        with open(scoresheetname, 'rU') as mainfile:
            self.data = list(tuple(entry) for entry in csv.reader(mainfile, delimiter=','))
        
        self.findroundnum()

        self.rowlen = len(self.data)
        self.columnlen = len(self.data[0])
        
        if self.roundnum<=3:
            self.seperateteams()
        else:
            self.getresults()
         
    def searchdata(self, rows, columns):
        self.dataset = []
        rowcounter = 0
        while rowcounter<len(rows):
            columncounter = 0
            while columncounter<len(columns):
                r = self.data[rowcounter]
                data = r[columncounter]
                self.dataset.append(data)
                columncounter += 1
            rowcounter += 1
        print self.dataset
        print ""
        
    def findroundnum(self):
        rows = [5,10,15,20]
        columns = [2,5,8]
        self.searchdata(rows, columns)
            
    def seperateteams(self): #creates lists of team IDs for varsity and novice teams
        if self.roundnum == 1:
            self.teamlist = [] #list of all teams
            self.vteamlist = [] #list of varsity teams
            self.nteamlist = [] #list of novice teams
            self.team1list = []
            self.team2list = []
            
            rowcounter = 2
            while rowcounter<self.rowlen:
                teamrow = self.data[rowcounter]
                nrow = self.data[rowcounter+1]
                team = teamrow[0]
                novice = nrow[0].lower()
                self.teamlist.append(team)
                if novice == "":
                    self.vteamlist.append(team)
                elif novice == "n" or novice == "(n)":
                    self.nteamlist.append(team)
                else:
                    print "Invalid inputs for novice identification."
                rowcounter = rowcounter+2
                    
            self.pairteams(self.vteamlist)
            self.pairteams(self.nteamlist)
            
            print self.team1list
            print self.team2list
            print ""
            
            self.createskims() #create the round 1 skims

            
            if int(len(self.teamlist)/2) != len(self.teamlist)/2: #If there are an odd number of teams, give one team a bye
                ""
        elif self.roundnum == 2:
            self.pastpairings()
        elif self.roundnum ==3:
            self.pastpairings()
        else:
            ""
            #self.awards()
        
        
    def pastpairings(self):
        pastskimname = "Round "+str(self.roundnum-1)+" Skims.csv" 
        with open(pastskimname, 'rU') as pastskim:
            self.pastskim = list(tuple(entry) for entry in csv.reader(pastskim, delimiter=','))
            rowlen = len(self.pastskim)
            rowcounter = 2
            while rowcounter<=rowlen:
                team1 = self.pastskim[rowcounter[0]]
                team2 = self.pastskim[rowcounter[0]]
            self.pastpairdict = {}
        

    def pairteams(self, teamlist): #pairs teams following the Guidelines for pairing ||| Sometimes this doesn't return a list of team pairings if same-school teams would be forced to go against each other.
        while len(teamlist)>1:
            team1 = choice(teamlist)
            team2 = choice(teamlist)
            while team1[:3] == team2[:3]:
                team1 = choice(teamlist)
                team2 = choice(teamlist)
            teamlist.remove(team1)            
            teamlist.remove(team2)
            self.team1list.append(team1)
            self.team2list.append(team2)
      
      
    def createskims(self):
        csvtestwrite = open("Round "+str(self.roundnum)+" Skims.csv","w")
        skimwriter = csv.writer(csvtestwrite)
        skimwriter.writerow(["Team 1", "Team 2", "Judges"])
        rows = zip(self.team1list, self.team2list)
        for row in rows:
            skimwriter.writerow(row)
            

DebateTabulation()


