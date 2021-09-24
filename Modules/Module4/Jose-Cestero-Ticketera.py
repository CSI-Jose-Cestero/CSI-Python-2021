from typing import MutableSequence


print("Welcome to Into The Heights!!!!!!")
print("The cost for each seat is the following: $65 for Upper Level, $75 for Main Level, $110 for Close Seat.")

UpperLevel = int(input("How many tickets are being bought for the upper level?"))
MainLevel = int(input("How many tickets are being bought for the main level?"))
CloseSeat = int(input("How many tickets are being bought for the close seats?"))
print()
def Sales(UpperLevel, MainLevel, CloseSeat):
  print(f"The cost for the upper level would be ${int(UpperLevel)*65}")
  print(f"The cost for the main level would be ${int(MainLevel)*75}")
  print(f"The cost for the close seats would be ${int(CloseSeat)*110}")

Sales(UpperLevel, MainLevel, CloseSeat)

ULS = UpperLevel * 65
MLS = MainLevel *75
CSS = CloseSeat *110

def TotalAmount(ULS, MLS, CSS):
 print(f"The total amount spent on tickets would be ${int(ULS) + int(MLS) + int(CSS)}")
print()
TotalAmount(ULS, MLS, CSS)

