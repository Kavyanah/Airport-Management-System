def checkT():
    l=[]
    while True:
        A = input("Enter Flight_code : ")
        if len(A) <= 30:
            l.append(A)
            break
        else:
            print("Length of flight_code should not be greater than 30")
    return l    
