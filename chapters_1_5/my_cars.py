import random

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

car_list = cars[:]
print(car_list)
for car in car_list:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    this_car = random.choice(car_list)
    print(this_car)
    print(f"{car == this_car}, I predict True.")
