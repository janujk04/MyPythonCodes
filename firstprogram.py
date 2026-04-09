a= int(input("enter the value of a= ")) 
b= int(input("enter the value of b= "))
sum = int(a) + int(b)

print("the value of a",a)

#The below line will print sum of two numbers
print("the sum is ",sum)

#The below line is for difference
difference = int(a) - int(b)

print("the difference is ",difference)
multiply = int(a) * int(b)
print(" the product is ", multiply)
if b % 2 == 0:
    print(b, "is even number")
else:
    print(b, "it is odd number")
if a > b:
    largest = a
else:
    largest = b
print("the largest number is", largest)
