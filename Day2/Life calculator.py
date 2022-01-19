#Life calculator
#   (_*5) simply itterate the character no. of time we want it   
print("_"*5 + "welcome to Life Calculator" + "_"*5)

#Type casting of Input String to Int
age = int(input("\nWhat is your age: "))
year_remain = 90 - age
week_remain = year_remain*52
days_remain = year_remain*365

#use of f string to print the variable value with string 
print(f"Year remain {year_remain}\nWeek remain {week_remain}\nDays remain {days_remain}")