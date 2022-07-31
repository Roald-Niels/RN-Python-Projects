print('Hello! Welcome to our miles to kilometer conversion tool.') #intro message
def main():
    miles = float(input("Please enter a distance in miles so we can convert this for you: ")) #input number of miles
    conv_fac = 1.609 #conversion factor 
    #calculating how many kilometers 
    kilometers = miles * conv_fac
    print("The distance converted to kilometers is:",kilometers) #show end result
main()
print('In order to get an approximate result,the length value was     multiplied by 1.609')
