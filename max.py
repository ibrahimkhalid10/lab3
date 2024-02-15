list=[]
big=0
count=0
while count != 10:
    num=int(input('enter the number'))
    list.append(num)
    count=count+1

for num in list:
    if num > big:
        big=num
print('the biggest number is:',big)