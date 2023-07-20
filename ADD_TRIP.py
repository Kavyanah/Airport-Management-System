def add_Trips():

    l = []

    while True:
        A = input("Enter Flight_code : ")
        if len(A) <= 30:
            l.append(A)
            break
        else:
            print("Length of flight_code should not be greater than 30")

    import datetime
    while True:
        try:
            B = input("Enter Departure Date(YYYY-MM-DD) : ")
            datetime.datetime.strptime(B, '%Y-%m-%d')
            B = B
            break
        except:
            print("Incorrect date format,Date should be like (YYYY-MM-DD)")

    while True:
        try:
            B1 = input("Enter Departure Time(HH:MM:SS) : ")
            datetime.datetime.strptime(B1, '%H:%M:%S')
            B1 = B1
            break
        except:
            print("Enter valid Time, enter in correct format(HH:MM:SS)")

    B2 = B + ' ' + B1  #concatenating date and time
    l.append(B2)

    while True:
        try:
            C = input("Enter Arrival Date(YYYY-MM-DD) : ")
            datetime.datetime.strptime(C, '%Y-%m-%d')
            C = C
            break
        except:
            print("Incorrect date format,Date should be like (YYYY-MM-DD)")

    while True:
        try:
            C1 = input("Enter Arrival Time(HH:MM:SS) : ")
            datetime.datetime.strptime(C1, '%H:%M:%S')
            C1 = C1
            break
        except:
            print("Enter valid Time, enter in correct format(HH:MM:SS)")

    C2 = C + ' ' + C1  
    l.append(C2)

    l.append('Delhi')

    while True:
        E = input("Enter Destination : ")
        if E.isalpha():
            if len(E) <= 30:
                l.append(E)
                break
            else:
                print("Length of destination should be less than 30")
        else:
            print("Destination should be in alphabet")

    while True:
        try:
            F = int(input("Enter Distance(Km): "))
            l.append(F)
            break
        except:
            print("Distance should numeric")

    t1 = datetime.datetime.strptime(B1, "%H:%M:%S")

    t2 = datetime.datetime.strptime(C1, "%H:%M:%S")

    s = t2 - t1
    l.append(str(s))

    while True:
        try:
            H = int(input("Price of efare : "))
            l.append(H)
            break
        except:
            print("Price  of efare should numeric")

    while True:
        try:
            I = int(input("Price of bfare : "))
            l.append(I)
            break
        except:
            print("Price of efare should numeric")

    while True:
        try:
            J = int(input("A_code : "))
            l.append(J)
            break
        except:
            print("A_code should numeric")
            
    status="Confirmed"
    l.append(status)

    return l
add_Trips()


