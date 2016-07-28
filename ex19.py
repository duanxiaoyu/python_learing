def cheese_and_crakers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Get a blanket!\n"



print "We can give the function numbers directly!\n"
cheese_and_crakers(10, 20)

print "Or we can use variables from our inputs:"

amount_of_cheese = int(raw_input("amount of cheese:"))
amount_of_crackers = int(raw_input("amount of crakers:"))
cheese_and_crakers(amount_of_cheese, amount_of_crackers)
    
    
