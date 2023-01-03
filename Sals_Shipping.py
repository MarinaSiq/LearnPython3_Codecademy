weight = float(input("What is the weight of the package? "))
ground_shippping = ""
ground_shipping_premium = ""
drone_shipping = ""
ground_price = 0
ground_prem_price = 0
drone_price = 0


#ground_price
if weight <= 2.0:
  ground_price = weight * 1.5 + 20.0
elif weight <= 6.0:
  ground_price = weight * 3.0 + 20.0
elif weight <= 10.0:
  ground_price = weight * 4.0 + 20.0
else:
  ground_price = weight * 4.75 + 20.0

print("The Ground Shipping Price is: $" + str(ground_price))

#ground_prem_price
ground_prem_price = 125.0

print("The Ground Premium Shipping Price is: $" + str(ground_prem_price))

#drone_price
if weight <= 2.0:
  drone_price = weight * 4.5
elif weight <= 6:
  drone_price = weight * 9.0
elif weight <= 10:
  drone_price = weight * 12.0
else:
  drone_price = weight * 14.25

print("The Drone Shipping Price is: $" + str(drone_price))

if ground_price < ground_prem_price and drone_price:
  print("The best choice is: Ground Shipping")
elif ground_prem_price < ground_price and drone_price:
  print("The best choice is: Ground Premium Shipping")
elif drone_price < ground_prem_price and ground_price:
  print("The best choice is: Drone Shipping")
else:
  print("Seems that you have more than one best shipping option. Review prices above.")
