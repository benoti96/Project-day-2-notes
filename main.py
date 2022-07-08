#Data Types
#print("Benjamin"[1])
#print(45+34) #Answer is 79
#print("45" + "39") #Answer is 4539
#print(len("23")) #answer is 2

#num_char = len(input("What is your name?\n"))
#Intially we could not combine an integer and a string. So we changed num_char to a string (as seen below) and now we can print the statement on line 10.
#new_num_char = str(num_char)
#print("Your name has" + " " + new_num_char + " " + "characters.") 

#print(type(num_char))



#print(10 + float("2.3")) # Answer is 12.3



#two_digit_number = input("Type a two digit number\n")
#print(str(two_digit_number))

#======================

#three_digit_number = input("Enter in a three digit number:\n")

#print(type(three_digit_number))

#first_digit = three_digit_number[0]
#second_digit = three_digit_number[1]
#third_digit = three_digit_number[2]

#result = int(first_digit) + int(second_digit) + int(third_digit)


#print(result)

#print(2**3)

#======================
#BMI Calculator
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")

#BMI = int(weight) / float(height) ** 2

#bmi_as_int = int(BMI) # adding the int changes the BMI to a whole number rather than decimal number.

#print(bmi_as_int)

#BMI = int(weight) // round(float(height)) ** 2
#print(BMI)

#===============
#NUMBER MANIPULATION AND F Strings in Python

print(round(8/3)) # rounds the answer to nearest whole number

print(round(8/3, 3)) # rounds the asnwer to 3 decimal places.

print(8 //3) # the double slash changes number to integer straight away

result = round(4/2)

result /= 2 # putting /= lets you continue divding or multiplying the result

print(round(result))

score = 2
score+=2 #adds on 2 to the previous value of socre
print(score)

#===============
score = 0
height = 1.8
weight = 90


#the f string function lets us automatically convert all data types into a way which lets us combine them in a string straight away.
print(f" Your score is {score}, your height is {height}, and your weight is weight {weight}")


#====================
#Challenge for day 2
#CREATE A PROGRAM USING MATHS AND F-STRINGS THAT TELLS US HOW MANY DAYS,WEEKS, MONTHS WE HAVE LEFT IF WE LIVE UNTIL 90 YEARS old
#Input always creates a string data type

age = input("What is your current age?")
age_as_int = int(age) #Input always creates string data type so change it into integer if necessary

Ninety_years_in_days = 90*365
Ninety_years_in_months = 90*12
years_remaining = 90 - age_as_int
days_remaining= Ninety_years_in_days - age_as_int*365
print(years_remaining)
print(days_remaining)
months_remaining = Ninety_years_in_months - age_as_int*12
print(months_remaining)

print(f"You have {days_remaining} days, {months_remaining} months, and {years_remaining} years left")








