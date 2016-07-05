#!/usr/bin/python2
# coding:utf-8

# by ins3c7
# 5 july 2016

# I.A. 02

import json, os, re
from requests import get
from random import choice
from unidecode import unidecode as uni

os.system('clear')

class iabot:
	def __init__(self):
		self.questioned = []
		pass

	def learn(self):
		dbase = []
		with open('tech1.json', 'r') as f:
			data = json.load(f)
		for question in data['questions']:
			dbase.append([question['text'], question['answers'][0]['text']])
		return dbase

	def say(self):
		words = []
		dbase = self.learn()
		put = uni(raw_input('> ').decode('utf-8')).upper()
		put = re.sub('[.,?!]', '', put)
		if put in self.questioned:
			print 'Creuza: de novo?'
			return
		self.questioned.append(put)
		if len(put.split()) < 2:
			if put.find('OI') != -1 or put.find('OLA') != -1:
				print 'Creuza: Oi, tudo bem?'
			if put.find('PRAZER') != -1:
				print 'Creuza: o prazer é todo seu..'
			if put.find('PORQUE') != -1:
				print 'Creuza: não enche..'

			return
		for question in dbase:
			words = []
			q = question[0].upper()
			q = re.sub('[.,?!]', ' ', q)
			answer = question[1]
			# text = re.split('\W+', q)
			text = q.split()
			for w in text:
				# if len(w) > 0:
				words.append(w)
			confirm = set(put.split()) & set(words)
			# print put.split()
			# if len(confirm):
			# 	print confirm
			if len(confirm) == len(put.split()):
				print 'Creuza:', choice(answer)
				return

bot = iabot()
while True:	bot.say()