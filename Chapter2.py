## Chap2.2.1 ##

print ('I\'m')
print ("\"learning\"")
print ("\"\"Python\"\"")

## Chap 2.4 ##

john = 3
mary = 5
adam = 6
print (john, mary, adam, sep=",")
total_apples = john + mary + adam
print (total_apples)
print ("Total number of apples:", total_apples)

## 2.4.1.9 ##

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

## 2.4.1.10 ##

x =  0
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("y =", y)

x =  1
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("y =", y)

x =  -1
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("y =", y)

## 2.5.1.2 ##

#this program computes the number of seconds in a given number of hours
#this program was written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

print("Goodbye.")
#this is the end of the program that computes the number of seconds in 3 hour

## 2.6.1 ## 

# Testing TypeError message.

anything = float (input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

## 2.6.1.9 ##

var_a = float(input("Input first number: "))
var_b = float(input("Input second number: "))


print("These numbers added together are " + str(var_a + var_b)
print("These numbers subtracted are " + str(var_a + var_b)
print("These numbers multiplied are " + str(var_a + var_b)
print("These numbers divided are " + str(var_a + var_b)


print("\nThat's all, folks!")
