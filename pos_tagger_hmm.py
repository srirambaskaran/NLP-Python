import sys
import random

states = ["VB","NN","IN","DT"]
emissions=["time","files","like","an","arrow"];
index = {"VB":1,"NN":2,"IN":3, "DT":4,"q0":0, "time":0,"flies":1,"like":2,"an":3,"arrow":4}
# a = [	[0,0.2,0.8,0,0],
# 		[0,0,0.3,0.2,0.5],
# 		[0,0.267,0.333,0.067,0],
# 		[0,0, 0.75, 0, 0.25],
# 		[0,0,1,0,0]]
a = [	[0.2,0.2,0.2,0.2,0.2],
		[0.2,0.2,0.2,0.2,0.2],
		[0.2,0.2,0.2,0.2,0.2],
		[0.2,0.2,0.2,0.2,0.2],
		[0.2,0.2,0.2,0.2,0.2] ]
b = [[0,0,0,0,0],[0.1,0.2,0.2,0,0],[0.1,0.1,0,0,0.1],[0,0,0.25,0,0],[0,0,0,0.5,0]]
backptr = {}
probability = {}

for q in states:
	probability[q] = {}
	backptr[q] = {}
	probability[q][index["time"]] = a[index["q0"]][index[q]] * b[index[q]][index["time"]]

print probability
for i in range(1, len(emissions)):
	print "===="+str(i)
	for q in states:
		max = float("-inf");
		maxState = ""
		for qStar in states:
			val = probability[qStar][i-1] * a[index[qStar]][index[q]] * b[index[q]][i]
			if(val > 0):
				print str(i)+"\t"+qStar+"\t"+q+"\t"+str(val)
			if val > max:
				max = val
				maxState = qStar
			elif val == max:
				if random.random() > 0.5:
					max = val
					maxState = qStar

		probability[q][i] = max
		backptr[q][i] = maxState
		


final_state = ""
max = float("-inf")
for q in states:
	if probability[q][4] > max:
		max = probability[q][4]
		final_state = q

print final_state
chosen = final_state
for i in range(len(emissions)-1, 0,-1):
	print str(i-1)+"\t"+backptr[chosen][i]
	chosen = backptr[chosen][i]



print "NN 0 \t"+str(probability["NN"][0])
print "VB 0 \t"+str(probability["VB"][0])

print "NN 1 \t"+str(probability["NN"][1])
print "VB 1 \t"+str(probability["VB"][1])

print "IN 2 \t"+str(probability["IN"][2])
print "VB 2 \t"+str(probability["VB"][2])

print "DT 3 \t"+str(probability["DT"][3])

print "NN 4 \t"+str(probability["NN"][4])

