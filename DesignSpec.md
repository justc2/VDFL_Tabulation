Debate Tabulation (Programming in Action)
Justin Chen

Design Specification
===============

Introduction
===============
The aim of this project is to use computer programming to make debate tournament tabulation for the Vermont Debate and Forensics League (VDFL) public forum debate tournaments more efficient.  Note: This document may change.

Client Side Programming Language
===============
All code will be run client-side using Python 2.7.

CSV Files
===============
This program will read and write certain csv/excel files.
These include:
-VDFL_Tournament_Records.csv (referred to as the main excel sheet)
-Round_1_Skims.csv
-Round_2_Skims.csv
-Round_3_Skims.csv

Debate Tabulation Process
===============
Before tournaments dates, schools submit the ID code for each team (of format <SchoolName LastInitial1LastInitial2> e.g., Hanover RC), as well as novice or A-team ranking, to the hosting coach.  The coach then makes 1st round schematics following the Guidelines for pairings.  During the tournament, win/loss records and speaker points for each participant/team are recorded on an excel spreadsheet (see attached).  Round 2 and 3 schematics are created based off of these records according to the Guidelines for pairings.  At the end of the tournament top teams and speakers are determined based off of the records according to Prize determination.

Guidelines for pairings
===============
For all rounds, no teams from the same schools can meet each other and no teams who have met before in the same tournament can meet each other.  For Round 1, novice teams should face novice teams.  Additionally, in Round 1 A-ranked teams should not face other A-ranked teams (this rule is nullified if the team is a novice team).  For Rounds 2 and 3, pairings are determined based off of the records so far.  Teams with the same win/loss ratio are paired against each other randomly.  If this method does not match all teams, teams with consecutive win/loss ratios are paired taking speaker points into account (for example, the highest speaker point 0/1 team would be paired with the lowest speaker point 1/0 team for Round 2).  If there are an odd number of teams, a random team from the lower tier (novice or losing team) is given a bye (meaning they sit out the round).

Prize determination
===============
There are two types of prizes: team and individual speaker awards.  Team awards are based first on win/loss ratios, then on team speaker points, and finally on team ranks.  Novice team awards are also given to the best novice team.  Individual speaker awards are based first on speaker points, then on ranks.  There are allowed to be ties if all relevant criteria are equal.

Methods
===============
This program is written using a number of methods in a class.  This section will describe all of the methods.
-__init__(self): Initializes the program and creates several class variables (self.team1list, self.team2list).  Calls the getdata(self).

-getdata(self):
Opens and reads the main excel file containing tournament records, storing all the data in self.data.  Uses available data to figure out the round number (stored in self.roundnum).  Finally, either calls seperateteams(self) if the round number is 1-3 or getresults(self) if all three rounds are over.

-seperateteams(self):
First, the method creates self.teamlist.  It does this by accessing the know place in self.data where the team IDs are found.  Depending on the round number, the rest of this method does different things.  If it is round 1, the method separates self.teamlist in to self.vteamlist and self.nteamlist.  It does this based on whether a (N) can be found in the cell below a team’s ID in the main excel file.  If it is round 2, the method separates self.teamlist into self.winteamlist and self.loseteamlist.  It does this by looking at whether the team won or lost their 1st round from the main excel file.  If it is round 3, the method separates self.teamlist into self.winteamlist, self.eventeamlist, and self.loseteamlist.  It does this by looking at team records for round 2.* †  The method then calls pairteams(self, teamlist) with the subset teamlists.  Then, it calls createskims(self).

-pairteams(self, teamlist):
This method will randomly combine teams in the inputted teamlist together, appending to self.team1list and self.team2list.

-createskims(self):
This method opens the schematic file and writes in self.team1list and self.team2list to fill out the skims (except for the judges column).

-getresults(self):
This method uses self.data to get the results of the tournament.  It finds the top 4 teams, the top novice team, and the top 8 speakers using the data.  It then opens and writes those results into the main excel file.

*If there are an odd number of teams when separating, a random team from the lower performing list (either self.loseteamlist or self.nteamlist) will be given a bye.  If there are an even number of teams total but an odd number of teams in the subset teamlists, one pairing will be inter-subset (the best team from the lower performing list will be paired with the worst team in the higher performing list).
†Also remember that not pairing teams that have previously seen each other or are from the same school takes precedent over all other criteria.

Class Variables
===============

-self.roundnum:
integer, the round number (1, 2, or 3)

-self.team1list:
list of strings, the team names for the 1st column of a schematic

-self.team2list:
list of strings, the team names for the 2nd column of a schematic

-self.data:
list of tuples of strings, a list of tuples representing the columns and rows of the main 
excel file containing tournament records

-self.teamlist:
list of strings, list of all the team IDs

-self.vteamlist:
list of strings, list of all the varsity team IDs (non-novice)

-self.nteamlist:
list of strings, list of all the novice team IDs

-self.winteamlist:
list of strings, list of all the team IDs who have won all their rounds

-self.loseteamlist:
list of strings, list of all the team IDs of teams who have a even record (won 1, 
lost 1)

-self.eventeamlist:
list of strings, list of all the team IDs of teams who have lost all their rounds

Test Strategy
===============
This program will be tested using an already filled main excel file from a previous VDFL tournament found here.  Filled columns can be added or deleted to simulate different stages of the tournament.  This will be done manually and also checked for accuracy manually.  The criteria checked will be:
*Schematics follow Guidelines for pairing
*Records accurately giving the top teams/individuals, concurrent with the current method of excel conditional formatting to show the top teams
