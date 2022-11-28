"""a="python" #printing in order
n=len(a)
for i in range(n):
    print(i,'=',a[i])

n=int(input("Enter a number:")) #loop for multiple
for i in range(1,11):
    print(f"{n}X{i}={n*i}")

n=int(input("Enter a number:")) #loop for opposite multiple
for i in range (10,0,-1):
    print(f"{n}X{i}={n*i}")

for i in range (1,50):
    print(i,'---',50-i)

num=int(input("Enter a number:"))
sum=0
out=str(num)[0]
for n in str(num):
    sum+=int(n)
    out+=f" + {n}"
print (f"{out[3:]} = {sum}")

num=int(input("Enter a number:"))
b=False
for a in range(2,num):
    if num%a==0:
        b=True
if num==1:
    print("Neither prime nor composite")
elif b:
    print("Not prime")
else:
    print("Prime") 
 
name=input("Enter a string:")
rev=''
for n in range(len(name)-1,-1,-1):
    rev+=name[n]
print(rev)

num = int(input("Enter a number:"))
mul=1
for n in range(1,num+1):
    mul*=n
print(mul)

value=input ("Enter:")
i=s=0
for v in value:
    if v.isdigit():
        i+=1
    else:
        s+=1
print(f"Integer = {i}\nString ={s}")

name=input("Enter a string:")
rev=''
for n in range(len(name)-1,-1,-1):
    rev+=name[n]
if rev==name:
    print("Palindromic")
else:
    print("Not palindromic")

uname,paswrd='admin','dadmin'
for a in range(3):
    name,pwd=input("Enter username and password:").split(' ')
    if uname == name and paswrd == pwd:
        print("Logged in")
        break
    else:
        tries+=1
        if tries==3
        print("You have been blocked)
     print("Wrong credentials")"""


for i in range(1,10):
    if i==5:
        continue
    print(i)