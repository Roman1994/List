class List :

  first = None
  length = 0
  tail = None

  def __init__(self, item=None) :
    self.head = item
    self.rest = None
    if self.head != None :
      List.length += 1
    if List.length <= 1 :
      List.first = self
      List.tail = self

  def insertRight(self, newItem) :
    temp = List(newItem)
    List.tail.rest = temp
    List.tail = temp
  def insertLeft(self, newItem) :
    temp = List(newItem)
    temp.rest = List.first
    List.first = temp
  def insert(self, newItem, index=0) :
    if index == 0 :
      self.insertLeft(newItem)
    elif index == List.length-1 :
      self.insertRight(newItem)
    elif index >= List.length or index < 0 :
      print('error')
    else :
      temp         = List(newItem)
      preTemp      = self.__searchByIndex(index-1)
      postTemp     = self.__searchByIndex(index)
      preTemp.rest = temp
      temp.rest    = postTemp

  def __search(self, item) :
    if self.head == item :
      return self
    elif self.head != item and self.rest == None :
      return None
    else : self.rest.search(item)
  def __searchPreNode(self, node) :
    current = List.first
    while True :
      if current.rest == node :
        return current
      current = current.rest
  def __searchPostNode(self, node) :
    current = List.first
    while True :
      if current == node.rest :
        return current
      current = current.rest
  def __searchByIndex(self, index) :
    if index < 0 or index >= List.length :
      return None
    else :
      current = List.first
      i = 0
      while True :
        if i == index :
          return current
        i += 1
        current = current.rest

  def deleteHead(self) :
    List.first = List.first.rest
  def deleteLast(self) :
    List.tail = self if self.rest.rest == None\
                else self.rest.deleteLast()
  def delete(self, item) :
    node = self.__search(item)
    if node == None         : print('None')
    elif node == List.first : self.deleteHead()
    elif node == List.tail  : self.deleteLast()
    else :
      preNode      = self.__searchPreNode(node)
      postNode     = self.__searchPostNode(node)
      preNode.rest = postNode


  def display(self, start=None) :
    if start == None :
      current = List.first
    else :
      current = start
    print('(', end = '')
    while True :
      if current != List.tail :
        print(str(current.head), end=' ')
      else :
        print(str(current.head), end='')
        break
      current = current.rest
    print(')')