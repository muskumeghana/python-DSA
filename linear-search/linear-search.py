 binarySearch(a,el):
    l=0
    r=len(a)-1
    while l<r:
        m=(l+r)//2
        if a[m]==el:
            return m
        eldefif a[m]<el:
            l=m
        else:
            r=m
b=[12,24,56,56,23,78,89]
print(binarySearch(b,56))