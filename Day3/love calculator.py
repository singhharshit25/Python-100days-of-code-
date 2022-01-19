#Love calculator 
#we use lower() and count()

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#lower() - string in lowercase
lower = name1.lower() + name2.lower()
"""
t=0
r=0
u=0
e=0
l=0
o=0
v=0
e=0
t = t + lower.count("t")
r = t + r + lower.count("r")
u =r + u + lower.count("u")
count1 =u + e +lower.count("e")

"""
#count() - it is used counts the total no. of times a specific character in a string 
#the count() takes atleast one argument


"""

l=0
e=0
l = l + lower.count("l")

o = l + o + lower.count("o")

v =o + v + lower.count("v")

count2 = v + e + lower.count("e")

num = int(f"{count1}{count2}")

"""
t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")
true = t + r + u + e
e=0
l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")
love = l + o + v + e
true_love = int(str(true) + str(love))
if true_love<=10 or true_love>=90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")

elif true_love>=40 and true_love<=50 :
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")