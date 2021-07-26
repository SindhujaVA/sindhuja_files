d1={"name":"sindhu","deg":"MCA"}
for i in d1:
  print(i)
d1.pop("name") 
print(d1)
d1.popitem()
print(d1)
l1=[1,2,3,4,5]
l2=[24,45,75,65,56]
d1=dict(zip(l1,l2))
print(d1)