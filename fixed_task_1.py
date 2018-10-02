def unique(e):
	list(e)
	l=[]
	for i in e:
		if i not in l:
			l.append(i) #i dont understood, why we dont need here a 'i+=1'
			
	b=sorted(l)

	return b

def mex(e):
	i=1
	while True:
		if i not in e:
			return i
		i+=1
