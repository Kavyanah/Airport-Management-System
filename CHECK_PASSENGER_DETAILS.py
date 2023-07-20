def checkPD():
    while True:
        try:
            A=int(input('Enter CId: '))
            l=[A]
            return l
            break
        except:
            print('CId must be in numeric')
