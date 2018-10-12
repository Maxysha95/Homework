def listToString(a):
        assert type(a) == list

	return str(a)

def competition(e, k):

        advanced = 0
	for i in range(len(e)):
		if e[i] >= e[k]:
			advanced += 1
	return advanced

def shorting(e):
	for i in range(len(e)):
		if len(e[i]) > 10:
			e[i] = e [i][0] + str(len(e[i]) - 2) + e[i][len(e[i]) - 1]
	return e

def addBorder(a):
	border = "+"
	for i in range(len(a[0])):
		border += "-"
	border += "+"
	for i in range(len(a)):
		a[i] = "|" + a[i] + "|"
	return [border] + a + [border]
