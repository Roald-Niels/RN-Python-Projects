stocks = {
'DIS':118.27,
'WBA': 45.54,
'NFLX': 215.52, 
'ATVI': 78.61, 
'SONY': 85.60, 
'CVS': 101.68, 
'NTDOF': 497, 
'TSLA': 1005.05, 
'WMT': 156.86,
'STAG': 40.77
}

entry = input("Type ticker symbol: ")
if entry in stocks:
    print ("Ticker symbol: " + entry)
    print ("Share value: " + str(stocks[entry]) + "\n")
else:
  print("Ticker not found.")
