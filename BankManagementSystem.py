import mysql.connector as dbc
import time
banksys = dbc.connect(
    host = "localhost",
    user = "root",
    passwd = "@gaurav123",
    database = "BankOfGaurav"
                      )
if banksys.is_connected():
    print("Server is Online !!!")
else:
    print("Oops ! Error ...")

cur = banksys.cursor() # cur = 'cursor object', banksys = 'connector object'

# ----------------------------All Class Section--------------------------------------------------------------------------------------------------------------
class CreateAccountSection:
    def __init__(self,FullName,AdharNumber,PANnumber,ClientAddress,ClientPasskey,UserName,DepositedMoney,WithdrawlMoney,TransferMoney,Balance):
        self.ufname = FullName
        self.uadharNum = AdharNumber
        self.upan = PANnumber
        self.uaddress = ClientAddress
        self.upass = ClientPasskey
        self.uname = UserName
        self.deposite = DepositedMoney
        self.withdrawal = WithdrawlMoney
        self.transfer = TransferMoney
        self.balance = Balance
        print("you are in constructor")
        
        query = f'''CREATE TABLE IF NOT EXISTS `{self.uname}` (
                DepositedMoney INT DEFAULT 0,
                WithdrawalMoney INT DEFAULT 0,
                TransferMoney INT DEFAULT 0,
                Received INT DEFAULT 0,
                Balance INT NOT NULL
            );'''

        cur.execute(query)
        banksys.commit()  
        query = f"insert into `{self.uname}` values (0,0,0,0,0)"
        cur.execute(query)
        banksys.commit()
        time.sleep(0.5)  
        print(f"Your account created with username : {self.uname}")
    def CollectingInfoInSQL(self):
        
        # Assuming AccountInfo, LoginInfo, and BankMoney tables exist
        query = f"INSERT INTO AccountInfo VALUES('{self.ufname}', {self.uadharNum}, '{self.upan}', '{self.uaddress}', '{self.upass}', '{self.uname}')"
        cur.execute(query)
        banksys.commit()

        query = f"INSERT INTO LoginInfo VALUES('{self.uname}', '{self.upass}')"
        cur.execute(query)
        banksys.commit()
        time.sleep(0.4)
        print("your info has been stored !")
        time.sleep(0.5)
        print("redirecting to login page...")
        time.sleep(0.5)
        # query = f"INSERT INTO  VALUES({self.deposite}, {self.withdrawal}, {self.transfer}, {self.balance}, '{self.uname}')"
        # cur.execute(query)
        # banksys.commit()
        print("------welcome to Login page hope you have username or passkey--------")
        time.sleep(0.3)
        introSection()
    # def showInfoOfClient(self):
        
        # cur.execute(f"select `{self.uname}` from AccountInfo where UID_Number={self.uadharNum}")
        # Clientdata = cur.fetchall()
        # print("your user name :",Clientdata)
        


class ClientLoginSection:                                    # 4th step  login class section 
    def __init__(self,UserName,ClientPasskey):
        self.uname = UserName
        self.upass = ClientPasskey
    def MatchingLogInInfoFromSQL(self):                   # 5th step  matching login info in method
        global LogInData
        time.sleep(0.4)
        print("Checking Username and Passkey...")
        cur.execute("select * from LoginInfo")
        LogInData = cur.fetchall()
        # for i in range(0,len(LogInData)):                      # 6th step  matching syntax
        #     for j in range(1):
        #         if self.uname == LogInData[i][j]:
        #             print("user allowed")
        # else:
        #     for i in range(0,len(LogInData)):
        #         for j in range(2):
        #             if self.upass == LogInData[i][j]:
        #                 pass
        #--------------------------------------------------------
        for i in range(0,len(LogInData)):
            if self.uname == LogInData[i][0]:
                if self.upass == LogInData[i][1]:
                    time.sleep(0.4)
                    print("User Allowed !")
                    break
        else:
            print("your username or passskey is wrong !!!")
            time.sleep(0.5)
            print("redirecting to login page...")
            time.sleep(0.4)
            introSection()
        #---------------------------------------------------------               
        MakeChoiceInBankAccount()           
                            
