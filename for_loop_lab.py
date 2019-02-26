import random

def pro1():
  for i in range(0,10):
    print("Chocolate Muffins")

def pro2():
  for j in range(5):
    print(j)
  print('Ending: ',j)

def pro3():
  sum = 0
  for k in range(1,51):
    print(2*k)
    sum += 2*k
  print('Sum of first 50 numbers:',sum)
  sum = 0
  for l in range(0,11):
    sum += l**2
  print('Sum of first 10 squares:',sum)

def pro4():
  sum = 0
  for k in range(0,10):
    if(2**k>=20 and 2**k<=220):
      sum += 2**k
      print(2**k)

def pro5():
  min = int(input('First number: '))
  max = int(input('Second number: '))
  if (min > max):
    swap = max
    max = min
    min = swap
  if (min != max):
    for i in range(min,max+1):
      print(i)

def pro6():
  list6 = []
  for i in range(1,11):
    intInput = int(input('Number: '))
    list6.append(intInput)
  min = list6[1]
  max = list6[1]
  evenC = 0
  oddC = 0
  for j in list6:
    if j<min:
      min = j
    if j>max:
      max=j
    if j%2==0:
      evenC+=1
    else:
      oddC+=1
  print('Min: ' + str(min) + '\nMax: ' + str(max) + '\nNumber of even: ' + str(evenC) + '\nNumber of odd: ' + str(oddC))

def pro7():
  listL = ['Argentina','Brazil','Canada','Denmark','Equador','France','Guinea','Hungary','India','Jamaica']
  for i in listL:
    print(i)

def pro8():
  for i in range (1,11):
    num = random.randint(50,100)
    isEven = 'Even'
    if num%2!=0:
      isEven = 'Odd'
    print(str(num)+ ': ' + isEven)

print('\nProgram 1\n')
pro1()
print('\nProgram 2\n')
pro2()
print('\nProgram 3\n')
pro3()
print('\nProgram 4\n')
pro4()
print('\nProgram 5\n')
pro5()
print('\nProgram 6\n')
pro6()
print('\nProgram 7\n')
pro7()
print('\nProgram 8\n')
pro8()
