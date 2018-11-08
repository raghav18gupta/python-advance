import os

def listoftxt(dir):
	for i in os.walk(dir):
		for j in i[2]:
			if j.endswith(".py"):
				print(i[0]+'/'+j)

listoftxt('/home/raghav/Desktop/gitHub/what-I-learned/py-advance')