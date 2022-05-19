import os

filename = input("What is the name of your file? ")
with open(filename, "w") as f:
  print('What is your name?')
  f.write('Name,')
  f.write(input())
  print('What is your current address?')
  f.write('\nAddress,')
  f.write(input())
  print('What is your phone number?')
  f.write('\nPhone number,')
  f.write(input())

print('Please review the following information')
with open(filename, "r") as f:
  contents = f.read()
  print(contents)
