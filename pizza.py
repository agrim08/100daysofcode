print("Welcome to My Pizza Deliveries!")
size = input("What size pizza do you want?S,M or L?")
add_onion = input("Do you want to add oninon, Y or N?")
extra_cheese = input("Do you want to add extra cheese, Y or N?")

price = 0

if size  == "S":
    price+= 15
elif size == "M":
    price+= 20
else:
    price+= 25

if add_onion == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1
    
print(f"Your final bill is ${price}")
