d1={"a":"2","b":"4"}
def sum_dict(d1):
 sum=0
 for i in d1.values():
  sum=int(sum)+int(i)
 return sum
print(sum_dict(d1))

