
fname=input('enter file name: ')
if len(fname)<1 : fname='clown.txt'
handle=open(fname)
counts= {}
for line in handle:
    line=line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1


lst=list()
for key,value in counts.items():
    newtup=(value,key)
    lst.append(newtup)
lst=sorted(lst,reverse=True)
for value,key in lst[0:5]:
    print(key,value)
