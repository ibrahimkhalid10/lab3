
check=0
dict= {}
while check != "no":
    inputN = input("enter the name of the employee:")
    inputS = int(input("enter the salary of the employee:"))
    dict[inputN]=inputS
    check=input("do you want to continue?")
print(dict)