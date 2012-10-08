#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import exit
import re
import json
import urllib2
import random

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
	dance = random.uniform(0.5,1.0)
	hotness = random.uniform(0.5,1.0)
	a = 'http://developer.echonest.com/api/v4/song/search?api_key=19EL7JSMTLLWIHPS0&format=json&results=1&artist_end_year_before=2004&min_danceability=0.{dance}&song_min_hotttnesss=0.{hotness}'.format(dance = random.randint(5,10), hotness = random.randint(5,10))
	f = urllib2.urlopen(a)
	songdata = json.load(f)
	print "The song playing on the jukebox is {song} by {artist}".format(song = songdata['songs'][0]['title'], artist = songdata['songs'][0]['artist_name'])
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
	print "Your father’s journals reveal that he isn’t the man that you thought he was."
	print "He was framed.  Someone will have to pay for this."
	print "Reading your father's journals, you find out who betrayed him."
	print " "
	print "1. Victoria Grayson: Queen of the Hamptons. Your father’s lover before he was framed."
	print "2. Conrad Grayson: CEO of Grayson Global. He is directly responsible for what happened to your father."
	print "3. Bill Harmon: Your father's best friend. Testified against your father to save his job."
	print "4. Dr. Michelle Banks: Put you in an institution in order to further her career."
	print "5. Mason Treadwell: Originally told you he would print the truth, but his book about your father was full of LIES!"
	print "6. Senator Kingsly: Ignored evidence that would have saved your father and proven him not guilty."
	print " "
	print "What do you do now? Do you:"
	print "1. Take time to plan it out. These assholes must be taken down appropriately."
	print "2. Who needs time when you have guns?"
	next = raw_input("> ")
	if next == "1":
		changetoemily()
	elif next == "2":
		gunsablazin()
	else:
		#send it back to the function that called it?
		cthulhu(anditbegins)
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

def cthulhu(wherefrom):
	print " "
	print "Hmm. You seem to have wondered over to the ocean."
	print "Rising out of the ocean is Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Can you kill Cthulhu before he drives you insane?"
	print "You have two choices. Do you pick the axe or the rifle?"
	cthulhu_life = 0
	emily_sanity = 0
	rifle = ('rifle', 'Rifle', 'RIFLE')
	axe = ('axe', 'Axe', 'AXE')
	while cthulhu_life < 10 and emily_sanity < 10:
		next = raw_input("> ")
		if any(a in next for a in axe):
			cthulhu_life += 4
			emily_sanity +=2
			print "Nice hit! Axe or rifle?"
		elif any(b in next for b in rifle):
			cthulhu_life +=3
			emily_sanity +=2
			print "Good shot! Axe or rifle?"
		else:
			emily_sanity +=4
			print "You are going insane. Axe or rifle?"
	if cthulhu_life >= 10:
		print "You have killed Cthulhu."
		#try to send it back from whence it came
		wherefrom()
	else:
		dead("You have gone insane. ")

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
