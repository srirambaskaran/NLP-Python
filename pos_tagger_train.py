from __future__ import print_function
import re
import sys


def calc_counts(tagI, tagJ):

	iRegex = "[a-z]+\/"+tagI
	jRegex = "[a-z]+\/"+tagJ

	nrRegex = "[a-z]+\/"+tagI+"\s[a-z]+\/"+tagJ

	f = open("input.txt","r")
	nr = 0
	dr = 0
	for line in f:
		for a in re.findall(iRegex,line):
			dr += 1
		for a in re.findall(nrRegex,line):
			nr += 1
	print( tagI+"\t"+tagJ+"\t"+"nr: "+str(nr)+"\tdr: "+str(dr)+"\t"+str(float(nr)/dr)+"\n",end='')


def counts(tagI):
	f = open("input.txt","r")
	nr = 0
	for line in f:
		for a in re.findall(tagI,line):
			nr += 1
	return nr;


# tags = [["VB","NN"],["VB","IN"],["VB","DT"],["NN","NN"],["NN","VB"],["NN","IN"],["IN","DT"],["DT","NN"],["IN","NN"]]
# # tags = [["DT","IN"]]
# for tag in tags:
# 	calc_counts(tag[0],tag[1])
tags = ["VB","NN","IN","DT"]
words = ["time","flies","like","an","arrow"]
# words = ["[a-z]+"]
for word in words:
	print( "\t"+word,end='')
print("\n",end='')
for tag in tags:
	print( tag, end='')
	for word in words:
		count = counts(word+"\/"+tag)
		print( "\t"+str(count),end='')
	print( "\n",end='')
