import math
def is_prime(numCalc):
  if (numCalc<2):
    return False
  for i in range(2,numCalc-1):
    if numCalc%i==0:
      return False
  return True

def primeswo():
  for i in range(1,101):
    if is_prime(i):
      print(i)

def primeswi():
  first = int(input('First number: '))
  second = int(input('Second number: '))
  minNum = min(first, second)
  maxNum = max(first, second)
  for i in range(minNum, maxNum+1):
    if is_prime(i):
      print(i)

def interest():
  presentVal = float(input('Present value of account: '))
  interestVal = float(input('Monthly interest value in decimal form: '))
  timeMon = int(input('Time value in months: '))
  print(format(presentVal*(1.+interestVal)**timeMon, '.2f'))

def savingsInterest():
  presentVal = float(input('Present value of account: '))
  interestVal = float(input('Monthly interest value in decimal form: '))
  cost = float(input('Current cost of item: '))
  return (math.log(cost)-math.log(presentVal))/math.log((1.+interestVal))

def continuePlaying():
  game1 = input('Which lab would you like to see? Type A for first 100 primes, B for primes in a range, C for compound interest, and D for savings interest. ')
  game1 = game1.upper()
  if game1=='A':
    primeswo()
  if game1=='B':
    primeswi()
  if game1=='C':
    interest()
  if game1=='D':
    objectThing1 = input('What are you buying: ')
    numMon1 = savingsInterest()
    numMon1 = math.ceil(float(numMon1))
    if numMon1<12:
      print(str(numMon1) + ' months')
    else:
      print('To afford ' + objectThing1 +', it will take you ' + str(math.floor(numMon1/12)) + ' years and ' + str(numMon1%12) + ' months.')
  continuePlaying()

game = input('Which lab would you like to see? Type A for first 100 primes, B for primes in a range, C for compound interest, and D for savings interest. ')
game = game.upper()
if game=='A':
  primeswo()
if game=='B':
  primeswi()
if game=='C':
  interest()
if game=='D':
  objectThing = input('What are you buying: ')
  numMon = savingsInterest()
  numMon = math.ceil(float(numMon))
  if numMon<12:
    print(str(numMon) + ' months')
  else:
    print('To afford ' + objectThing +', it will take you ' + str(math.floor(numMon/12)) + ' years and ' + str(numMon%12) + ' months')
continuePlaying()
