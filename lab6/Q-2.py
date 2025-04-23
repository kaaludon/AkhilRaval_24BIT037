import random as r
s=set()
for i in range(10):
    s.add(r.randint(15,45))
c=0
print(s)
a=s.copy()
for i in a:
    if i<30:
        c+=1
    elif i>35:
        s.discard(i)
print(c,"numbers less than 30")
print(s)
