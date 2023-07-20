import mysql.connector
import datetime
import ADD_AN_AIRCRAFT
import CHECK_AIRCRAFT_DETAILS
import ADD_TRIP
import CHECK_TRIP_DETAILS
import ADD_PASSENGER
import CHECK_PASSENGER_DETAILS
import ADD_BOOKING
import CHECK_BOOKING_DETAILS
from prettytable import from_db_cursor

cnx=mysql.connector.connect(user='root', password='kavyansh@cs', host='127.0.0.1')
cur=cnx.cursor()
cur.execute('use ams')

print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')
print('*******************************************************')            
print(' !!!WELCOME TO K.A.D. AIRPORT MANAGEMENT SYSTEM!!!')
print('*******************************************************') 
print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')
menu1='''
 1.AIRCRAFT DETAILS
 2.TRIPS
 3.CUSTOMERS DETAILS
 4.BOOKING DETAILS
 5.EXIT
'''
menu2='''
 1.ADD AN AIRCRAFT
 2.CHECK AIRCRAFT DETAILS
 3.UPDATE AIRCRAFT DETAILS
 4.SET AN AIRCRAFT AS NOT FUNCTIONING
 5.EXIT
'''
menu3='''
 1.ADD A TRIP
 2.CHECK TRIP DETAILS
 3.UPDATE TRIP DETAILS
 4.CANCEL A TRIP
 5.EXIT
'''
menu4='''
 1.ADD A CUSTOMER
 2.CHECK CUSTOMER DETAILS
 3.UPDATE CUSTOMER DETAILS
 4.DEACTIVATE A CUSTOMER
 5.EXIT
'''
menu5='''
 1.ADD A BOOKING
 2.CHECK BOOKING DETAILS
 3.UPDATE BOOKING DETAILS
 4.CANCEL A BOOKING
 5.EXIT
'''
creaters='''
 ***CODERS***
 1.Kavyansh
 2.Akshat Swami
 3.Deepika

 [CLASS 12TH SCIENCE]

 INSTRUCTOR: MR.Pawan Sihag
'''
 
