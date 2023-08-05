count=1
a=input("enter the string1 value:")
b=input("enter the string2 value:")
for i in range(0,len(a)):
 for j in range(0,len(b)):
  if a[i]==b[j]:
   count=count+1
c=len(a)+len(b)-count
print(c)
x=c
e=["f","l","a","m","e","s"]
if x<=6:
  print(e[x-1])
elif x>=6:
   d=x%6
   print(e[d-1])