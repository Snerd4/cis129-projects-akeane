#Abigail Keane 2/13/24

#program goal: ask a customer for an amount of purchases and correctly calculate
#cost of purchased items, with tax.

#Initialization
print("The price of a coffee is $5. The price of a muffin is $4.")

#Gather input from user
coffeeAmount = int(input("How many coffees would you like to buy? "))
muffinAmount = int(input("How many muffins would you like to buy? "))

#get total cost before tax
coffeeCost = coffeeAmount * 5
muffinCost = muffinAmount * 4
initialCost = muffinCost + coffeeCost
#get total cost after tax
taxCost = initialCost * 0.06
finalCost = taxCost + initialCost

#receipt
print ("***************************************")
print ("My Coffee and Muffin Shop Receipt")

#if statements to get correct plurality
if coffeeAmount != 1:
    print (coffeeAmount, "Coffees at $5 each = $" + str(coffeeCost))
else:
    print (coffeeAmount, "Coffee at $5 each = $" + str(coffeeCost))
if muffinAmount != 1:
    print (muffinAmount, "Muffins at $4 each = $" + str(muffinCost))
else:
    print (muffinAmount, "Muffin at $4 each = $" + str(muffinCost))
    
#final Calculations
print ("6% tax: $" + str(taxCost))
print ("---------")
print ("total: $" + str(finalCost))
print ("***************************************")

