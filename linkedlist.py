class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
   
class linkedlist:
  def __init__(self):
    self.head=None
    self.size=0
  def append(self,data):
    if self.head==None:
      self.head=Node(data)
      return
    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=Node(data)
    self.size+=1
  def traverse(self):
    cn=self.head
    while cn.next is not None:
      print(cn.data,end="->")
      cn=cn.next
    print("None")
    print(cn.next)
  def search(self,data):
    if self.head is None:
      print('no elements in the ll')
      return
    cn=self.head
    ind=0
    while cn.next is not None:
      if cn.data==data:
          print(f'element {data} is found at {ind} index')
          return
          cn=cn.next
          ind+=1
      print("Element not found")
      def len(self):
        return self.size
      def insStart(self,data):
        obj=Node(data)
        obj.next=self.head
        self.head=obj
        self.size+=1
        def delStart(self):
          if self.head is None:
            return
          self.head=self.head.next
        def delLast(self):
          if self.head is None:
            return
          cn=self.head
          while cn.next.next is not None:
            cn=cn.next
          cn.next=None
          def insAt(self,data,pos):
            if pos>self.len()-1:
              print("invalid index")
              return
            if pos==0:
              self>insStart(data)
              return
            ind=0
ll=linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.traverse()
ll.search(50)
print(ll.len())
ll.insStrart()
traverse()
ll.delLast(20)

    