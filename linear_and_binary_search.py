def binarySearch(varB, listB):
  listB = sorted(listB)
  mini = 0
  maxa = len(listB)
  while mini<maxa:
    mid = mini + (maxa-mini)//2
    if varB == listB[mid]:
      return True
    elif varB>listB[mid]:
      if mini == mid:
        break
      mini = mid
    elif varB<listB[mid]:
      maxa = mid
  return False

def linearSearch(varL, listL):
  for i in listL:
    if varL==i:
      return True
  return False

listA = [1,2,3,5,8,89,55,34,21,13]
varToCheck = int(input('What number do you want to check if in this list?'))
print('With binary search,', binarySearch(varToCheck, listA))
print('With linear search,', linearSearch(varToCheck, listA))
#linearSearch(varToCheck, listA)
