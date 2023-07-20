def add_booking_details():
  
  l=[]
  
  while True:
    try:
      A=int(input("Customer_id : "))
      l.append(A)
      break
    except:
      print("Customer id should be numeric") 

  while True: 
      B=input("Flight_code : ")
      if len(B)<=30:
        l.append(B)
        break
      else:
        print("Length of flight_code should not be greater than 30")
      
  import datetime  
  while True:
      try:
        C=input("Date of booking('YYYY-MM-DD') : ")
        datetime.datetime.strptime(C,'%Y-%m-%d')
        l.append(C)
        break 
      except:
         print("Incorrect data format, should be YYYY-MM-DD")
    
  while True:
    try:
      D=int(input("Fare : "))
      l.append(D)
      break
    except:
      print("Fare should be numeric ")

  l.append('Confirmed')
  return l
