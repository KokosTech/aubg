l = list(range(1,6))

print(l[2])

print(l[:3])

print(l[-1])

for i in l:
  print(i, end=' ')
print()

print(l)

l.extend([6, 7])

print(l)

n = 6
print(f"The element {n} is in the list: {n in l}")

# ==========================

odd = []
even = []

for x in range(1, 21):
  pass

# ==========================

def add_matrix(a: list, b: list):
  if len(a) != len(b) or len(a[0]) != len(b[0]):
    return
  
  result = []
  
  for i, x in enumerate(a):
    result.append([])
    for j, y in enumerate(x):
      result[i].append(y + b[i][j])
      
      
  return result
      
# def add_matrix_simplified(a: list, b: list):
#   if len(a) != len(b) or len(a[0]) != len(b[0]):
#     return
  
#   result = 
  

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
C = add_matrix(A, B)
print(C)

  
