print("\n\nWELCOME TO THE PHONE CUSTOMER SERVICE")
name=input("\n\nWhat your name:")
print("\nHello", name,",Welcome again to the Phone Customer Service")
def newuser():
    name=input("SURNAME:")
    new_username=input("\n\nUSERNAME:")
    new_password=input("\n\nPASSWORD:")
    f=open("secured.txt","a+")
    f.write("\n")
    f.write(new_username)
    f.write(":")
    f.write(new_password)
    f.close()
    print("\nWELCOME",new_username)
    print("\n\nPLEASE PICK FROM OUR SERVICES BELOW")
def olduser():
        username=input("\n\nUSERNAME:")
        password=input("\n\nPASSWORD:")
        f=open("secured.txt","r")
        if f.mode=='r':
            f1 =[x.split(':') for x in f.readlines()]
            if [username,password] in f1:
                print("\nWELCOME BACK",username)
                print("\n\nPLEASE PICK FROM OUR SERVICES BELOW")
            else:
                print("\nSorry but your details can not be found\n")
                login()
        f.close()
def login():
    option = None
    print("""\n\n
              Select an option below
              1) OLD MEMBER
              2) NEW MEMBER
          \n""")
    option=int(input("\nOPTION:"))
    print()
    if option == 1:
        olduser()
    elif option == 2:
        newuser()
login()
def airtime():
    print("\n\nYOU HAVE SUCCESSFULLY LOADED",credit,"POUNDS AIRTIME")
def databundle():
    x=()
    print("""\n\n
              1.DAILY
              2.WEEKLY
              3.MONTHLY
          \n""")
    x=int(input(">"))
    print()
    global credit
    global data
    if x==1:
        print("""\n\n
                1. 2 Pound for 25MB\n
                2. 3 Pounds for 75MB\n
                3. 5 Pounds for 200MB(2-DAY PLAN)\n
                4. 7 Pounds for 1GB\n
                5. 8 Pounds for 2GB(2-DAY PLAN)\n
               \n""")
        f=()
        f=int(input(">"))
        print()
        
        if f==1:
           
            credit-=2
            
            data+=25
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==2:
            
            credit-=3
            
            data+=75
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==3:
            
            credit-=5
            
            data+=200
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==4:
           
            credit-=7
            
            data+=1000
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==5:
            
            credit-=8
            
            data+=2000
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
    if x==2:
        print("""\n\n
                1. 5 Pounds for 350MB\n
                2. 8 Pounds for 750MB(2-WEEK PLAN)\n
                3. 8 Pounds for 500MB\n
                4. 5 Pounds for Whatsapp Only\n
                5. 11 Pounds for 6GB\n
               \n""")
        f=()
        f=int(input(">"))
        print()
       
        if f==1:
            
            credit-=5
            
            data+=350
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==2:
            
            credit-=8
            
            data+=750
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==3:
           
            credit-=8
           
            data+=500
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==4:
          
            credit-=5
            
            data+=100
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==5:
            
            credit-=11
            
            data+=6000
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
    if x==3:
        print("""\n\n
                1. 12 Pounds for 1.5GB\n
                2. 15 Pounds for 3GB\n
                3. 18 Pounds for 6GB\n
                4. 20 Pounds for 10GB\n
                5. 25 Pounds for 15GB\n
               \n""")
        f=()
        f=int(input(">"))
        print()
       
        if f==1:
            
            credit-=12
           
            data+=1500
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==2:
            
            credit-=15
            
            data+=3000
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==3:
            
            credit-=18
            
            data+=6000
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==4:
           
            credit-=20
            
            data+=10000
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
        elif f==5:
            
            credit-=25
            
            data+=15000
            print("\n\nYOUR DATA BUNDLE OF ",data,"MB HAS BEEN SUCCESSFUL")
            print("\n\nYOU HAVE A TOTAL OF",credit,"POUNDS AIRTIME LEFT")
choice=None
again=()
data=0
credit=0
while again !="Y":
    print("""\n\n
             1.BUY AIRTIME
             2.BUY DATA BUNDLE
             3.CHECK BALANCE
             4.ACTIVATION/DEACTIVATION
             5.CUSTOMER CARE
             6.EXIT
          \n""")
    choice=int(input("\nCHOICE:"))
    print()
    if choice==1:
        credit=int(input("\nHow much airtime would you like to buy:"))
        airtime()
    if choice==2:
        databundle()
    if choice==3:
        print("\n\nYOU HAVE A BALANCE OF",credit,"POUNDS AIRTIME AND",data,"MB OF MOBILE DATA")
    if choice==4:
        print("""\n\n
                1.ACTIVATE SIM\n
                2.DEACTIVATE SIM\n
               \n""")
        y=()
        y=int(input(">"))
        print()
        if y==1:
            SIM=input("\nWHICH SIM DO YOU USE:")
            number=int(input("\n\nPLEASE INPUT YOUR PHONE NUMBER:"))
            print("\n\nYOUR",SIM,"SIM WILL BE ACTIVATED IN A SHORT WHILE")
        elif y==2:
            SIM=input("\nWHICH SIM DO YOU USE:")
            number=int(input("\n\nPLEASE INPUT THE PHONE NUMBER:"))
            print("\n\nYOUR",SIM,"SIM WILL BE DEACTIVATED IN A SHORT WHILE")
    if choice==5:
        print("\nPLEASE CALL 09074933837\n")
    if choice==6:
        again=input("\n\nARE YOU SURE YOU WANT TO EXIT(Y/N):\n")
        if again=="N":
            print()
