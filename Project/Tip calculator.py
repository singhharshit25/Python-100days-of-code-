print("Welcome to Tip Calculator")
bill=float(input("What is the total bill? $ "))
per =float(input("What percentage tip you like to Give? 10,12 or 15 "))

#input is typecast from int to int only passing float will generate a invalid literal error

split = int(input("How many people split the bill? "))
print(type(split))
tip = float(bill*per)/100
total = bill + tip
# this will roundof print the decimail digit upto 2 decimal place but it zero is at last deciaml place it not going to print this 
print("Each have to pay: ",round((total/split),2))

#this will give the value upto 2 decimal place and include zero
print("Each one have to pay {:.2f}".format(round(total/split,2)))



# in int it does not round up the number
#r=12.467
#print(round(r))

