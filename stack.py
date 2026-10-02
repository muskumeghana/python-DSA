class stack:
  def __init__(self, size):
    self._a = []
    self._top = None
    self._size = size
  def push(self,data):
    if self._top is not None:
      if self._top+1==self._size:
        print('stack overflow')
        return

    if self._top is None:
      ar=[]
      ar.append(data)
      self._a=ar
      self._top=0
    else:
      ar=[]
      for i in self._a:
        ar.append(i)
      ar.append(data)
      self._a=ar
      self._top+=1
  def peek(self):
    if self._top is None:
      return "No elements"
    return self._a[self._top]
  def append(self,ar,data):
    if self._top is None:
      self._a.append(data)
    else:
      self._a.append(data)
      self._top+=1
  def pop(self):
    if self._top is None:
      return "stack Underflow"
    ar=[None for i in range(self._top)]
    for i in range(self._top):
      ar[i]=self._a[i]
    temp=self._a[-1]
    self._top -= 1
    self._a=ar
    if self._top==-1:
      self._top=None

    return temp