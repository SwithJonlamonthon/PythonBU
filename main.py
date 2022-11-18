"""
######diamond#########
def diamond(n):
  space = (n-1) // 2
  for  i in range(1,n+1,2):
    print((space * " ")+(i * "*")+(space * " "))
    space = space - 1 
  space = 1
  for z in range(n-2,0,-2):
    print((space * " ")+(z * "*")+(space * " "))
    space = space +1
 
diamond(9)
"""
######LIMIT#########
"""
def limit(y):
  if y == 0:
    return 1
  else:
    return 1 / limit(y-1) + y

print(limit(9))

value = 0
for i in range(1,10):
  n = 1 / i+1
  value = n+ value
print(value)
"""

#####Prime number#########
"""
x = int(input("Insert number here: "))
y = input("Select mode o/e/b mean odd/even/both: ")
z = input("Do u want only prime numbers(y/n): ")
def primenum(pmode,mode,number):
  if pmode == "n":
    if mode == "b" and number != 0:
      value = number % 6
      if number % 5 == 0 and number != 5:
        print(f"{number} is not prime number")
      elif value == 1 or value == 5 or number == 2 or number == 3 :
        print(f"{number} is prime number")
      else:
        print(f"{number} is not prime number")
      return primenum(pmode,mode,number-1)
    if mode == "o" and number != 0:
      value = number % 2
      if value != 0:
        print("Please enter ODD number")
        return
      if number == 2 :
        print(f"{number} is prime number")
        return
      else:
        print(f"{number} is not prime number")
      return primenum(pmode,mode,number-2)
    if mode == "e" and number >= 0:
        value = number % 6
        if number % 2 == 0:
          print("Please enter EVEN number")
          return
        if value == 1 or value == 5 or number == 3:
          print(f"{number} is prime number")
        else:
          print(f"{number} is not prime number")
        return primenum(pmode,mode,number-2)
    else:
      return
  else:
      if mode == "b" and number != 0:
        value = number % 6
        if value == 1 or value == 5:
          print(f"{number} is prime number")
        elif number == 2 or number == 3:
          print(f"{number} is prime number")
        return primenum(pmode,mode,number-1)
      if mode == "o" and number != 0:
        value = number % 2
        if value != 0:
          print("Please enter ODD number")
          return
        if number == 2 :
          print(f"{number} is prime number")
          return
        return primenum(pmode,mode,number-2)
      if mode == "e" and number >= 0:
          value = number % 6
          if number % 2 == 0:
            print("Please enter EVEN number")
            return
          if value == 1 or value == 5:
            print(f"{number} is prime number")
          elif number == 3:
            print(f"{number} is prime number")
          return primenum(pmode,mode,number-2)
      else:
        return
    

        
     
primenum(z,y,x)
"""
###Week 2 ####
#### 1 #####
"""
arr = [5,7,9,11,13]
Sum = sum(arr)
print(Sum)
"""
"""
#### 2 #####
arr = [7,5,10,14,3,9,7]
arr2 = [9,10,3,4,2,5,7,1]
print("first arr length = ",len(arr))###Find length of 1st arr
print("2ed arr length = ",len(arr2))###Find length of 2ed arr
#### insert 15 to 1st arr
arr.insert(0,15)
print(arr)
####Find index 7 in 2ed arr
test = arr.index(7)
print(test)
test = arr2.index(7)
print(test)
#### Append 1 in 1st arr and 14 in 2ed arr
arr.append(1)
print(arr)
arr2.append(14)
print(arr2)
####Copy 1st arr to create 3rd arr
arr3 = arr
print(arr3)
##### Merge 3rd and 2ed
arr4 = arr3 + arr2
print(arr4)
##### Count 7 in 3rd arr
test = arr3.count(7)
print(test)
####Sort 3rd arr
arr3.sort()
print(arr3)
####Remove 7 in 3rd arr
value = arr3.count(7)
while value > 0 :
  for i in arr3:
    if i == 7:
      arr3.remove(i)
  value = value - 1
print(arr3)
##### copy 3rd arr to 4th arr
arr4 = arr3 + arr4
print(arr4)
####reversed 4th arr
test = list(reversed(arr4))
print(test)
#### Print 3rd arr and 4th arr
print(arr3)
print(arr4)
"""
"""
########## 3 ##########
arr = ["Name ID","Name","Count"]
#######Find length of arr
print(len(arr))
#######Find location of name arr
print(arr.index("19209"))
print(arr.index("Swith"))
print(arr.index("BKK"))
####### add value status in arr
arr.append("Status")
print(arr)
"""
"""
########## 4 ############
arr = ["Name ID","Name","Count","Status"],[],[],[],[],[]
test = list(arr)

test.append([])
test[1].append("value 1")
test[1].append("Rubber")
test[1].append(0)
test[1].append("Out of stock")
test[2].append("value 2")
test[2].append("Ruler")
test[2].append(5)
test[2].append("In stock")
test[3].append("value 3")
test[3].append("Pencil")
test[3].append(1)
test[3].append("In stock")
###print(len(test)) #### length of arr
###print(test)


##############5###################
test[4].append("value 4")
test[4].append("Pen")
test[4].append(10)
test[4].append("In stock")
test[5].append("value 5")
test[5].append("Colour pencil")
test[5].append(5)
test[5].append("In stock")
test[6].append("value 6")
test[6].append("A4 Paper")
test[6].append(0)
test[6].append("Out of stock")
###print(test)
"""
"""
for i in range(0,len(test)):
  if test[i][3] == "In stock":
    print(test[i])

for i in range(0,len(test)):
  if test[i][3] == "Out of stock":
    print(test[i])

for i in range(0,len(test)):
  if test[i][1] == "Ruler":
    test [i][2] = test [i][2] - 1
  if test[i][1] == "Pencil":
    test [i][2] = test [i][2] - 1
  if test[i][1] == "Pen":
    test [i][2] = test [i][2] - 2
  if test[i][1] == "Colour pencil":
    test [i][2] = test [i][2] - 1
  if test[i][2] == 0:
    test [i][3] = "Out of stock"
print(test)
"""


