def findIsLeapYear():
  year = int(input('What year do you want to check for leap year?'))
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def isLeapYear():
  value = findIsLeapYear()
  if value:
    print('Yes! It is a leap year!')
  else:
    print('Nope! Not a leap year.')

def isTriangle(s1,s2,s3):
  if s1<=0 or s2<=0 or s3<=0:
    return False
  if s1>=s2+s3 or s2>=s1+s3 or s3>=s2+s1:
    return False
  return True

def typeOfTriangle(s1,s2,s3):
  if s1==s2==s3:
    return 'equilateral'
  elif s1==s2 or s2==s3 or s1==s3:
    return 'isosceles'
  else:
    return 'scalene'

def isATriangle():
  side1 = float(input('First side of the triangle?'))
  side2 = float(input('Second?'))
  side3 = float(input('Third?'))
  val = isTriangle(side1,side2,side3)
  if val:
    print('You have inputted the sides of a ' + typeOfTriangle(side1,side2,side3) + ' triangle!')
  else:
    print('Impossible! Not a triangle!')

for i in range(1,5):
  isLeapYear()
for i in range(1,5):
  isATriangle()
