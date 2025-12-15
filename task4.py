# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole") 

num = int(input("what is your number (greater than or equal to 0 and less than 10): "))
if 0 <= num < 10:
    print("The person at that position is:", people[num])
else:
    print("Invalid input")