class BankManagementSystem(CreateAccountSection):
    def __init__(self,UserName,DepositedMoney,WithdrawlMoney,TransferMoney,Balance,bal_trans,user_trans,data):
        self.uname = UserName
        self.deposite = DepositedMoney
        self.withdrawal = WithdrawlMoney
        self.transfer = TransferMoney
        self.balance = Balance
        self.baltrans = bal_trans
        self.usertrans = user_trans
        self.data = data
        query = f"select * from `{self.uname}`"
        cur.execute(query)
        self.data = cur.fetchall()
        
    def checkStatusOfAccount(self):
        
        print("|-----x------x-------x--------x---------x--------x------|")
        print("|-----------|     Your Bank Account Info    |-----------|")
        print("|-----x------x-------x--------x---------x--------x------|")  
        cur.execute(f"select * from AccountInfo where UserName = '{self.uname}'")
        Clientdata = cur.fetchall()
        print(Clientdata)

        # print(Clientdata[1])
        print(f"Full Name : {Clientdata[0][0]}\nAdhar Number : {Clientdata[0][1]}\nPAN Number : {Clientdata[0][2]}\nAddress : {Clientdata[0][3]}\nPassword : {Clientdata[0][4]}\nUserName : {Clientdata[0][5]}")
        print("Current Balance : ",self.data[-1][-1],"$")

      
        MakeChoiceInBankAccount()
    def ToDepositeMoney(self):
        print("---- Deposit Money Section  ----")
        try:
            self.deposite = int(input("Enter Money Amount ($) : "))
        except ValueError:
            print("Deposite amount will be in numbers !")
            b.ToDepositeMoney()
        print(f"Your {self.deposite}$ Have been Depositted !")
        self.balance += self.deposite
        query = f"select * from `{self.uname}`"
        cur.execute(query)
        self.data = cur.fetchall()
        self.balance += (self.data[-1][-1])
        
        # self.update_balance()
        query = f"INSERT INTO `{self.uname}` (DepositedMoney, Balance) VALUES ({self.deposite}, {self.balance});"
        cur.execute(query)
        banksys.commit()
        print("-------Bank Balance---------")
        query = f"select * from `{self.uname}`"
        cur.execute(query)
        self.data = cur.fetchall()
        print("Current Balance : ",self.data[-1][-1],"$")
        MakeChoiceInBankAccount()
    def ToWithdrwalMoney(self):
        query = f"select * from `{self.uname}`"
        cur.execute(query)
        self.data = cur.fetchall()
        print("--------Money Withdrawl Section ---------------------------------")
        try:
            self.withdrawal = int(input("Enter Withdrawal Money Amount ($) : "))
        except ValueError:
            print("Withdrawal amount will be in numbers !")
            b.ToWithdrwalMoney()
        
        if self.withdrawal > (self.data[-1][-1]):
            print("Dont have enough Balance in your bank !")
            b.ToWithdrwalMoney()
            print("re-enter your amount")
            
        else:
            print(f"Your {self.withdrawal}$ Have been Withdrawl !")
            self.data = int(self.data[-1][-1])
            self.data-= self.withdrawal
            # self.update_balance()
            query = f'''INSERT INTO `{self.uname}` (WithdrawalMoney,Balance)VALUES ({self.withdrawal},{self.data});'''
        cur.execute(query)
        banksys.commit()
        query = f"select * from `{self.uname}`"
        cur.execute(query)
        self.data = cur.fetchall()
        print("Current Balance : ",self.data[-1][-1],"$")
        MakeChoiceInBankAccount()
    def ToTransferMoney(self):
        query = f"select * from `{self.uname}`"
        cur.execute(query)
        self.data = cur.fetchall()
        print("--------Money TRANSFER Section ---------------------------------")
        
        try:
            self.transfer = int(input("Enter Transfer Money Amount ($) : "))
        except ValueError:
            print("Transfer amount will be in numbers !")
            b.ToTransferMoney()
            
        query = f"select * from `{self.uname}`"
        cur.execute(query)
        self.data = cur.fetchall()
        
        if self.transfer > (self.data[-1][-1]):
            print("Dont have enough Balance in your bank !")
            b.ToTransferMoney()
            print("re-enter a valid your amount !")
            
        
        print("-------Here you type username that you want to send money----------")
        self.usertrans =  input("enter username :  ")
        for i in range(0,len(LogInData)):
            if self.usertrans == LogInData[i][0]:
                break
        else:
            print("Plz Enter a valid username  !!!")
            print("redirecting to login page...")
            b.ToTransferMoney()
        print(f"Your {self.transfer}$ Have been Transfer to '{self.usertrans}'\'s Account !")
        self.data = int(self.data[-1][-1])
        self.data -= self.transfer
        
        query = f'''INSERT INTO `{self.uname}` (TransferMoney,Balance)
                    VALUES ({self.transfer},{self.data});'''
        cur.execute(query)
        banksys.commit()
        # data of username given in transaction----->
        query = f"select * from `{self.usertrans}`"
        cur.execute(query)
        self.data = cur.fetchall()
        
        self.data = int(self.data[-1][-1])
        self.data += self.transfer
        
        query = f'''INSERT INTO `{self.usertrans}` (Received,Balance)
                    VALUES ({self.transfer},{self.data});'''
        cur.execute(query)
        banksys.commit()
        
        query = f"select * from `{self.uname}`"
        cur.execute(query)
        self.data = cur.fetchall()
        print("Current Balance : ",self.data[-1][-1],"$")
        MakeChoiceInBankAccount()
    def AboutMe(self):
        print("--------------------------------------")
        print('''|Purpose:
Develop a robust Bank Management System in Python\n integrated with MySQL, streamlining financial\n operations for efficient customer service.|''')
        print("|-------------------------------------|")
        print('''|Technologies Used:
Built with Python for backend functionality and\n MySQL database for secure and organized data\n storage.|''')
        print("|-------------------------------------|")
        print('''|Key Features:
User-friendly interface, account management, \ntransaction tracking, and real-time balance\n updates ensure a seamless banking experience.|''')
        print("|-------------------------------------|")
        print('''|Project Scope:
Empowering banks with a comprehensive solution for\n customer management, transaction processing, and\n data integrity in a secure environment.|''')
        print("|-------------------------------------|")
        print("--------------------------------------")

