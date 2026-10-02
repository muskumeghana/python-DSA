def linearSearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i]==el:
      ar.append(i)
  if len(ar)>0:
    return ar
  return -1
      

a=[1,11,12,9,18,2,12,11,12,12]
print(linearSearch(a,12))