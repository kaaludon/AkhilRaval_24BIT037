s={"aryan","bhavya",'amit'}
a,b=set(),set()
for i in s:
    if i[0]=='a':
        a.add(i)
    elif i[0]=='b':
        b.add(i)
print(s)
print(a)
print(b)