while True:
  print(menu1)
  ch1=input('Enter your choice: ')
  if ch1=='1':
    while True:
      print(menu2)
      ch2=input('Enter your choice: ')
      if ch2=='1':
        l=ADD_AN_AIRCRAFT.addAC()
        cur.execute('insert into aircraft_details values(%s,%s,%s,%s,%s)',l)
        cnx.commit()
      elif ch2=='2':
          s=input('Press "1" for all data and "2" for specific data search with Acode: ')
          if s=='2':
            l=CHECK_AIRCRAFT_DETAILS.checkAD()
            cur.execute('select * from aircraft_details where Acode=%s',l)
            data=cur.fetchall()
            if len(data)!=0:
                cur.execute('select * from aircraft_details where Acode=%s',l)
                mytable = from_db_cursor(cur)
                print(mytable)
            else:
              print('NO SUCH DATA FOUND!')
          elif s=='1':
            cur.execute('select * from aircraft_details')
            mytable = from_db_cursor(cur)
            print(mytable)
          else:
            print('INVALID CHOICE')
      elif ch2=='3':
          cur.execute('select * from aircraft_details')
          mytable = from_db_cursor(cur)
          print(mytable)

          while True:
            print()
            print('1.Acode\n2.Airlines\n3.Capacity\n4.Model\n5.Exit')
            print()
            try:
              A=input('Enter your choice: ')
              if A=='1':
                try:
                  while True:
                    B=int(input('Enter Acode: '))
                    cur.execute('select * from aircraft_details where Acode=%s',[B])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("ACODE DOESN'T EXIST!")
                      break
                    C=int(input('Enter new Acode: '))                  
                    l=[C,B]
                    cur.execute('update aircraft_details set Acode=%s where Acode=%s',l)
                    cnx.commit()
                    print('DONE')
                    break
                except:
                  print('VALUE SHOULD BE INTEGER!')
              elif A=='2':
                try:
                  while True:
                    B=int(input('Enter Acode: '))
                    cur.execute('select * from aircraft_details where Acode=%s',[B])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("ACODE DOESN'T EXIST!")
                      break
                    
                    C=input('Enter new Airline Name: ')
                    l=[C,B]
                    cur.execute('update aircraft_details set Airlines=%s where Acode=%s',l)
                    cnx.commit()
                  break
                except:
                  print('Acode SHOULD BE INTEGER!')
              elif A=='3':
                try:
                  while True:
                    B=int(input('Enter Acode: '))
                    cur.execute('select * from aircraft_details where Acode=%s',[B])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("ACODE DOESN'T EXIST!")
                      break
                    
                    C=int(input('Enter new Capacity: '))
                    l=[C,B]
                    cur.execute('update aircraft_details set capacity=%s where Acode=%s',l)
                    cnx.commit()
                    break
                except:
                  print('VALUE SHOULD BE INTEGER!')
              elif A=='4':
                try:
                  while True:
                    B=int(input('Enter Acode: '))
                    cur.execute('select * from aircraft_details where Acode=%s',[B])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("ACODE DOESN'T EXIST!")
                      break
                    
                    C=input('Enter new Model: ')
                    l=[C,B]
                    cur.execute('update aircraft_details set model=%s where Acode=%s',l)
                    cnx.commit()
                    break
                except:
                  print('Acode SHOULD BE INTEGER!')
              elif A=='5':
                break
              else:
                print('INVALID INPUT!')
            except:
              print('Enter input in correct datatype')
      elif ch2=='4':
              cur.execute('select * from aircraft_details')
              mytable = from_db_cursor(cur)
              print(mytable)
              try:
                print()
                A=int(input('Enter Acode of the aircraft u want to set as not functioning(NF): '))
                l=[A]
                cur.execute('select * from aircraft_details where Acode=%s',l)
                data=cur.fetchall()
                if len(data)!=0:
                    cur.execute('update aircraft_details set status="NF" where Acode=%s',l)
                    cnx.commit()
                    print('STATUS CHANGED OF AIRCRAFT WITH AIRCODE',A)
                else:
                    print('NO SUCH DATA FOUND!')
              except:
                print()
                print('Enter integer only')
      elif ch2=='5':
            break
      else:
            print('INVALID INPUT')
  elif ch1=='2':      
        while True:
          print(menu3)
          ch3=input('Enter your choice: ')
          if ch3=='1':
            l=ADD_TRIP.add_Trips()
            cur.execute('insert into trips values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',l)
            cnx.commit()
            print('DONE')
          elif ch3=='2':
            s=input('Press "1" for all data and "2" for specific data search with Flight_code: ')
            if s=='2':
              l=CHECK_TRIP_DETAILS.checkT()
              cur.execute('select * from trips where flight_code=%s',l)
              data=cur.fetchall()
              if len(data)!=0:
                cur.execute('select * from trips where flight_code=%s',l)
                mytable = from_db_cursor(cur)
                print(mytable)
              else:
                 print('NO SUCH DATA FOUND!')
            elif s=='1':
              cur.execute('select * from trips')
              mytable = from_db_cursor(cur)
              print(mytable)
            else:
              print('INVALID CHOICE')
          elif ch3=='3':
            cur.execute('select * from trips')
            mytable = from_db_cursor(cur)
            print(mytable)
            print()
            
            l=[]   #[old ,new]
            while True:
              print("1.Flight_code ")
              print("2.Departure date and time")
              print("3.Arrival date and time")
              print("4.Destination")
              print("5.Distance")
              print("6.Price of efare")
              print("7.Price of bfare")
              print("8.A_code")
              print("9.Exit\n")
              ch=input("Enter your choice which you want to update : ")
              
              if ch=='1':
                while True:
                  A=input("Enter old flight_code : ")
                  if len(A)<=30:
                    A=A
                    cur.execute('select * from trips where flight_code=%s',[C])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("FLIGHT_CODE DOESN'T EXIST!\n")
                    break
                  else:
                    print("Length of flight code should not be greater than 30")
                  B=input("Enter new flight code : ")
                  if len(B)<=30:
                    B=B 
                    break
                  else:
                    print("Length of flight code should not be greater than 30")
                  l=[B,A] 
                  cur.execute('update trips set flight_code=%s where flight_code=%s',l)
                  cnx.commit()        

              elif ch=='2':
                while True:
                    C = input("Enter flight_code : ")
                    cur.execute('select * from trips where flight_code=%s',[C])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("FLIGHT_CODE DOESN'T EXIST!\n")
                      break
                    try:
                      D = input("Enter new Departure Date(YYYY-MM-DD) : ")
                      datetime.datetime.strptime(D, '%Y-%m-%d')
                      D = D
                    except:
                        print("Incorrect date format,Date should be like (YYYY-MM-DD)")
                        break
                    try:
                        D1 = input("Enter new Departure Time(HH:MM:SS) : ")
                        datetime.datetime.strptime(D1, '%H:%M:%S')
                        D1 = D1
                    except:
                        print("Enter valid Time, enter in correct format(HH:MM:SS)")
                        break
                    D2 = D + ' ' + D1  #concatenating date and time
                    l=[D2,C]
                    cur.execute('update trips set departure=%s where flight_code=%s',l)
                    cnx.commit()
                    print('DONE')

              elif ch=='3':
                while True:
                    E=input('Enter Flight_code: ')
                    cur.execute('select * from trips where flight_code=%s',[E])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("FLIGHT_CODE DOESN'T EXIST!\n")
                      break
                    try:
                      F = input("Enter new Arrival Date(YYYY-MM-DD) : ")
                      datetime.datetime.strptime(F, '%Y-%m-%d')
                      F = F
                    except:
                        print("Incorrect date format,Date should be like (YYYY-MM-DD)")
                        break
                    try:
                        F1 = input("Enter new Arrival Time(HH:MM:SS) : ")
                        datetime.datetime.strptime(F1, '%H:%M:%S')
                        F1 = F1
                    except:
                        print("Enter valid Time, enter in correct format(HH:MM:SS)")
                        break
                    F2 = F + ' ' + F1  #concatenating date and time
                    l=[F2,E]
                    cur.execute('update trips set arival=%s where flight_code=%s',l)
                    cnx.commit()
                    print('DONE')

                
              elif ch=='4':
                while True:
                    G=input('Enter Flight_code: ')
                    cur.execute('select * from trips where flight_code=%s',[G])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("FLIGHT_CODE DOESN'T EXIST!\n")
                      break
                    H=input("Enter new destination : ")
                    if len(H)<=25:
                      H=H
                    else:
                      print("Length of destination sholud not be greater than 25 ")
                      break
                    l=[H,G]
                    cur.execute('update trips set destination=%s where flight_code=%s',l)
                    cnx.commit()
                    print('DONE')
                    break

              elif ch=='5':
                while True:
                    I=input('Enter Flight_code: ')
                    cur.execute('select * from trips where flight_code=%s',[I])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("FLIGHT_CODE DOESN'T EXIST!\n")
                      break
                    try:
                        J=int(input("Enter new distance : "))
                        J=J
                    except:
                        print("Distance should numeric")
                        break
                    l=[J,I]
                    cur.execute('update trips set distance=%s where flight_code=%s',l)
                    cnx.commit()
                    print('DONE')
                    break
                
              elif ch=='6':
                while True:
                    K= input('Enter Flight_code: ')
                    cur.execute('select * from trips where flight_code=%s',[K])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("FLIGHT_CODE DOESN'T EXIST!\n")
                      break
                    try:
                       L=int(input("Enter new efare : "))
                       L=L
                    except:
                       print("Price  of efare should numeric")
                       break
                    l=[L,K]
                    cur.execute('update trips set efare=%s where flight_code=%s',l)
                    cnx.commit()
                    print('DONE')
                    break
                                      
              elif ch=='7':
                while True:
                    M=input('Enter Flight_code: ')
                    cur.execute('select * from trips where flight_code=%s',[M])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("FLIGHT_CODE DOESN'T EXIST!\n")
                      break
                    try:
                        N = int(input("Enter new bfare : "))
                        N=N
                    except:
                        print("Price of efare should numeric")
                        break
                    l=[N,M]
                    cur.execute('update trips set bfare=%s where flight_code=%s',l)
                    cnx.commit()
                    print('DONE')
                    break
                      
              elif ch=='8':
                      
                while True:
                    try:
                        O=input('Enter flight_code: ')
                        cur.execute('select * from trips where flight_code=%s',[O])
                        check=cur.fetchall()
                        if len(check)==0:
                          print("FLIGHT_CODE DOESN'T EXIST!\n")
                          break
                        P = int(input("Enter new Acode : "))
                        P=P
                        cur.execute('select * from aircraft_details where Acode=%s',[P])
                        check1=cur.fetchall()
                        if len(check1)==0:
                          print("ACODE DOESN'T EXIST!\n")
                          break
                    except:
                        print("Acode should numeric")
                        break
                    l=[P,O]
                    cur.execute('update trips set Acode=%s where flight_code=%s',l)
                    cnx.commit()
                    print('DONE')
                    break
              elif ch=='9':
                break   
          elif ch3=='4':
              cur.execute('select * from trips')
              mytable = from_db_cursor(cur)
              print(mytable)
              print()
              A=input('Enter Flight_code of the trip u want to cancel: ')
              l=[A]
              cur.execute('select * from trips where Flight_code=%s',l)
              data=cur.fetchall()
              if len(data)!=0:
                  cur.execute('update trips set status="Cancelled" where Flight_code=%s',l)
                  cnx.commit()
                  print('TRIP CANCELLED WITH FLIGHT_CODE',A)
              else:
                  print('NO SUCH DATA FOUND!')
          elif ch3=='5':
            break
          else:
            print('INVALID INPUT')

  elif ch1=='3':
    while True:
      print(menu4)
      ch2=input('Enter your choice: ')
      if ch2=='1':
        l=ADD_PASSENGER.add_passenger()
        cur.execute('insert into passenger_details values(%s,%s,%s,%s,%s,%s)',l)
        cnx.commit()
      elif ch2=='2':
          s=input('Press "1" for all data and "2" for specific data search with CId: ')
          if s=='2':
            l=CHECK_PASSENGER_DETAILS.checkPD()
            cur.execute('select * from passenger_details where Cid=%s',l)
            data=cur.fetchall()
            if len(data)!=0:
                cur.execute('select * from passenger_details where Cid=%s',l)
                mytable = from_db_cursor(cur)
                print(mytable)
            else:
              print('NO SUCH DATA FOUND!')
          elif s=='1':
            cur.execute('select * from passenger_details')
            mytable = from_db_cursor(cur)
            print(mytable)
          else:
            print('INVALID CHOICE')
      elif ch2=='3':
        # update customers detail

        while True:
          print("1.Name") 
          print("2.Age")
          print("3.Phone number")
          print("4.Gender")
          print("5.Exit\n")
          ch=input("Enter your choice : ")
             
          if ch=='1':
            while True:
              try:
                A=int(input("Enter your customer id : "))
                A=A
                cur.execute('select * from passenger_details where cid=%s',[A])
                check=cur.fetchall()
                if len(check)==0:
                  print("CId DOESN'T EXIST!\n")
                  break
              except:
                print("Customer id should be numeric")
                break

              D=input("Enter new Name : ")
              if D.isalpha():
                if len(D)<=13:
                  D.capitalize()
                else:
                  print("First Name sholud not be greater then 13")
                  break
              else:
                print("Name should be alphabet")
                break
                
              l=[D,A]
              cur.execute('update passenger_details set Name=%s where cid=%s',l)
              cnx.commit()
              print('DONE')
              break
              
          elif ch=='2':
            while True:
              try:
                A=int(input("Enter your customer id : "))
                A=A
                cur.execute('select * from passenger_details where cid=%s',[A])
                check=cur.fetchall()
                if len(check)==0:
                  print("CId DOESN'T EXIST!\n")
                  break
              except:
                print("Customer id should be numeric")
                break
              try:
                E=int(input("New Age : "))
                E=E

              except:
                print("Age should be numeric")
                break
              l=[E,A]
              cur.execute('update passenger_details set Age=%s where cid=%s',l)
              cnx.commit()
              print('DONE')
              break
            
          elif ch=='3':
              
              while True:
                try:
                  A=int(input("Enter your customer id : "))
                  A=A
                  cur.execute('select * from passenger_details where cid=%s',[A])
                  check=cur.fetchall()
                  if len(check)==0:
                    print("CId DOESN'T EXIST!\n")
                    break
                except:
                  print("Customer id should be numeric")
                  break
                try:
                  F= int(input("Please enter your new 10 digit Phone Number : "))
                  G=str(F)
                  if len(G)==10:
                    G=G
                  else:
                    print("Phone number should be of 10 digits")
                    break
                except:
                  print("Phone number should be numeric")
                  break
                l=[G,A]
                cur.execute('update passenger_details set Phone_number=%s where cid=%s',l)
                cnx.commit()
                print('DONE')
                break
                    
          elif ch=='4':
              while True: 
                  try:
                    A=int(input("Enter your customer id : "))
                    A=A
                    cur.execute('select * from passenger_details where cid=%s',[A])
                    check=cur.fetchall()
                    if len(check)==0:
                      print("CId DOESN'T EXIST!\n")
                      break
                  except:
                    print("Customer id should be numeric")
                    break
                  H=input("Enter Gender(M/F/O) : ")
                  if H.isalpha():
                      I=H.capitalize()
                      if I in ['M','F','O']:
                        I=I
                      else:
                        print("Gender should be from given option")
                        break
                  else:
                    print("Gender should be alphabet")
                    break
                  l=[I,A]
                  cur.execute('update passenger_details set gender=%s where cid=%s',l)
                  cnx.commit()
                  print('DONE')
                  break
              
          elif ch=='5':
              break
      elif ch2=='4':
              cur.execute('select * from passenger_details')
              mytable = from_db_cursor(cur)
              print(mytable)
              print()
              A=input('Enter CId of the customer u want to deactivate: ')
              l=[A]
              cur.execute('select * from passenger_details where cid=%s',l)
              data=cur.fetchall()
              if len(data)!=0:
                  cur.execute('update passenger_details set status="Deactivated" where cid=%s',l)
                  cnx.commit()
                  print('User deactivated with CId ',A)
              else:
                  print('NO SUCH DATA FOUND!')
      elif ch2=='5':
        break

  elif ch1=='4':
      while True:
          print(menu5)
          ch2=input('Enter your choice: ')
          if ch2=='1':
            l=ADD_BOOKING.add_booking_details()
            cur.execute('insert into booking_details values(%s,%s,%s,%s,%s)',l)
            cnx.commit()
          elif ch2=='2':
              s=input('Press "1" for all data and "2" for specific data search with Flight_code and CId: ')
              if s=='2':
                l=CHECK_BOOKING_DETAILS.checkBD()
                cur.execute('select * from booking_details where Flight_code=%s and cid=%s',l)
                data=cur.fetchall()
                if len(data)!=0:
                    cur.execute('select * from booking_details where Flight_code=%s and cid=%s',l)
                    mytable = from_db_cursor(cur)
                    print(mytable)
                else:
                  print('NO SUCH DATA FOUND!')
              elif s=='1':
                cur.execute('select * from booking_details')
                mytable = from_db_cursor(cur)
                print(mytable)
              else:
                print('INVALID CHOICE')
          elif ch2=='3':
              l=[]
              
              while True :
                  print("1. Flight code ")
                  print("2. Fare")
                  print("3. Exit")
                  ch=input("Enter your choice : ")
                  
                  if ch=='1':
                      while True:
                          try:
                            A=int(input("Enter customer id : "))
                            A=A
                            cur.execute('select * from passenger_details where cid=%s',[A])
                            check=cur.fetchall()
                            if len(check)==0:
                              print("CId DOESN'T EXIST!\n")
                              break
                          except :
                            print("Customer id should be numeric")
                            break
                          B=input("Enter new flight code : ")
                          if len(B)<=30:
                            B=B
                          else:
                            print("Length of flight code should not be greater than 30")
                            break
                          l=[B,A]
                          cur.execute('update booking_details set flight_code=%s where cid=%s',l)
                          cnx.commit()
                          print('DONE')
                          break
                    
                  elif ch=='2':
                      while True:
                          try:
                            A=int(input("Enter customer id : "))
                            A=A
                            cur.execute('select * from passenger_details where cid=%s',[A])
                            check=cur.fetchall()
                            if len(check)==0:
                              print("CId DOESN'T EXIST!\n")
                              break
                          except :
                              print("Customer id should be numeric")
                              break
                          try:
                            D=int(input("Enter new fare : "))
                            D=D
                          except:
                            print("Price  of efare should numeric")
                            break
                          l=[D,A]
                          cur.execute('update booking_details set fare=%s where cid=%s',l)
                          cnx.commit()
                          print('DONE')
                          break
                  elif ch=='3':
                     break
          elif ch2=='4':
                  cur.execute('select * from booking_details')
                  mytable = from_db_cursor(cur)
                  print(mytable)
                  print()
                  A=input('Enter CId of the customer u want to deactivate: ')
                  B=input('Enter Flight_code of the customer u want to deactivate: ')
                  l=[B,A]
                  cur.execute('select * from booking_details where flight_code=%s and cid=%s',l)
                  data=cur.fetchall()
                  if len(data)!=0:
                      cur.execute('update booking_details set status="Cancelled" where flight_code=%s and cid=%s',l)
                      cnx.commit()
                      print('BOOKING CANCELLED')
                  else:
                      print('NO SUCH DATA FOUND!')
          elif ch2=='5':
            break
  if ch1=='5':
    print('\n*****THANKS FOR VISITING!!*****\n')
    print(creaters)
    break
      
 
        
