l=[1,"hi",True,None,1]
print(l)
#len fun
print(len(l))
#type
print(type(l))
#list const
a=list(["hi",1,34,56,True])
print(a)
#access the element
print(a[3])
#negative index
print(l[-2])
#Slice
print(l[1:3])
print(l[1:])
print(l[:4])
print(l[-4:])
print(l[:-1])
#check iitem is exists
if 1 in l:
    print("yes")
#change items value
l[1]='deva'
print(l)
#change range items
l[2:4]=[22,False,"hi"]
print(l)
l[4:5]=[555]
print(l)
#insert
a.insert(0,333)
print(a)
#append
a.append(40)
print(a)
#extends
a.extend({22,33,87})
print(a)
b=[45,67,88,90]
a.extend(b)
print(a)