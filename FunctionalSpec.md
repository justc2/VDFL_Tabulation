Debate Tabulation (Programming in Action)

Justin Chen


Functional Specification
===============

Introduction
---------------
The aim of this project is to use computer programming to make debate tournament tabulation for the Vermont Debate and Forensics League (VDFL) public forum debate tournaments more efficient.  Inputs and outputs will be handled with comma separated value (csv) files that will be opened as Microsoft Excel spreadsheets and manipulated by the programming language Python.  Note: This document may change.


Tabulation Step by Step
---------------
Here is some general information on public forum debate and VDFL tournaments from their website at http://www.vdflonline.org/Debate.html:

The VDFL offers tournament competition in Public Forum Debate. This style of debate involves a two person (pro) team competing against a two person (con) team. Each side develops its arguments for and against a proposition posed by the monthly resolution topic (announced online at nationalforensicsleague.org) The clash of ideas must be communicated in a manner persuasive to the non-specialist or “citizen judge”...
Judges provide a written critique of the debaters' performances and also indicate the winning team. At a tournament, [each team debates in three rounds. At the end of the tournament,] top teams as well as top speakers are recognized by the presentation of awards.

Here is a brief summary of the steps of tabulation for a public forum tournament.  The highlighted steps will be done by the program.
Input teams.
Create Round 1 schematics.
Input Round 1 results.
Create Round 2 schematics.
Input Round 2 results.
Create Round 3 schematics.
Input Round 3 results.
Calculate total results and award recipients.

Before a tournament, the tournament director (usually the coach of the hosting school) will be sent a list of the teams coming from each school.
The list will include…
the name of the school (e.g., Hanover)
the names of the individuals of the 2-person teams (e.g., Sera Richards-Gerngross and Justin Chen)
the team IDs using the school name and last initials of the individuals (e.g., Hanover RC)
if the team is a novice (both competitors are in their first academic year of debating)
if the team is an A-team - the top team from that school (cannot be a novice)

From this, the director creates an excel file of this data.  An example from a 2013 VDFL tournament at Hanover High School can be found [here](https://docs.google.com/a/hanovernorwichschools.org/file/d/0B00xrZeZB8EVYzd0bXE1UHBUYW8/edit).

Then, a round 1 (of 3) schematic is created to pair up the teams for the first round.  The program will be used to do this.  Based on novice and A-team ranking, the program will match teams from different schools against each other.  Schematics also include judge assignments, however, these will not be part of the program and will have to still be entered manually.  [Here](https://docs.google.com/a/hanovernorwichschools.org/file/d/0B00xrZeZB8EVdW1xRVNwTDg5V1E/edit) is a sample schematic (w/o judges filled in).

As the tournament progresses, a number of criteria filled out for each round on paper ballots by the judge are recorded in the Excel Sheet.  They include…
Win/Loss (W/L) =  The outcome of the round.
Speaker points (Pts) =  Individual debating skill ranked from 20-30 points.
Speaker rank (R) = Rank of the speakers from best to worst (1-4).
[Here](https://docs.google.com/a/hanovernorwichschools.org/file/d/0B00xrZeZB8EVY0s5V3h6SU0wM2s/edit) is a blank version of the complete judge’s ballot.

Later rounds (2 and 3) schematics will also be created by this program.  They no longer take novice or A-team rankings into account.  Instead, they are based off of the W/L ratio of the teams (teams with similar ratios are paired against each other).

At the end of the tournament, awards are given to the top 3 teams and top novice team based off of W/L ratios, then speaker points, then ranks.  This will be done by the program.  Additionally, speaker awards are given to the top 3-8 individuals based off of speaker points, then ranks.  This will also be done by the program.  This concludes the VDFL tabulation process.  The previously referenced Hanover tournament excel sheet can be found filled in with all the data from the tournament [here](https://docs.google.com/a/hanovernorwichschools.org/file/d/0B00xrZeZB8EVTy01QkFwTk9VM1E/edit).


CSV to Excel
---------------
Premade csv files will be used for the tournament including a scoresheet (for inputs) and 3 schematic tables (outputs by round).  In order for the user to easily manipulate, read, and print these files, they can be opened in Microsoft Excel by right clicking the file and using Open With → Microsoft Excel (on a mac).


Inputs
---------------
Most inputs will be received through a csv/excel file that contains information on teams, participants, wins/losses by round, speaker points/ranks by round, and total wins, losses, speaker points, ranks, and team sums of speaker points.  The file will start blank except for the column titles.  As the tournament progresses, the sheet will be filled out.  The data from this sheet will be used to run the program.  (See the example file from Hanover 2013 found in Tabulation Step by Step)


Outputs
---------------
Round by round schematics will be outputted into csv files.  The csv files will be titled with the format “Round 1 Skims.csv.”  They will be formatted with columns for Team 1, Team 2, and Judge (where one row would represent the two team who would debate against each other and the judge who would judge that round).  The program will fill in the Team 1 and Team 2 columns.  Judge assignments are currently not part of this project and can be manually entered (as they are currently).  If a team has a “bye” (meaning they do not debate that round due to an odd number of teams), the team ID will be found in the Team 1 column and the word “bye” will be found in the Team 2 column.  An example schematic can be found in Tabulation Step by Step.  If the tournament moderators are dissatisfied with the outputted schematics, they can be manually changed as well (as they are currently).  Post-tournament results will be outputted to the csv/excel file described in the Inputs section.  The program will output data for the final W, L, Pts, R (ranks), and Tm Pts columns.


Running the program
---------------
The “tabbers” of VDFL tournaments have a dedicated mac laptop to tabulate the tournaments that is accessible and has the IDLE development environment for python.  The program and necessary files will be downloaded onto the computer in a folder on the Desktop labelled “Debate Tabulation Program.”  During tournaments, the file entitled “Debate_Tabulation_Program.py” in that folder should be opened in IDLE and run by clicking on Run → Run Module.  The tabbers simply need to enter data into the csv/excel file (from Inputs).  The program will then output the correct data, so no user input is needed to the program itself.  In essence, the “tabbers” will fill in data to the main excel sheet before each round, run the program, and receive filled in schematics for the next round.  After the third round, the tabbers will run the program and receive a list of the award recipients.


Other notes
---------------
A secondary goal for this program after basic functionality is complete is to make the program as easily user-manipulated as possible.  Current debate tournament tabulation is very messy with lots of team/judge complications.  It is important that this program does not exacerbate these tabulation woes, but instead allows easy changes in anticipation of conflicts and problems.
