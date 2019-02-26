import math
from random import randint, sample

def Cookout():
  numPeopleInput = input('How many people will be coming to the cookout? ')
  numPeople = float(numPeopleInput)
  numHotDogsInput = input('How many Hot Dogs will each person eat? ')
  numHotDogs = float(numHotDogsInput)
  print('You will need to purchase ' + str(math.ceil(numPeople*numHotDogs/10)) + ' package(s) of hot dogs and ' + str(math.ceil(numPeople*numHotDogs/8)) + ' package(s) of hot dog buns.')

def is_prime(numCalc):
  for i in range(2,numCalc-1):
    if numCalc%i==0:
      return False
  return True

def randomNumber():
  aInput = input('Lower bound of random numbers? ')
  a = int(aInput)
  bInput = input('Upper bound of random numbers? ')
  b = int(bInput)
  for i in range (1,50):
    print(randint(a,b))

def randomNumberNoRepeats():
  listRandom = sample(range(1,1000), 50)
  for i in range(1,50):
    print(listRandom[i-1])

def continuePlaying():
  game1 = input('\nWhich lab would you like to see? Type A for Hot Dogs, B for Prime Numbers, C for Random Numbers, and D for Random Numbers without Repeats. ')
  game1 = game1.upper()
  if game1=='A':
   Cookout()
  if game1=='B':
    numCalcUserInput1 = input('Which number would you like to check to see if prime? ')
    numCalcInput1 = int(numCalcUserInput1)
    returnVal1 = is_prime(numCalcInput1)
    if(returnVal1):
      print('Yes, ' + str(numCalcInput1) + ' is prime.')
    else:
      print('No, '+ str(numCalcInput1) + ' is not prime.')
  if game1=='C':
    randomNumber()
  if game1=='D':
    randomNumberNoRepeats()
  continuePlaying()

game = input('Which lab would you like to see? Type A for Hot Dogs, B for Prime Numbers, C for Random Numbers, and D for Random Numbers without Repeats. ')
game = game.upper()
if game=='A':
  Cookout()
if game=='B':
  numCalcUserInput = input('Which number would you like to check to see if prime? ')
  numCalcInput = int(numCalcUserInput)
  returnVal = is_prime(numCalcInput)
  if(returnVal):
    print('Yes, ' + str(numCalcInput) + ' is prime.')
  else:
    print('No, '+ str(numCalcInput) + ' is not prime.')
if game=='C':
  randomNumber()
if game=='D':
  randomNumberNoRepeats()
continuePlaying()
