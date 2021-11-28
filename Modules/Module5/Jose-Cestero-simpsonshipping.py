print("This is Simpson's Shipping!!")

weight = float(input("How much does your package weigh in pounds? "))

if(weight <= 2):
      print("Ground Shipping: $" + str(float((weight *1.75)+20)))
      print("Courier Shipping: $" + str(float((weight *3.5)+5)))
      print("Drone Shipping: $" + str(float((weight*5.25))))
      print("Ground Shipping Premium: $150.00")
elif(2<weight<=6):
      print("Ground Shipping: $" + str(float((weight *3.5)+20)))
      print("Courier Shipping: $" + str(float((weight *7)+8)))
      print("Drone Shipping: $" + str(float((weight*10.5))))
      print("Ground Shipping Premium: $150.00")
elif(6<weight<=10):
      print("Ground Shipping: $" + str(float((weight *4.5)+20)))
      print("Courier Shipping: $" + str(float((weight *9)+12)))
      print("Drone Shipping: $" + str(float((weight*13.5))))
      print("Ground Shipping Premium: $150.00")
elif(weight<10):
      print("Ground Shipping: $" + str(float((weight * 5.25)+20)))
      print("Courier Shipping: $" + str(float((weight *10.5)+15)))
      print("Drone Shipping: $" + str(float((weight*15.75))))
      print("Ground Shipping Premium: $150.00")

print("We hope you pick one of our choices!!!")



