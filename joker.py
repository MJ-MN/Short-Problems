q = int(input())
for i in range(q):
  n, l, t = [int(j) for j in input().split()]
  position = 0
  max_count = 0
  for vi in input().split():
    excessive_time = t + -l // int(vi)
    if excessive_time < 0 or excessive_time > n - 1:
      continue
    if not position & (1 << excessive_time):
      max_count += 1
      position |= (1 << excessive_time)
  print(max_count)
