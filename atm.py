import sys
import random
class Team:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first+'.'+last+'@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp1=Team('tina', 'hope', 5000)
emp2=Team('benjamin','tulienge',8000)
print(emp1.fullname())
print(emp2.fullname())
print(emp1.email)
        
class Atm:
    def __init__(self,name,password,account_number,balance=0):
        self.password=password
        self.balance=balance
        self.name=name
        self.account_number=account_number
    
    
    def withdrawal(self,amount,password):
        self.amount=self.amount
        self.password=self.password
        if self.password==self.password:
            if self.amount>self.balance:
              print("Insufficient funds")
            else:
              self.balance=self.balance- self.amount
              print(f"withrawal of {amount} succesful")
              print("Current Balance",self.balance)
                
        else:
            print("Invalid Password try again")
    def account_info(self):
        print('\n----ACCOUNT DETAILS----')
        print()
        print(f"Account Number:{self.account_number}")
        print(f"Available Balance:{self.balance}")
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Current Balance:",self.balance)
    def check_balance(self):
        print("Balance:",self.balance)
    def transaction(self):
        print("""
              TRANSACTION
              **************
              Menu:
              1.Account Detail
              2.Check Balance
              3.Deposit
              4.Withdraw
              5.Exit
              ******************
              """)
        while True:
                  try:
                      option=int(input("Select option:"))
                  except:
                      print('Error: Enter 1,2,3,4 or 5 only!\n')
                  else:
                      if option ==1:
                          atm.account_info()
                      elif option==2:
                          atm.check_balance()
                      elif option==3:
                          amount=int(input("How much you want to deposit:"))
                          atm.deposit(amount)
                      elif option==4:
                          amount=int(input('How much you want to Withdraw:'))
                          password=int(input('Enter your Password:'))
                          if password<5:
                              print('password too short')
                              
                          atm.withdrawal(amount, password)
                      elif option==5:
                          sys.exit()
print("***WELCOME TO BANK OF MAMBO IMECHMKA")
print("_________________________________")
print("---ACCOUNT CREATION----")
name=input('Enter your name:')
account_number=int(input('Enter your Account Number:'))
password=int(input('Enter Password'))
print('Congratulations Account Created Sucessfully')
atm=Atm(name, password, account_number)
while True:
    trans=input('Do you want to transact:')
    if trans=='y' or 'Y':
        atm.transaction()
    elif trans=='n' or 'N':
        print("THANKS FOR CHOOSING US")
        break
    else:
        print('Wrong command')
        
                          
                             
    
            
       
        