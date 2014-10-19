import re
f = open("acineto.network.match.filter.gunk", "r")
proDict = dict()
for line in f.read().split("\n"):
	arr = re.split("\t+", line)
	if len(arr) <= 1: continue
	interaction_A =arr[0]
	proA = interaction_A.split("_")[0]
	proB = interaction_A.split("_")[1]
	for i in range(1, len(arr)):
		ab_arr = arr[i].split("_")
		a = ab_arr[0]
		b = ab_arr[1]		
		if proA in proDict:
			if a in proDict[proA]:
				proDict[proA][a] = proDict[proA][a] + 1
			else:
				proDict[proA][a] = 1
		else :
			proDict[proA] = dict()
			proDict[proA][a] = 1
		if proB in proDict:
			if b in proDict[proB]:
				proDict[proB][b] = proDict[proB][b] + 1
			else:
				proDict[proB][b] = 1
		else :
			proDict[proB] = dict()
			proDict[proB][b] = 1
f.close()
fout = open("alignment.index","w")
for pro in proDict:
	for p in proDict[pro]:
		if proDict[pro][p] >= 2:
			fout.write(pro + "\t" + p + "\t" + str(proDict[pro][p]) + "\r")
fout.close()
f = open("acineto.network.match.filter.gunk", "r")
fout = open("acineto.network.match.filter.gunk.final", "w")
for line in f.read().split("\n"):
	arr = line.strip().split("\t")
	proA = arr[0].split("_")[0]
	proB = arr[0].split("_")[1]
	fout.write(arr[0] + "\t")
	if (len(arr) > 1):
		for i in range(1, len(arr)):
			ab_arr = arr[i].split("_")
			if len(ab_arr) < 2: continue
			a = ab_arr[0]
			b = ab_arr[1]
			if proDict[proA][a] >= 2 and proDict[proB][b] >= 2:
				fout.write(arr[i] + "\t")
	fout.write("\r")			
fout.close()
f.close()
