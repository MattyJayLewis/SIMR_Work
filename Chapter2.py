## Matthew Lewis, Chapter 2, 20/092021 ##

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
a = 3 # number of hours
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


print("These numbers added together are " + str(var_a + var_b))
print("These numbers subtracted are " + str(var_a - var_b))
print("These numbers multiplied are " + str(var_a * var_b))
print("These numbers divided are " + str(var_a / var_b))
print("\nThat's all, folks!")

## 2.6.1.10 ##

x = float(input("Enter value for x: "))

y = float(1 / ((x + 1 / (x + 1 /(x + 1 / x)))))

print("y =", y)
      
## 2.6.1.11 ##
      
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
## time_hour variable created to work out the hour mark of the time, this is done by adding the duration to the hour then dividing by 60 to give duration in hours adding this to the minutes left over
##(modulo equation) and then these 2 added together and "modulo'd" from 24 hours gives the hour for the time  ##
time_hour = (hour + dura // 60 + (mins+ dura % 60) // 60) % 24 ## The same is then repeated for minutes but worked out for the remainder using modulo. 
time_min = (mins+ dura%60)%60## The same is then repeated for minutes but worked out for the remainder using modulo. This is then used with the modulo equation for 60 minutes in the hour to give remaining miniutes ##
print("It will end at " + str(time_hour) + ":" + str(time_min)) ## These 2 added together as strings then give the expected end time ##
