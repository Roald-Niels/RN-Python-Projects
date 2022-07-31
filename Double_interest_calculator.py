print ("This program calculates how many years it will take for your   new investment to double in size.")
investment = input('How much will your initial investment be? $ ')#initial investment
rate = input("Please enter the interest percentage rate on your account: ") #interest rate input
years = 0 #sets years to zero
value = int(investment)
 
while value <= int(investment)*2: 
    value = value + value*((float(rate)/100)) #calculates investment
    years = years + 1 #adds a year for every loop
    
print ("Your investment doubles in",years,"years") 
