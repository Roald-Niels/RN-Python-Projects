def main():
  class vehicle:
    def _init_(self):
      self.vehicle_options = {'make': '', 'model': ''}

  def setmake(self, make):
    self.vehicle_options['make'] = make

  def setmodel(self, model):
    self.vehicle_options['model'] = model

  class car(vehicle):
    def setdoors(self, doors):
      self.vehicle_options ['doors'] = doors

  class pickup(vehicle):
    def setbedlength(self, bedlength):
      self.vehicle_options ['bedlength'] = bedlength

print('Welcome to your virtual garage.')
start = input('Press 1 to create a car, 2 to create a pickup and 3 to quite.')

if int(start) ==1:
  make = input("what is the make of the car? ")
  model = input("what is the model of the car? ")
  doors = input("How many doors does the car have? " )

elif int(start) ==2:
  make = input("what is the make of the pickup truck? ")
  model = input("what is the model of the pickup truck? ")
  bedlength = input("How long is the bed length? ")
if int(start) == 1:
  print("You have successfully added a new car ")
  print(make, model, doors +str("door"))

elif int(start) == 2:
  print("You have successfully added a new pickup ")
  print(make, model, bedlength +str("bedlength"))

import os
import sys

restart = input("\nDo you want to restart the program? [y/n] > ")

if restart == "y":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
else:
    print("\nThe programm will me closed...")
    sys.exit(0)
