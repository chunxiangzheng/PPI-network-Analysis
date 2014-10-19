#store the id of homologous proteins in a set, and return
def getProteinSet(blast):
	s = set()
	f = open(blast, "r")
	for line in f.read().split("\n"):
		arr = line.split("\t")
		if len(arr) < 3: continue
		s.add(arr[1])
	f.close()
	return s
#store the interaction network in a dictionary, the key is one protein, the value is a list of interactors for that protein
def getInteractionDict(db):
	d = dict()
	f = open(db, "r")
	for line in f.read().split("\n"):
		arr = line.split("\t")
		if len(arr) < 2: continue
		if arr[0] in d: d[arr[0]].append(arr[1])
		else : d[arr[0]] = [arr[1]]
		if arr[1] in d: d[arr[1]].append(arr[0])
		else : d[arr[1]] = [arr[0]]
	f.close()
	return d
#num is the threshold of num of interactions, d is the dictionary of ineraction, s is the set of homologous proteins, out is output file
def writeHighOverlapProteins(num, d, s, out):
	fout = open(out, "w")	
	for key in d:
		count = 0
		for pro in d[key]:
			if pro in s: count = count + 1
		if count >= num: fout.write(key + "\t" + str(count) + "\n")
	fout.close()
#get the first order interactor from the curated network, d is the dictionary as desribed before, stored the entire network, 
#l is a list of identifiers of targeted proteins
def getFirstOrder(d, l):
	newl = []
	for pro in l:
		visited= set()
		for p in d[pro]:
			visited.add(p)
			for pp in d[p]:
				if not pp in visited : 
					newl.append(pp)
					visited.add(pp)
	return newl
#yeast
s = getProteinSet("gapdh.ecoli.yeast.full.tsv.filtered")
d = getInteractionDict("full.yeast")
writeHighOverlapProteins(8, d, s, "gapdh.potentialMatch.yeast")
#human
s = getProteinSet("gapdh.ecoli.human.full.tsv.filtered")
d = getInteractionDict("full.human")
writeHighOverlapProteins(18, d, s, "gapdh.potentialMatch.human")
