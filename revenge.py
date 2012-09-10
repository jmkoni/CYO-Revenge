from sys import exit
import re

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
	print why, "Good job!"
	exit(0)

def start():
	print "Date: June 2002. You're Amanda Clarke."
	print "You're father is David Clarke, convicted of helping launder money for the domestic terrorists who blew up Flight 197 on June 4, 1993."
	print "You've just been released from Allenwood Juvenile Detention Facility after two years." 
	print "Picking you up is Nolan Ross."
	print " "
	print "Nolan hands you a box and tells you that your father is not who you think he is."
	print "He also tells you that there is a key in the box that unlocks a safe in Switzerland with billions of dollars, the earnings from your father investing in his company."
	print "What do you do?"
	print " "
	print "1) Ignore the contents of the box. You already know what your father did. But definitely take the money. There is some sweet partying to be done."
	print "2) You're intrigued. You go through the contents of the box. And take the money. It is yours, after all."
	
	next = raw_input("> ")
	
	if next == "1":
		self_destruct()
	elif next == "2":
		anditbegins()
	else:
		dead("You stumble around the room until you starve.")

start() 
