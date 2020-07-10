"""""
def findDuplicate(num):
    tort = num[0]
    hare = num[0]
    while True:
        tort = num[tort]
        hare = num[num[hare]]
        if tort == hare: 
            break
    part1 = num[0]
    part2 = tort
    while part1 != part2:
        part1 = num[part1]
        part2 = num[part2]
    return part1
"""""



def findDuplicate(num):
  num.sort()
  for i in range(1, len(num)):
    if num[i] == num[i-1]:
      return num[i]

print(findDuplicate([2, 5, 6, 8, 1, 3, 2]))