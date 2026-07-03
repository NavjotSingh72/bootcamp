n=int(input("Enter Your Number"))

freq=0
for i in range(1,n):
    if n==0:
        print("Zero is not prime nor composite")
    elif n%i!=0:
        freq+=1
    else:
        pass
    
if freq>1:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")