
un = input("please type your username")
pw = input("please type your password")
if len(pw) <8 :
    print("your password needs to be longer")

print("#"*20)

print("Your username is" , un.lower(),"#") 
print("#","Your password is" ,pw.capitalize(),"#")
length = len(pw)
print ("#","your password is",length,"characters long","#")

print("#"*20)

print(un.__contains__("oh no"))