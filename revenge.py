from sys import exit
import re

def self_destruct():
	print " "
	print "It\'s 2002 and you are now an 18 year old billionaire with major issues."
	print "You\'re partying like you just got out of juvie and maybe getting into a few bar fights."
	print "Then pesky, pesky Nolan shows up again to bail you out."
	print "He comments on your self-destruction and asks if you\'ve read the journals."
	print "What do you do?"
	print " "
	print "1) Say \"hell no, I don\'t care what they say. My father was a terrorist.\""
	print "2) Consider that maybe this is not what you should be doing and maybe"
	print "   looking into your and your father\'s history would be worth your time."
	next = raw_input("> ")
	if next == "1":
		destruct()
	elif next == "2":
		anditbegins()
	else:
		dead("Looks like the guy you were fighting with in the bar came back out and stabbed you.")
def destruct():
	print " "
	print "It\'s New Year\'s 2003 and you pick the wrong bar to party at."
	print "You start a fight with these two punks."
	print "One is a larger woman who seems to have a knife."
	print "The other is a skinny man who doesn?t appear to have a weapon."
	print "Who do you attack first?"
	print " "
	print "1) Disarm the woman!"
	print "2) Take out scrawny."
	next = raw_input("> ")
	if next == "1":
		dead("Too bad, scrawny also had a knife! He stabs you in the back and you die.")
	elif next == "2":
		dead("Not quick enough! The woman stabs you as soon as you go for the man. You die.")
	else:
		dead("Too slow! The woman stabs you while the man punches you in the face. You die.")
def anditbegins():
	print " "
	print "REVENGE TIME"

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
#	if "0" in next or "1" in next:
	if re.match('^[\d-]+$', next):
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of the other door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leff off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print " "
	print why, "Sorry."
	exit(0)

def start():
	print "Date: June 2002. You're Amanda Clarke."
	print "You're father is David Clarke, convicted of helping launder money"
	print "for the domestic terrorists who blew up Flight 197 on June 4, 1993."
	print "You've just been released from Allenwood Juvenile Detention Facility after two years." 
	print "Picking you up is Nolan Ross."
	print " "
	print "Nolan hands you a box and tells you that your father is not who you think he is."
	print "He also tells you that there is a key in the box that unlocks a safe in Switzerland"
	print "with billions of dollars, the earnings from your father investing in his company."
	print "What do you do?"
	print " "
	print "1) Ignore the contents of the box. You already know what your father did."
	print "   But definitely take the money. There is some sweet partying to be done."
	print "2) You're intrigued. You go through the contents of the box."
	print "   And take the money. It is yours, after all."
	
	next = raw_input("> ")
	
	if next == "1":
		self_destruct()
	elif next == "2":
		anditbegins()
	else:
		dead("Looks like you drank too much tequila in Allenwood and forgot how to talk without slurring your words. You couldn't figure out how to get the money and end up homeless.")

start() 
