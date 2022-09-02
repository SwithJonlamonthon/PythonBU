"""
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


########## 4 ############
arr = ["Name ID","Name","Count","Status"],[]
test = list(arr)
print(test)

