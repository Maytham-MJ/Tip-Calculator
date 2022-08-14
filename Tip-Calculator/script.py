#First we ask the user for input
# Then we will code the bill to be changable 
# The tip will be %20 of the total bill amount (the bill / %20 )
# Finally we will print the amount using float to capture the whole amount (float(tip))

print("How much was your bill?")
bill = int(input())
tip= (bill * 0.20)
print (float (tip))
