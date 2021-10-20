import datetime

class Tournament:
	date= datetime.date
	matches= []
	patch= "v0"
	name= "Test"
	def __init__(self,patch,name):
		self.date= datetime.date.today()
		self.patch= patch
		self.name= name
	def addMatch(self,match):
		self.matches.append(match)
	def print(self,output):
		#output.write(name+" "+str(self.date)+" "+str(self.patch)+"\n")
		output.write(name+","+str(self.date)+","+str(self.patch)+"\n")
		for match in self.matches:
			match.print(output)

class Match:
	level= -1
	rounds= []
	def __init__(self,level):
		self.level=level
	def addRound(self,round):
		self.rounds.append(round)
	def print(self,output):
		#output.write("\t"+str(self.level)+"\n")
		output.write(",,,"+str(self.level)+"\n")
		for round in self.rounds:
			round.print(output)

class Round:
	playerL= "default 1"
	playerR=  "default 2"
	scoreL= -1
	scoreR= -1
	characters= ["Isabella","Marie","Father Zera","Kalkstein","Lazlo","Gedeon","Barabash","Jacek"]
	characterL=characters[0]
	characterR=characters[0]
	def __init__(self,playerL,playerR,scoreL,scoreR,characterL,characterR):
		self.playerL= playerL
		self.playerR= playerR
		self.scoreL= scoreL
		self.scoreR= scoreR
		self.characterL= characterL
		self.characterR= characterR
	def print(self,output):
		#output.write("\t\t"+str(self.playerL)+"\t"+str(self.characterL)+"\t"+str(self.scoreL)+"\t"+str(self.playerR)+"\t"+str(self.scoreR)+"\t"+str(self.characterR)+"\n")
		output.write(",,,,"+str(self.playerL)+","+str(self.characterL)+","+str(self.scoreL)+","+str(self.playerR)+","+str(self.scoreR)+","+str(self.characterR)+"\n")



output= open("HQdata.csv",'a')
characters= ["Issabella","Marie","Father Zera","Kalkstein","Lazlo","Gedeon","Barabash","Jacek"]
name= input("Enter the name of the tournament:\n")
patch= input("Enter the current patch number of the game:\n")
tournament= Tournament(patch,name)
unwonT= True 
while unwonT:
	
	level= input("Enter the level of the next match. Finals are level 0, each round earlier is one higher. Round robins are all level 3:\n")
	match= Match(level)
	tournament.addMatch(match)
	unwonM= True
	while unwonM:
		playerL= input("Enter the name of the player on the left:\n")
		playerR= input("Enter the name of the player on the right:\n")
		scoreL= input("Enter the number of flags earned by "+playerL+":\n")
		scoreR= input("Enter the number of flags earned by "+playerR+":\n")
		characterL=characters[int(input("For "+playerL+" enter 0 for izzy, 1 for marie, 2 for zera, 3 for kalk, 4 for lazlo, 5 for gedeon, 6 for barabash, 7 for jacek:\n"))]
		characterR=characters[int(input("For "+playerR+" enter 0 for izzy, 1 for marie, 2 for zera, 3 for kalk, 4 for lazlo, 5 for gedeon, 6 for barabash, 7 for jacek:\n"))]
		round= Round(playerL,playerR,scoreL,scoreR,characterL,characterR)
		match.addRound(round)
		won=0
		while won!="Y" and won!="n":
			won= input("Is the match over? Y/n:\n")
		if won=="Y":
			unwonM=False

	won=0
	while won!="Y" and won!="n":
		won= input("Is the tournament over? Y/n:\n")
	if won=="Y":
		unwonT=False
tournament.print(output);

