n = int(input())
def fizz_buzz(n):
    for n in range(1, n+1):
        if (n % 3 == 0) and (n % 5 == 0):
            print("fizzbuzz")
        elif n % 5 == 0:
            print("buzz")
        elif n % 3 == 0:
            print ("fizz")
        else:
            print(n)
fizz_buzz(n) 
