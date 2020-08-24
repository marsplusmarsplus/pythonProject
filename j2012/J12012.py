speedLimit = eval(input("Enter the speed limit: "))
recordedSpeed = eval(input("Enter the recorded speed of the car: "))
if recordedSpeed <= speedLimit:
    print("Congratulations, you are within the speed limit!")
elif recordedSpeed <= speedLimit + 20:
    print("You are speeding and your fine is $100.")
elif recordedSpeed <= speedLimit + 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")
