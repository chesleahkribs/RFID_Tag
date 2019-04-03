#proj2.py
import numpy as np


# Python program to get average of a list 
def Average(lst): 
    return sum(lst) / len(lst) 



with open("testdata") as f:
	floatdata = f.read()

floatdata = floatdata.rstrip()

tdata = floatdata.split("\n")

#tdata = tdata.strip()

new_tdata = []
for item in tdata:
	new_tdata.append(float(item))

  
# Driver Code 
 
average = Average(new_tdata) 
  
## Printing average of the list 
#print("Average of the list =", average)

threshold = 0.02

#if above the threshold 
pulselist=[]

for i in range(len(new_tdata)):
	if new_tdata[i] > threshold and new_tdata[i-1] < threshold and new_tdata[i+1] > threshold:
		pulselist.append(i)

#print len(pulselist)

	#if concurcount 
tagdict = {}
counter = 1
with open("Proj2_tag_signature") as t:
	tg = t.read()

tg = tg.rstrip()

tagline = tg.split("\n")

for line in tagline:
	l = line.split(' ')
	temp = []
	for i in l:
		if i:
			temp.append(int(i))
	if temp:		
		tagdict[counter] = temp
		counter += 1
	
#print tagdict	


#calculating the bursts and trying to print them out 
hits = 0
counter = 1 
for peak in pulselist:
	for tag in tagdict:
		startpeak = peak
		for interval in tagdict[tag]:
			if new_tdata[startpeak+interval+2] > threshold:
				hits += 1
				startpeak += interval # increment start peak by the interval 
			else: 
				hits = 0
				break # break out of the interval loop
		if hits == 39: #bc a burst is 40 pulses??
			#print "hi " + str(counter)
			print "burst", counter, ": got tag", tag, "at", peak
			counter+= 1 # print burst the tag and p 
			hits = 0
			break
	



		'''count = 0
		for intervalnum in tag:
			startpeak += tag
			#if any value p in peak such that p exists within startpeak -25 or startpeak +25
			startpeak 
'''

