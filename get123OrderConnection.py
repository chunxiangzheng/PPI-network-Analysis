import os
def buildMap(f):
	network = dict()	
	fin = open(f, "r")
	for line in fin.read().split("\n"):
		arr = line.strip().split("\t")
		if len(arr) < 2: continue
		if not arr[0] in network:
			network[arr[0]] = [arr[1]]
		else :  network[arr[0]].append(arr[1])
		if not arr[1] in network:
			network[arr[1]] = [arr[0]]
		else :  network[arr[1]].append(arr[0])
	fin.close()
	return network
def get123(network):
	d = dict()
	for pro in network:
		print(pro)
		d[pro] = []
		first = []
		second = []
		third = []
		s = set()
		for p in network[pro]:
			s.add(p)
			first.append(p)
			print("first order " + p)
		d[pro].append(first)
		print("finish first order")
		for p in first:
			for pp in network[p]:
				if not pp in s:
					second.append(pp)
					s.add(pp)
					print("second order " + pp)
		d[pro].append(second)
		print("finish second order")		
		for p in second:
			for pp in network[p]:
				if not pp in s:
					third.append(pp)
					s.add(pp)
					print("third order " + pp)
		d[pro].append(third)
		print("finish third order")
	return d
#get homolog mapped table
def mapProtein(f):
	m = dict()
	fin = open(f, "r")
	for line in fin.read().split("\n"):
		arr = line.strip().split("\t")
		if len(arr) < 6: continue
		if arr[0] in m:
			m[arr[0]].append(arr[5])
		else:
			m[arr[0]] = [arr[5]]
	return m
#reduce data network to homolog proteins only
def reduceDataNetwork(m, d):
	t1 = dict()	
	for pro in d:
		t1[pro] = []
		for p in d[pro]:
			if p in m:
				for pp in m[p]:
					t1[pro].append(pp)
	t2 = dict()
	for pro in t1:
		if len(t1[pro]) >= 1: 
			t2[pro] = t1[pro]
	return t2

#match DATA with reference
def matchDataWithRef(d, ref, outdir):
	for pro in d:
		f = open(outdir + "/" + pro, "w")
		for target in ref:
			f.write(target + "\t")
			count = 0
			for p in ref[target][0]:
				if p in d[pro]:
					count = count + 1
			f.write(str(count) + "\t")
			count = 0
			for p in ref[target][1]:
				if p in d[pro]:
					count = count + 1
			f.write(str(count) + "\t")
			count = 0
			for p in ref[target][2]:
				if p in d[pro]:
					count = count + 1
			f.write(str(count) + "\n")		
		f.close()













