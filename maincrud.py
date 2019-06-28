from insert import inserData;


print("1.insert")
print("2.View")

print("Enter your choices")
choices = int(input())
if(choices == 1):
    print("Enter the fullname",end="")
    fullname = input()
    print(end ="")
    print("Enter the email",end="")
    email = input()
    isInsert = inserData(fullname,email)
    if(isInsert == "true"):
        print("Recod inserted succesfully")
    else:
        print("oops..! Recor not inserted")