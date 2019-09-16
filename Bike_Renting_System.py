# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:30:35 2019

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:36:45 2019

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:20:59 2019

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:04:14 2019

@author: admin
"""

class User():
    def enter(self):
        self.name=str(input("Enter your name"))
        self.Email_Id=str(input("Enter your Email ID"))
        self.contact=int(input("Enter your Phone number"))
        
    def printU(self):
        print("Name:"+self.name)
        print("EmailId:"+self.Email_Id)
        print("Contact:"+str(self.contact))
        
        
        
class Shop():
    def __init__(self,available=25):  #assuming initial stock to be 25 incase no number is provided!
        self.available=available 
       
    def bike(self):
        bikeList=open('bikelist.txt','r').read()
        print(bikeList)
        
    def order(self,opt,no_bike,date,time):
    
        if no_bike > self.available :
            print('Sorry these many bikes are not available right now')
        else:
            self.available-=no_bike
            print('We hope you have a safe ride')
            
            
    def Return(self,no_bike):
        
        self.available+=no_bike
        
    def DTcalc(self,date,time,Rdate,Rtime):
        self.days=Rdate-date
        self.timet=Rtime-time
        
    def bill(self,opt,no_bike):
        if opt==1:
            amount=(self.timet)*5*no_bike
        elif opt==2:
            amount=(self.days)*20*no_bike
        else:
            amount=(self.days)/7*60*no_bike
         
        if 3<=no_bike<=5:             #family discount
            amount=0.70*amount
            
        return amount

       
u1=User()
u1.enter()

#Menu - Driven Program
def menu():
    print('WELCOME\n BIKE RENTAL SYSTEM')
    
    s1=Shop()
    print('     1.SEE THE BIKES AVAILABLE ON RENT')
    print('     2.RENT BIKE(S)')
    
    choice=int(input("what do you want to do?"))
    
    if choice<0:
        print('The choice cannot be negative')
    elif choice==1:
        s1.bike()
        print("type menu() for running menu again")
                
    elif choice==2:
        opt=int(input("On which basis do you want to rent a bike on?\n 1.Hourly ($5 per hour) \n 2.Daily($20 per day) \n 3. On weekly basis ($60 per week)"))
        no_bike=int(input("Enter no. of bikes uwant ot rent \n If you rent more than 3 and less than 5 bikes you can avail Family discount of 30% on total bill"))
        date=int(input("Enter date of bike issue"))
        time=int(input("Enter time of bike issue(in hours)"))
        s1.order(opt,no_bike,date,time)
        Rdate=int(input("Enter date of bike return"))
        Rtime=int(input("Enter time of bike return(in hours)"))
        s1.Return(no_bike)
        s1.DTcalc(date,time,Rdate,Rtime)
        u1.printU()
        print("Your total bill is of"+str(s1.bill(opt,no_bike))+"rupees")
        print("Kindly visit again thankyou(Type menu() for menu list)")
    else:
        print("Invalid choice")
        
menu()

