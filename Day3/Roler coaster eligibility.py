#Checking eligibility for Rolercoster ride using if else
height = int(input("Enter your Height in cm: "))
if height>=120:
  print("You are eligible for Rolercoaster ride")
  age= int(input("Enter your age: ")
  )
  if age>=45 and age<=55:
    bill=0
    print("Your ride is free")
  elif age>18:
    bill=12
    print("Adult ticket of $12")
  elif age>=12:
    bill=7
    print("Teenage ticket of $7")
  elif age<12:
    bill=5
    print("Children ticket of $5")

  want_ticket=input("Do you want a photo Taken for $3? Y or N: ")
  if want_ticket=='Y' or 'y':
    bill+=3
    print(f"Your final bill is ${bill}")
else:
  print("You are not eligible for Rolercoaster ride")
