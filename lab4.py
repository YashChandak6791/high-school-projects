import os
def addName():
  infile = open('main.txt', 'w')
  infile.write('Yash Chandak\n')
  infile.close()

def fileDisplay():
  infile = open('main.txt', 'r')
  print(infile.read())
  infile.close()

def writeHunnid():
  infile = open('main.txt', 'a')
  for i in range(1,101):
    if i%5==0:
      infile.write(str(i)+' By Fives\n')
    else:
      infile.write(str(i)+'\n')
  infile.close()

def createFriends():
  infile = open('friends.txt', 'w')
  infile.write('Yash 17\nJohn 3\nBill 6\nHerbert 8\nWilliam 15\nJosh 13\nRaviraj 4\nAmeer 12\nAmjad 12\nAadit 18\nAvi 21')
  infile.close()

def movingFriend(byeFriend):
  friendFile = open('friends.txt', 'r')
  infileTemp = open('temp.txt', 'w')
  for des in friendFile:
    if byeFriend != des[0:len(byeFriend)] or des[len(byeFriend)]!=' ':
      infileTemp.write(des)
  os.remove('friends.txt')
  os.rename('temp.txt', 'friends.txt')
  print('Adios!')

def bday():
  friendFile = open('friends.txt', 'r')
  tempFile = open('temp2.txt', 'w')
  des = friendFile.readline()
  while des != '':
    if 'Yash' == des[0:4]:
      age = int(des[5:])
      tempFile.write(des.replace(des[5:7], str(age+1)+''))
    else:
      tempFile.write(des)
    des = friendFile.readline()
  os.remove('friends.txt')
  os.rename('temp2.txt', 'friends.txt')

addName()
fileDisplay()
writeHunnid()
createFriends()
movingFriend(input('Who is moving away: '))
bday()
