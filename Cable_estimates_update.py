display_message = 'Welcome to cable estimates. Please fill in the information below for the most accurate estimate.'
print(display_message)

request_companyname = input('What is the name of your company? ')
print('Company name: ')
print(request_companyname)
request_feet = input('How many feet of cable are you planning to have us install for you? ')
if int(request_feet)< 100:
  cost = 0.87 * int(request_feet)
elif int(request_feet)< 250:
  cost = 0.80 * int(request_feet)
elif int(request_feet)< 500:
  cost = 0.70 * int(request_feet)
elif int(request_feet)> 500:
  cost = 0.50 * int(request_feet)
print('Companyname:') 
print(request_companyname)
print('Requested amount of feet:')
print(request_feet)
print(f"Your total cost will be ${cost}")
