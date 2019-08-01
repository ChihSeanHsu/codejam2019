t = int(input())

for i in range(1, t + 1):
  n = input()
  a = int(n.replace('4', '3'))
  print('Case #{0}: {1} {2}'.format(i, a, int(n) - int(a)))
  
