l1=['S001','S002','S003','S004']
l2=['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards']
l3=['85','98','89','92']

d={}
for i in range(len(l2)):
    d[l1[i]]={l2[i],l3[i]}
print(d)

