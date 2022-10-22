i=int(input("ENTER THE LIMIT :-"))
x=0
y=1
z=1
print("Fibonacci Series\n")
print(x,y,end="")
while(z<=i):
    print(z, end=' ')
    x=y
    y=z
    z=x+y