####Lab 3#########
"""
class filo:

  def __init__(self, arr):
    self.arr = arr

  def push(self, value):
    arr = self.arr
    arr.append(value)

  def pop(self):
    arr = self.arr
    arr.pop()

  def show(self):
    print(str(self.arr))

### First in
print("FILO")
arr = filo([])
arr.push("a")
arr.show()
arr.push("b")
arr.show()
arr.push("c")
arr.show()
arr.push("d")
arr.show()
arr.push("e")
arr.show()
arr.push("f")
arr.show()
### Last out
arr.pop()
arr.show()
arr.pop()
arr.show()
arr.pop()
arr.show()
arr.pop()
arr.show()
arr.pop()
arr.show()
arr.pop()
arr.show()

class fifo:

  def __init__(self, arr):
    self.arr = arr

  def push(self, value):
    arr = self.arr
    arr.append(value)

  def pop(self):
    arr = self.arr
    arr.pop(0)

  def reverse(self):
    Rarr = []
    arr = self.arr
    for i in range(len(arr)):
      Rarr.append(arr.pop())
    self.arr = Rarr
  

  def show(self):
    print(str(self.arr))
### First in
print("FIFO")
arr = fifo([])
arr.push("a")
arr.show()
arr.push("b")
arr.show()
arr.push("c")
arr.show()
arr.push("d")
arr.show()
arr.push("e")
arr.show()
arr.push("f")
arr.show()
print("Reverse ")
arr.reverse()
arr.show()
### First out

arr.pop()
arr.show()
arr.pop()
arr.show()
arr.pop()
arr.show()
arr.pop()
arr.show()
arr.pop()
arr.show()
arr.pop()
arr.show()
"""
"""
class intopost:
  def __init__(self,str):
    self.str = str

  def create(self):
    output = []
    stack = []
    op = set(['+','-','*','/'])
    Str = self.str 
    for cha in Str :
      if cha not in op:
        if cha == '(':
          if stack == []:
            stack.append(cha)
          else:
            output.append(stack.pop())
            stack.append(cha)
        elif cha == ')':
          output.append(stack.pop())  
        else:
          output.append(cha)
      else:
        stack.append(cha)
     
    
    while stack != []:
        output.append(stack.pop())
    for i in output:
      if i == '(':
        continue
      print(i,end = '')
        
        
    

      
test = intopost('A+(B*C)') 
test.create()
"""

