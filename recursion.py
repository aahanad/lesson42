#n=input("What number?")
#def sum(n):
#    if n==1:
#        return n
#    else:
#        return sum(n-1)+n
#print(sum(4))
#sum(4)

#factorials
#n=input("what number")
#def sum(n):
#    if n==1:
#        return n
#    else:
#        return n* sum (n-1)
#print (sum(3))
#sum(3)

#exponents
n=int(input("what number?"))
e=int(input("what exponent?"))
def sum(n,e):
    if e==1:
        return n
    elif e==0:
        return 1 
    else:
        return n* sum (n,e-1)
print (sum(n,e))
sum(n,e)
#ice cream tub
def empty_scoops(n):
    if n == 0:
        print("All scoops are gone. The tub is empty!")
        return
    else:
        print(f"Scoop number {n} removed...")
        empty_scoops(n - 1)
n=int(input("How many scoops do you want? "))
empty_scoops(n)

