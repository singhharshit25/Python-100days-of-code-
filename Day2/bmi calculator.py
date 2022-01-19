weight = int(input("Enter your Weight: "))
height = input("Enter your Height: ")
bmi= weight/float(height)**2
print(bmi)
bmi_int_value = int(bmi)
print("integer value of bmi :",bmi_int_value )