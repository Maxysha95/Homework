def transposeDict(d):
	      res = {}
	      for k,v in d.items():
	              res[v] = k
	      return res

def frequencyDict(s):
	      res={}
	      for i in s:
	           if i not in res:
	                res[i] = 1
	           else:
	                res[i]+=1
	      return res
