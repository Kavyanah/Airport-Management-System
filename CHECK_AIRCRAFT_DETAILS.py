def checkAD():
    while True:
        try:
            A=int(input('Enter Acode: '))
            l=[A]
            return l
            break
        except:
            print('Acode must be in numeric')