"""
####Lab 4########
class cylin:
    def cal(height,radius):
        value = 3.16 *height * radius**2
        return round(value,2)
                    
x = cylin.cal(10,5)
y = cylin.cal(13,7)
print("𝑣𝑜𝑙𝑢𝑚𝑒 𝑜𝑓 𝑐𝑦𝑙𝑖𝑛𝑑𝑒𝑟 :",x)
print("𝑣𝑜𝑙𝑢𝑚𝑒 𝑜𝑓 𝑐𝑦𝑙𝑖𝑛𝑑𝑒𝑟 :",y)

class pyramid:
    def cal(height,width,length):
        value =  (height*width*length) / 3
        return round(value,2)

x = pyramid.cal(17,7,10)
print("𝑣𝑜𝑙𝑢𝑚𝑒 𝑜𝑓 𝑝𝑦𝑟𝑎𝑚𝑖𝑑 :",x)


class Node:
     def __init__(self, data, next = None, previous = None):
        self.data = data;
        self.next = next;
        self.previous = previous

class li:## For init list
    def __init__(self):
        self.head = None
     
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
            
    # for inserting at end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp
        
    # deleting a node from linked list
    def delete(self, data):
        temp = self.head
        if(temp.next != None):
            # if head node is to be deleted
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
                    # if element to be deleted is in between
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    # if element to be deleted is the last element
                    temp.previous.next = None
                    temp.previous = None
                return
        
        if (temp == None):
            return
        
    # for printing the contents of linked lists
    def printdll(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=' ')
            temp = temp.next
        
     
            
            
dll = li()
dll.insertAtStart(1)
dll.insertAtStart(2)
dll.insertAtEnd(3)
dll.insertAtStart(4)
dll.printdll()
dll.delete(2)
print()
dll.printdll()
        

"""
"""
#########Lab 5############
class node:

    def __init__(self, value):
        self.value = value
        self.next = ""
        self.back = ""


class linlist:

    def __init__(self):
        self.head = None

    def append(self, val):
        newdata = node(val)
        if self.head == None:
            self.head = newdata
            self.back = None
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = newdata

    def display(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next


test = linlist()
test.append(1)
test.append(2)
test.append(2)
test.display()

class bst:

  def __init__(self, item):
    self.left = self.right = None
    self.var = item

    


def add(node, data):
  if node == None:  ## For create new node when it don't have any child
    return bst(data)
  else:  ## for check node condition
    if node.var == data:
      return node
    elif node.var < data:
      node.right = add(node.right, data)  ##For check next node
    else:
      node.left = add(node.left, data)  ##For check next node

  return node  ##For recursive


def heighttree(node):
  root = node  ## for pointer on root
  htr = 0
  while (node):  ## for left subtree
    htr = htr + 1
    node = node.right
  #print("Height right side is ",htr)
  ht = 0
  node = root  ## For reset Pointer to root
  while (node):  ## for right subtree
    ht = ht + 1
    node = node.left
  #print("Height left side is ",ht)
  if htr != ht:
    print("This tree is unbalanced")
    if htr > ht :
      return htr
    else:
      return ht
  else:
    print("This tree is balanced")


def minMax(arr):
  max = arr[0]
  min = arr[0]
  for i in range(len(arr)):
    if max < arr[i]:
      max = arr[i]
    if min > arr[i]:
      min = arr[i]
  print("Max value is : ",max)
  print("Min value is : ",min)
  
def search(node,data):
    if node.var == data:
        print("IT has")
    elif node.var != data:
        if node.var == data:
            return node
        elif node.var < data:
            node.right = search(node.right, data)  ##For check next node
        else:
            node.left = search(node.left, data)  ##For check next node

        return node ##For recursive
    else:
        print("It doesn't have")

arr = []
def show (node):
    if node:
      arr.append(node.var)
      show(node.left)
      show(node.right)
def deleteDeepest(node,d_node):
    q = []
    q.append(node)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def delete(node,data):
  if node == None :
      return None
  if node.left == None and node.right == None:
        if node.var == data :
            return None
        else :
            return node
  key_node = None
  q = []
  q.append(node)
  temp = None
  while(len(q)):
      temp = q.pop(0)
      if temp.var == data:
          key_node = temp
      if temp.left:
          q.append(temp.left)
      if temp.right:
          q.append(temp.right)
  if key_node :
      x = temp.var
      deleteDeepest(node,temp)
      key_node.var = x
  
  return node
  
    
      



r = bst(50)
r = add(r, 25)
r = add(r, 35)
r = add(r,60)
r = delete(r,35)
show(r)
print(arr)
minMax(arr)


"""
"""
###Lab6
class graph:

    def __init__(self):
        self.value = [["-", "A"], ["A", "0"]]

    def show(self):
        x = len(self.value)
        # for i in range(x):
        #   print("\n")
        #   for j in range(x):
        #     print(self.value[i][j],"  ",end="")
        for i in range(x):
            print(self.value[i])

    def create(self, node):
        x = len(self.value)
        for i in range(x):
            if self.value[i][0] == "-":
                self.value[i].append(node)
            elif self.value[i][0] != "":
                self.value[i].append("0")
        self.value.append([node])
        for i in range(x):
            self.value[-1].append("0")

    def connect(self, fnode, snode):
        x = len(self.value)
        indexcol = self.value[0].index(fnode)
        indexscol = self.value[0].index(snode)
        for i in range(x):
            if (self.value[i][0] == snode):
                self.value[i][indexcol] = "1"
                break

        for y in range(x):
            if (self.value[y][0] == fnode):
                self.value[y][indexscol] = "1"
                break
    def disconnect(self, fnode, snode):
        x = len(self.value)
        indexcol = self.value[0].index(fnode)
        indexscol = self.value[0].index(snode)
        for i in range(x):
            if (self.value[i][0] == snode):
                self.value[i][indexcol] = "0"
                break

        for y in range(x):
            if (self.value[y][0] == fnode):
                self.value[y][indexscol] = "0"
                break




### EX 1
table = graph()
table.create("B")
table.create("C")
table.create("D")
table.connect("A", "B")
table.connect("A", "C")
table.connect("B", "C")
table.connect("C", "D")
##table.show()

###Ex2
table2 = graph()
table2.create("B")
table2.create("C")
table2.create("D")
table2.create("E")
table2.create("F")
table2.connect("A", "B")
table2.connect("A", "C")
table2.connect("A", "F")
table2.connect("C", "D")
table2.connect("D", "E")
table2.connect("E", "F")
##table2.show()

###Ex3
table2.disconnect("C","F")
table2.disconnect("A","B")
table2.disconnect("C","D")
###table2.show()
table2.connect("A", "E")
table2.connect("B", "C")
table2.connect("D", "F")
table2.show()

"""
"""
###Lab7

def bubbleSort(arr):

  n = len(arr)

  for i in range(n):
    for j in range(0, n - i - 1):

      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]



def selectionSort(array, size):
     
    for s in range(size):
        min_idx = s
         
        for i in range(s + 1, size):
             
   
            if array[i] < array[min_idx]:
                min_idx = i
 
        (array[s], array[min_idx]) = (array[min_idx], array[s])


def insertion_sort(list1): 
   
        
        for i in range(1, len(list1)): 
   
            a = list1[i] 
   
            
            j = i - 1 
           
            while j >= 0 and a < list1[j]: 
                list1[j + 1] = list1[j] 
                j -= 1 
                 
            list1[j + 1] = a 

arr = [2, 1, 10, 23, 0]
size = len(arr)
selectionSort(arr, size)
print("Selection sort")
print(arr)
arr = [ 10, 2, 1, 6 ]
bubbleSort(arr)
print("Bubble sort")
print(arr)
arr = [ 7, 2, 1, 6 ] 
insertion_sort(arr)
print("Insertion sort")
print(arr)

####For performance it all have same performance because they all
####have time complexity O(n)
###For resources management for me i think bubble sort is the best 
### Because they just swap value in list it is really simple

"""
""""
### Sorting part 2

def mergeSort(arr):
  if len(arr) > 1:
    divide = int((len(arr) / 2))
    left = arr[:divide]
    right = arr[divide:]
    
    mergeSort(left) 
    mergeSort(right)
    i = 0
    j = 0 
    k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i = i+1
      else:
        arr[k] = right[j]
        j = j+1
      k = k+1
    while i < len(left):
      arr[k] = left[i]
      i = i+1 
      k = k+1
    while j < len(right):
      arr[k] = right[j]
      j = j+1
      k = k+1
      
list = [29,10,14,37,14,20,7,16]
mergeSort(list)
print(list)

"""

####LAB 8

Value = [7,10,12,14,16,20,29,37]

def lisearch(arr,data):
  for value in range(len(arr)):
    if arr[value] == data:
      print(f"Data is in position : {value+1} ({data})")
      check = False
      break
    else:
      check = True
    
  if check == True:
    print("You input is nothing")
    
    
lisearch(Value,14)


def bisearch(arr,data):
  left = 0
  right = len(arr) 
  if data not in arr:
    print("You input is nothing")
    return 
  while True:
    median = int((left + (right - 1)) / 2)
    if arr[median] > data:
      median = median - 1
      left = median
    elif arr[median] < data:
      median = median + 1
    elif arr[median] == data:
      print(f"Data is in position : {median+1} ({data})")
      break
    left = median
  



bisearch(Value,37)