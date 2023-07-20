def add_passenger():
  
  l=[]
  
  while True:
    try:
      A=int(input("Customer_id : "))
      l.append(A)
      break
    except:
      print("Customer_id should be numeric")
      
  while True: 
      B=input("First Name : ")
      if B.isalpha():
        if len(B)<=13:
          C=B.capitalize()
          break
        else:
          print("Name sholud not be greater then 13")
      else:
        print("Name should be alphabet")

  while True: 
      D=input("Last Name : ")
      if D.isalpha():
        if len(D)<=12:
          E=D.capitalize()
          break
        else:
          print("Name sholud not be greater then 12")
      else:
        print("Name should be alphabet")  
        
  F= C +' '+ E      #concatenating first and last name
  l.append(F)
      
  while True:
    try:
      G=int(input("Age : "))
      l.append(G)
      break
    except:
      print("Age should be numeric")

  while True:
    try:
        H= int(input("Please enter your 10 digit Phone Number : "))
        I=str(H)
        if len(I)==10:
          l.append(H)
          break
        else:
            print("Phone number should be of 10 digits")
    except:
        print("Phone number should be numeric")

      
  while True: 
    J=input("Gender(M/F/O) : ")
    if J.isalpha():
      K=J.capitalize()
      if K in ['M','F','O']:
          l.append(K)
          break
      else:
            print("Gender should be from given option")
    else:
      print("Gender should be alphabet")
  l.append('Activated')    
  return l
