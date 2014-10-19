#get protein match dict
d = dict()
f = open("A-E.final.tsv", "r")
for line in f.read().split("\n"):
	arr = line.split("\t")
	if len(arr) < 2: continue
	if arr[0] in d :
		d[arr[0]].append(arr[1])
	else: d[arr[0]] = [arr[1]]
f.close()
#match protein interaction
f = open("acineto.network.clean", "r")
fout = open("acineto.network.match", "w")
for line in f.read().split("\n"):
	arr = line.split("\t")
	if not arr[0] in d or not arr[1] in d: continue
	fout.write(arr[0] + "_" + arr[1])	
	s = set()
	for proA in d[arr[0]]:
		for proB in d[arr[1]]:
			if proA < proB: tmp = proA + "_" + proB
			else : tmp = proB + "_" + proA
			if not tmp in s:
				fout.write("\t" + proA + "_" + proB)
				s.add(tmp)
	fout.write("\n")
fout.close()
f.close()
#match with EciD network
s = set()
f = open("E.coli","r")
for line in f:
	arr = line.strip().split("\t")
	if len(arr) < 2: continue
	if arr[0] < arr[1] : tmp = arr[0] + "_" + arr[1]
	else : tmp = arr[1] + "_" + arr[0]
	s.add(tmp)
f.close()
f = open("acineto.network.match", "r")
fout = open("acineto.network.match.filter","w")
for line in f.read().split("\n"):
	arr = line.split("\t")
	if len(arr) < 2: continue
	filtered = []
	for i in range(1, len(arr)):
		subarr = arr[i].split("_")
		if subarr[0] < subarr[1] : tmp = arr[i]
		else: tmp = subarr[1] + "_" + subarr[0]
		if tmp in s: filtered.append(arr[i])
	if len(filtered) > 0: 
		fout.write(arr[0])
		for item in filtered:
			fout.write("\t" + item)
		fout.write("\n")
fout.close()
f.close()
