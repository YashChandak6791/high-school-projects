def missingWords(s, t):
  arrS = s.split()
  len_arr = len(arrS)
  arrT = t.split()
  arrFinal = []
  count = 0

  while(count < len_arr):
    if (len(arrT) == 0):
      arrFinal.append(arrS[0])
      arrS.pop(0)
      count += 1
    elif (arrS[0] == arrT[0]):
      arrS = arrS[1:]
      if (len(arrT) != 1):
        arrT = arrT[1:]
      else:
        arrT = []
      count += 1
    else:
      arrFinal.append(arrS[0])
      arrS = arrS[1:]
      count += 1
  return arrFinal

print(missingWords("Hello I am Yash", "I"))
