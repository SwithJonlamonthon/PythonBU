
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