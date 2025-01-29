def reorder(set):
  i = -1
  temp_set = []
  for i in range(len(set) // 3):
    temp_set.append(set[-2 * i - 1])
    temp_set.append(set[-2 * i - 2])
    temp_set.append(set[i])
  if len(set) % 3 == 2:
    temp_set.append(set[-2 * i - 3])
    temp_set.append(set[-2 * i - 4])
  if len(set) % 3 == 1:
    temp_set.append(set[i + 1])
  return temp_set

n = int(input())
num_of_floors = sorted([int(i) for i in input().split()])
part1 = [num_of_floors[2 * i] for i in range((n + 1) // 2)]
part2 = [num_of_floors[2 * i + 1] for i in range(n // 2)]
ordered = [0] + reorder(part1) + list(reversed(reorder(part2))) + [0]
lighty_count = 0
for i in range(1, n + 1):
  shortest = min(ordered[i - 1], ordered[i + 1])
  if ordered[i] > shortest:
    lighty_count += (ordered[i] - shortest)
print(lighty_count)
