def cookie():
  cookies1 = input('How many cookies would you like? ')
  cookies = float(cookies1)
  sugar = "%.2f" % (1.5/48*cookies)
  butter = "%.2f" % (1/48*cookies)
  flour = "%.2f" % (2.75/48*cookies)
  print('You will need ' + sugar + ' cups of sugar, ' + butter + ' cups of butter, and ' + flour + ' cups of flour.')

def classPercentages():
  maleNumberInput = input('Number of males in the class: ')
  femaleNumberInput = input('Number of females in the class: ')
  maleNumber = float(maleNumberInput)
  femaleNumber = float(femaleNumberInput)
  malePercentage = "%.2f" % (maleNumber/(maleNumber + femaleNumber)*100)
  femalePercentage = "%.2f" % (femaleNumber/(maleNumber + femaleNumber)*100)
  print('The males constitute ' + malePercentage + '% of the class and females constitute ' + femalePercentage + '% of the class.')

def populationSize():
  startingNumberInput = input('Starting number of organisms: ')
  startingNumber = float(startingNumberInput)
  dailyPopIncreaseInput = input('Average daily population increase: ')
  dailyPopIncrease = float(dailyPopIncreaseInput)
  numDaysInput = input('Number of days left to multiply: ')
  numDays = int(numDaysInput)
  print('Day Approximate       Population')
  for i in range(0, numDays):
    calc = "%.6f" % (startingNumber*((1+dailyPopIncrease/100)**i))
    print(str(i+1) + '                     ' + str(calc))

def continuePlaying():
  game1 = input('Which lab would you like to see? Type A for Cookies, B for Male and Female Percentages, and C for Population. ')
  game1 = game1.upper()
  if game1=='A':
   cookie()
  if game1=='B':
    classPercentages()
  if game1=='C':
    populationSize()
  continuePlaying()

game = input('Which lab would you like to see? Type A for Cookies, B for Male and Female Percentages, and C for Population. ')
game = game.upper()
if game=='A':
  cookie()
if game=='B':
  classPercentages()
if game=='C':
  populationSize()
continuePlaying()
