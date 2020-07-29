d={'a':10,'b':1,'c':22}
t=list(d.items())
print(t)

for key,value in t:
   print(key,value)

l=list()
for key,value in d.items():
   l.append((value,key))

print(l)

l.sort(reverse=True)

print(l)