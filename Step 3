#Abigail Keane 2/13/24

#program goal: ask a customer for an amount of purchases and correctly calculate
#cost of purchased items, with tax.

#User Info
print("The price of items of the menu is:")
print("Donut: $6")
print("Coffee: $5")
print("Muffin: $4")
print("Bagel: $3")

#Gather input from user
donutAmount = int(input("How many donuts would you like to buy? "))
coffeeAmount = int(input("How many coffees would you like to buy? "))
muffinAmount = int(input("How many muffins would you like to buy? "))
bagelAmount = int(input("How many bagels would you like to buy? "))

#get total cost before tax
donutCost = donutAmount * 6
coffeeCost = coffeeAmount * 5
muffinCost = muffinAmount * 4
bagelCost = bagelAmount * 3
initialCost = donutCost + muffinCost + coffeeCost + bagelCost 
#get total cost after tax
taxCost = initialCost * 0.06
finalCost = taxCost + initialCost

#receipt
print ("***************************************")
print ("My Coffee and Muffin Shop Receipt")

#if statements to get correct plurality
if donutAmount != 1:
    print (donutAmount, "Donuts at $6 each = $" + str(donutCost))
else:
    print (donutAmount, "Donut at $6 each = $" + str(donutCost))
if coffeeAmount != 1:
    print (coffeeAmount, "Coffees at $5 each = $" + str(coffeeCost))
else:
    print (coffeeAmount, "Coffee at $5 each = $" + str(coffeeCost))
if muffinAmount != 1:
    print (muffinAmount, "Muffins at $4 each = $" + str(muffinCost))
else:
    print (muffinAmount, "Muffin at $4 each = $" + str(muffinCost))
if bagelAmount != 1:
    print (bagelAmount, "Bagels at $3 each = $" + str(bagelCost))
else:
    print (bagelAmount, "Bagel at $3 each = $" + str(bagelCost))
    
#final Calculations
print ("6% tax: $" + str(taxCost))
print ("---------")
print ("total: $" + str(finalCost))
print ("***************************************")
print ("Thanks for shopping with us, have a nice day!")
