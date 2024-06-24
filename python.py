def prime(a):
    for i in range(2,a):
        if a%i==0:
            print(a,"Not a Prime number")
            break
    else:
        print(a,"Is a prime number")

prime(int(input("Enter the number : ")))