#---------------------------All Methods (Function)---------------------------------------------------------------------------------------------
    
def introSection():                                            # 2nd step choice b/w login / create account
    global x
    print("-----|-1-|->LogIn...\n-----|-2-|->create account... ")
    x = int(input("enter your choice-->"))
    ExecutionOfChoice(x)
def ExecutionOfChoice(x):  
    global Balance
    global WithdrawlMoney
    global TransferMoney
    global DepositedMoney
    Balance = 0
    DepositedMoney = 0
    WithdrawlMoney = 0
    TransferMoney = 0                                                 #  3rd step applying choices 1 and 2
    if x==1:
        global UserName
        UserName = input("enter username : ")
        ClientPasskey = input("enter userpass : ")
        logged = ClientLoginSection(UserName,ClientPasskey) # class object
        logged.MatchingLogInInfoFromSQL() # calling class method
    elif x==2:

 #      Full Name ------->
        time.sleep(0.4)  # import time
        FullName = input("enter your name --> ")
        #adhar number ------>
        while True:
            AdharNumber = int(input("enter Aadhar Number --> "))
            if len(str(AdharNumber)) == 12:
                AdharNumber = int(AdharNumber)
                break
            else:
                print("valid adhar number should contain 12 numbers !")
        while True:
            PANnumber = input("enter your PAN number --> ")
            if len(PANnumber) == 10:
                break
            else:
                print("Enter a valid PAN number !")
        ClientAddress = input("enter your address --> ")
        ClientPasskey = input("set your Password --> ")
        UserName =f"{FullName}{len(PANnumber)+len(ClientAddress)}@banksys"
        ClientAccInfo = CreateAccountSection(FullName,AdharNumber,PANnumber,ClientAddress,ClientPasskey,UserName,DepositedMoney,WithdrawlMoney,TransferMoney,Balance)
        # class methods
        ClientAccInfo.CollectingInfoInSQL()
        # ClientAccInfo.showInfoOfClient()
    else:
        print("---+---enter valid operation !!!")
        introSection()
        
def MakeChoiceInBankAccount():                             # 8th step    input for bank sys features 
    print("X--------------------------------X")
    print("|--|Check Status   -> 1  |-------|")
    print("X--------------------------------X")
    print("|--|Dposite Money  -> 2  |-------|")
    print("X--------------------------------X")
    print("|--|Withdrawl Money-> 3  |-------|")
    print("X--------------------------------X")
    print("|--|Money Transfer -> 4  |-------|")
    print("X--------------------------------X")
    print("|--|Others         -> 5  |-------|")
    print("X--------------------------------X")
    print("|--|Log Out        -> 6  |-------|")
    y = int(input("Enter your choice----> "))
    ExecutionOfChoiceInAcc(y)
def ExecutionOfChoiceInAcc(y):
    global b                                                           #9th step  executing  choice in bank sys features 
    global bal_trans
    global user_trans
    data = []
    bal_trans = None
    user_trans = None
    b = BankManagementSystem(UserName,DepositedMoney,WithdrawlMoney,TransferMoney,Balance,bal_trans,user_trans,data)
    if y == 1:
        b.checkStatusOfAccount()
    elif y == 2:
        b.ToDepositeMoney()
    elif y == 3:
        b.ToWithdrwalMoney()
    elif y == 4:
        b.ToTransferMoney()
    elif y == 5:
        b.AboutMe()
    elif y == 6:
        introSection()
    else:
        print("Enter valid a Option of the following !")
        MakeChoiceInBankAccount()
        
        
        
        
        
    
        
#----------------------------CallBack Functions_----------------------------------------------------------------------------------------        

    # Main function to start the program
def main():
    introSection()
    

if __name__ =="__main__":
    main()
    

                        #7th step     make choice in bank ssytem features

        
        
    
    
    

