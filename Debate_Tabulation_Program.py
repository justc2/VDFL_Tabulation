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
    
        self.rowlen = len(self.data)
        self.columnlen = len(self.data[0])
        
        self.findroundnum()

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
        self.searchdata([5,10,15,20],[2,5,8])
            
    def seperateteams(self): #creates lists of team IDs for varsity and novice teams
        self.teamlist = [] #list of all teams  
        self.team1list = []
        self.team2list = [] 
        self.byelist = []   
        if self.roundnum == 1:
            self.vteamlist = [] #list of varsity teams
            self.nteamlist = [] #list of novice teams

            self.searchdata(range(1,self.rowlen),[1])
            
            rowcounter = 2
            while rowcounter<len(self.dataset)-1:
                team = self.dataset[rowcounter]
                novice = self.dataset[rowcounter+1].lower()
                if novice == "":
                    self.vteamlist.append(team)
                elif novice == "n" or novice == "(n)":
                    self.nteamlist.append(team)
                else:
                    print "Invalid inputs for novice identification."
                rowcounter += 2
        

            self.givebye(self.vteamlist)
            self.givebye(self.nteamlist)
                    
            self.pairteams(self.vteamlist)
            self.pairteams(self.nteamlist)
            
            print self.team1list
            print self.team2list
            print ""
            
            self.createskims() #create the round 1 skims

            
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
        while True:
            tlist = teamlist
            t1list = self.team1list
            t2list = self.team2list
            print "tlist: ",tlist
            while len(tlist)>1:
                breakcounter = 0
                team1 = choice(tlist)
                team2 = choice(tlist)
                while team1[:3] == team2[:3]:
                    team1 = choice(tlist)
                    team2 = choice(tlist)
                    breakcounter += 1
                    if breakcounter == 3:
                        break
                tlist.remove(team1)            
                tlist.remove(team2)
                t1list.append(team1)
                t2list.append(team2)
            if len(tlist) == 1 or len(tlist) == 0:
                break
        self.team1list = t1list
        self.team2list = t2list
      
      
    def givebye(self, teamlist):
        if len(teamlist)/2 != float(len(teamlist))/2:
            self.byelist.append()
    
      
    def createskims(self):
        csvtestwrite = open("Round "+str(self.roundnum)+" Skims.csv","w")
        skimwriter = csv.writer(csvtestwrite)
        skimwriter.writerow(["Team 1", "Team 2", "Judges"])
        rows = zip(self.team1list, self.team2list)
        for row in rows:
            skimwriter.writerow(row)
            

DebateTabulation()


