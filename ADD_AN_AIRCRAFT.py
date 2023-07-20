def addAC():
  l=[]
  while True:
    try:
      A=int(input('Enter Acode: '))
      l.append(A)
      break
    except:
      print('Acode should be numeric')
  B=input('Enter Airline: ')
  while True:
    try:
      C=int(input('Enter Capacity: '))
      l.append(C)
      break
    except:
      print('Capacity should be numeric')
  D=input('Enter Model: ')

  l=[A,B,C,D,'F']
  return l
