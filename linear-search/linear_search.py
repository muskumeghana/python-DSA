def linearSearch(a,el):
  for i in range(len(a)):
    if a[i]==el:
      print(f'element {el} is found at index {i}')
      return i
  return -1





a=[1,31,12,9,18,2]
print(linearSearch(a,12))