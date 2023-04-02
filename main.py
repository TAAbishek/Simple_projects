#login system
def isValidUsername(user_name):
    with open('account/ac.txt','r') as f:
        text=f.read()
        tar="username:"+user_name
        if tar in text:
            return False
        else:
            return True
#print(isValidUsername('arun'))
def login():
    option=input("  sign/login up (1/2) ")
    if option=='1':
        while(True):
            user_name=input('enter user-name  ')
            if isValidUsername(user_name):
                break
            else:
                print('username already exists')
        while(True):
            password=input("enter password  ")
            password1=input("renter password  ")
            if password1==password:
                print('account succesfully created')
                with open('account/ac.txt','a') as f:
                    f.write(f"username:{user_name} \n")
                    f.write(f"password :{password} \n")
                break
            else:
                print("passwords not matching")
        
    elif option=='2':
        while(True):
            user_name=input('enter user-name  ')
            if isValidUsername(user_name):
                print('username does not exist')
            else:
                break
        while(True):
            password=input("enter password  ")
            with open('account/ac.txt','r') as f:
                text=f.read()
                ind=text.find(user_name)
                ind1=text.find('password',ind)
                password1=''
                for i in range(ind1+10,99999):
                    if text[i] !=' ':
                        password1+=text[i]
                    else:
                        break
            print(password1,password)
            if password1==password:
                print('login successfull')
                break
            else:
                print("password not matching")
                          
login()