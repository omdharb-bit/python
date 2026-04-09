# wap which will take radius of a circle as input and print and circumference of a circle

# radius=float(input("Enter the radius of a circle: "))
# circumference= 2*3.14*radius
# print("Circumference of a circle is: ",circumference)

# wap to determine grades based on marks
# marks=int(input("Enter the marks: "))
# if marks>=90:
#   print("Grade A")
# elif marks >=80:
#     print("Grade B")
# elif marks>=70:
#       print("Grade C")
# else :
#         print("Fail")

# wap to find no is divisible ny noth 3 and 5

# n=int(input("Enter the no. : "))
# if n%3==0 & n%5==0:
#   print("no. is divisible by 3 and 5")
# else:
#   print("No. is not divisible ny 3 and 5")

# wap to find largest of three numbers
# a=int(input("Enter the first no. : "))
# b=int(input("Enter the second no. : "))
# c=int(input("Enter the third no. : "))
# if a>b and a>c:
#     print("Largest no. is: ",a)
# elif b>a and b>c:
#     print("Largest no. is: ",b)
# else:
#     print("Largest no. is: ",c)


# n=int(input("Enter the units. : "))

# if n<=50:
#     n= n*0.50
#     print("Your electricity bill: ",n)
# elif n<=150:
#     n=n*0.75
#     print("Your electricity bill: ",n)
# elif n<=250:
#     n = n * 1.20
#     print("Your electricity bill: ", n)


# for i  in range(1,100):
#   if i%3 ==0:
#     print("Fizz")
#   elif i %5==0:
#     print("Buzz")
#   elif i% 3==0 & i%5==0:
#     print("Fizz buzz")
#   else:
#      print(i)


# Prime or not using while loop
# n=int(input("Enter the no. : "))
# i=2
# while i<n:
#     if n%i==0:
#         print("No. is not prime")
#         break
#     i+=1
# else:
#     print("No. is prime")


# def factors(n):
#    for i  in range(1,n+1):
#      if n%i==0:
#        print(i,end=" ")
#      return(10)

# x=factors(12)
# print(x)

# Wap a program factorial is even or odd using function.by taking user input

# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# def check_even_odd(num):
#     fact = factorial(num)
#     print("Factorial of", num, "is:", fact)

#     if fact % 2 == 0:
#         print("Factorial is Even")
#     else:
#         print("Factorial is Odd")

# number = int(input("Enter a number: "))
# check_even_odd(number)


# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact


# # ncr program using function

# def nCr(n, r):
#     return factorial(n) // (factorial(r) * factorial(n - r))

#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact


# def nCr(n, r):
#     return factorial(n) // (factorial(r) * factorial(n - r))


# n = int(input("Enter n: "))
# r = int(input("Enter r: "))

# result = nCr(n, r)
# print("nCr =", result)
# n = int(input("Enter n: "))
# r = int(input("Enter r: "))

# result = nCr(n, r)
# print("nCr =", result)


# wap which take integer as a input , increase even no. by 5 and subtract odd by 5

# lst=eval(input("Enter list element: "))
# for i in range(len(lst)):
#  if lst[i]%2==0:
#   lst[i]+=5
#  else:
#   lst[i]-=5
#   print(lst)


 
