print("Welcome to Into The Heights!!!!!!")
print("The cost for each seat is the following: $65 for Upper Level, $75 for Main Level, $110 for Close Seat.")

UpperLevel = int(input("How many tickets are being bought for the upper level?"))
MainLevel = int(input("How many tickets are being bought for the main level?"))
CloseSeat = int(input("How many tickets are being bought for the close seats?"))

def Sales(UpperLevel, MainLevel, CloseSeat):
  print("The cost for the upper level would be $" + (int(UpperLevel*65))
  print("The cost for the main level would be $" + (int(MainLevel*75)))
  print("The cost for the close seats would be $" + (int(CloseSeat*110)))

Sales(UpperLevel, MainLevel, CloseSeat)

print("The total amount spent on tickets would be $" + (int((UpperLevel*65)+(MainLevel*75)+(CloseSeat*110))))

