'''
Created on Feb 3, 2014

@author: JustinC
'''

import csv
from random import choice


class DebateTabulation(object):
    
    def __init__(self):
        self.roundnum = 4
        self.getdata("Hanover Filled Sheet.csv")
        self.maindata = self.data
        self.rowlen = len(self.maindata)
        self.columnlen = len(self.maindata[0])
#        self.findroundnum()

        if self.roundnum<=3:
            self.seperateteams()
        else:
            self.getresults()
     
    def getdata(self, scoresheetname): #takes data off of a csv file with team names/records
        with open(scoresheetname, 'rU') as mainfile:
            self.data = list(tuple(entry) for entry in csv.reader(mainfile, delimiter=','))
         
    def searchdata(self, datalist, rows, columns):
        self.dataset = []
        rowcounter = 0
        while rowcounter<len(rows):
            columncounter = 0
            while columncounter<len(columns):
                r = datalist[rows[rowcounter]]
                data = r[columns[columncounter]]
                self.dataset.append(data)
                columncounter += 1
            rowcounter += 1
        print "dataset:",self.dataset
        print ""
        
        
    def findroundnum(self):
        self.searchdata(self.maindata,[5,10,15,20],[2,5,8])
        counter = 0
        while counter<len(self.dataset):
            if self.dataset[counter-1] == "" and self.dataset[counter] == "" and self.dataset[counter+1] == "":
                if counter>7:
                    self.roundnum = 3
                    break
                elif counter>3:
                    self.roundnum = 2
                    break
                else:
                    self.roundnum = 1
            else:
                counter += 1                
        if counter == 12:
            self.roundnum = 4
        
        
    def seperateteams(self): #creates lists of team IDs for varsity and novice teams
        self.teamlist = [] #list of all teams  
        self.team1list = []
        self.team2list = [] 
        self.lowerteamlist = []   
        if self.roundnum == 1:
            self.vteamlist = [] #list of varsity teams
            self.nteamlist = [] #list of novice teams

            self.searchdata(self.maindata, range(0,self.rowlen), [0])
            
            rowcounter = 2
            while rowcounter<len(self.dataset)-1:
                team = self.dataset[rowcounter]
                novice = self.dataset[rowcounter+1].lower()
                if novice == "":
                    self.vteamlist.append(team)
                elif novice == "n" or novice == "(n)":
                    self.nteamlist.append(team)
                else:
                    print "Invalid inputs for novice identification for team "+team
                rowcounter += 2
        

            self.givebye(self.vteamlist)
            self.givebye(self.nteamlist)
                    
            self.pairteams(self.vteamlist)
            self.pairteams(self.nteamlist)
            
            self.createskims() #create the round 1 skims

            
        elif self.roundnum == 2:
            self.winteamlist = []
            self.loseteamlist = []
            self.pastpairings()
            self.searchdata(self.maindata, range(0,self.rowlen), [0,2])
            rowcounter = 4
            while rowcounter<len(self.dataset)-3:
                team = self.dataset[rowcounter]
                winloss = self.dataset[rowcounter+1].lower()
                if winloss == "w":
                    self.winteamlist.append(team)
                elif winloss == "l":
                    self.loseteamlist.append(team)
                else:
                    print "Invalid Win/Loss input for team "+team
                rowcounter+=4
            
            print self.winteamlist
            print self.loseteamlist
            
            self.givebye(self.winteamlist)
            self.givebye(self.loseteamlist)
                        
            self.pairteams(self.winteamlist)
            self.pairteams(self.loseteamlist)
            
            self.createskims()
                
        else:
            self.winteamlist = []
            self.eventeamlist = []
            self.loseteamlist = []
            self.pastpairings()
            self.searchdata(self.maindata, range(0,self.rowlen), [0,2,5])
            rowcounter = 6
            while rowcounter<len(self.dataset)-5:
                team = self.dataset[rowcounter]
                winloss1 = self.dataset[rowcounter+1].lower()
                winloss2 = self.dataset[rowcounter+2].lower()
                if winloss1 == "w" and winloss2 == "w":
                    self.winteamlist.append(team)
                elif winloss1 == "w" or winloss1 == "l" and winloss2 == "w" or winloss2 == "l" and winloss1 != winloss2:
                    self.eventeamlist.append(team)
                elif winloss2 == "l" and winloss2 == "l":
                    self.loseteamlist.append(team)
                else:
                    print "Invalid Win/Loss input for team "+team
                rowcounter+=6
            
            print self.winteamlist
            print self.eventeamlist
            print self.loseteamlist
            
            self.givebye(self.winteamlist)
            self.givebye(self.eventeamlist)
            self.givebye(self.loseteamlist)
                        
            self.pairteams(self.winteamlist)
            self.pairteams(self.eventeamlist)
            self.pairteams(self.loseteamlist)
            
            self.createskims()
        
        
    def pastpairings(self):
        self.pastpairdict = {}
        self.getdata("Round 1 Skims.csv")
        self.searchdata(self.data, range(0,len(self.data)),[0,1])
        self.r1data = self.dataset
        counter = 2
        while counter<len(self.r1data):
            team1 = self.r1data[counter]
            team2 = self.r1data[counter+1]
            self.pastpairdict[team1] = [team2]
            self.pastpairdict[team2] = [team1]
            counter += 2
        print self.pastpairdict
        if self.roundnum == 3:
            self.getdata("Round 2 Skims.csv")
            self.searchdata(self.data, range(0,len(self.data)),[0,1])
            self.r2data = self.dataset
            counter = 2
            while counter<len(self.r2data):
                team1 = self.r2data[counter]
                team2 = self.r2data[counter+1]
                self.pastpairdict[team1].append(team2)
                self.pastpairdict[team2].append(team1)
                counter += 2
            print self.pastpairdict                           

    def givebye(self, teamlist):
        if len(teamlist)/2 != float(len(teamlist))/2:
            if self.roundnum == 1:
                if teamlist == self.vteamlist:
                    lowerteam = choice(self.vteamlist)
                    self.vteamlist.remove(lowerteam)
                    self.nteamlist.append(lowerteam)
                    self.lowerteamlist.append(lowerteam)
                else:
                    self.nteamlist.append("Bye")
            else:
                if teamlist == self.winteamlist:
                    lowerteam = choice(self.winteamlist)
                    self.winteamlist.remove(lowerteam)
                    if self.roundnum == 2:
                        self.loseteamlist.append(lowerteam)
                    else:
                        self.eventeamlist.append(lowerteam)
                    self.lowerteamlist.append(lowerteam)
                elif teamlist == self.eventeamlist:
                    lowerteam = choice(self.eventeamlist)
                    self.eventeamlist.remove(lowerteam)
                    self.loseteamlist.append(lowerteam)
                    self.lowerteamlist.append(lowerteam)
                else:
                    self.loseteamlist.append("Bye")

    def pairteams(self, teamlist): #pairs teams following the Guidelines for pairing ||| Sometimes this doesn't return a list of team pairings if same-school teams would be forced to go against each other.
        while True:
            tlist = []
            for x in teamlist:
                tlist.append(x)
            tempteam1list = []
            tempteam2list = []
            breakcounter = 0
            while len(tlist)>1:
                team1 = choice(tlist)
                team2 = choice(tlist)
                while team1[:3] == team2[:3]:
                    team1 = choice(tlist)
                    team2 = choice(tlist)
                    breakcounter += 1
                    if breakcounter == 3:
                        break
                if breakcounter == 3:
                    print "broke"
                    break
                tlist.remove(team1)            
                tlist.remove(team2)
                tempteam1list.append(team1)
                tempteam2list.append(team2)
            if len(tlist) == 0:
                break
        for a in tempteam1list:
            self.team1list.append(a)
        for b in tempteam2list:
            self.team2list.append(b)
        print ""
        print self.team1list
        print self.team2list
        print ""

    def createskims(self):
        csvtestwrite = open("Round "+str(self.roundnum)+" Skims.csv","w")
        skimwriter = csv.writer(csvtestwrite)
        skimwriter.writerow(["Team 1", "Team 2", "Judges"])
        rows = zip(self.team1list, self.team2list)
        for row in rows:
            skimwriter.writerow(row)
        
    def getresults(self):
        self.topteams = []
        self.topspeakers = []
        self.searchdata(self.maindata, range(0,self.rowlen), [0,1] + range(11,16))
        
            

DebateTabulation()


