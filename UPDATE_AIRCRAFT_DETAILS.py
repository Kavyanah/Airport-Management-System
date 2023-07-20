    A=input('Enter what to update[Acode,Airlines,Capacity,Model]: ')
    if A.lower()=='acode':
        B=int(input('Enter old Acode: '))
        C=int(input('Enter new Acode: '))
        l=[C,B]
    elif A.lower()=='airlines':
        B=input('Enter old Airline Name: ')
        C=input('Enter new Airline Name: ')
        l=[C,B]
    elif A.lower()=='capacity':
        B=int(input('Enter old Capacity: '))
        C=int(input('Enter new Capacity: '))
        l=[C,B]
    elif A.lower()=='model':
        B=input('Enter old Model: ')
        C=input('Enter new Model: ')
        l=[C,B]
    else:
        print('INVALID INPUT!')


