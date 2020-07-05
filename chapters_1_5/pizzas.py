pizzas = ['pepperoni', 'margherita', 'veggie', 'meaty', 'bbq chicken']
for pizza in pizzas:
    print(pizza)
    # print(f" I like to eat {pizza.title()} pizza.\n")
# print(f" I really like to eat meaty pizzas, all pizzas are good.")

print(f" \nThe first three pizzas in the list are:")
print(pizzas[0:3])

print(f" \nThree pizzas from the middle of the list are:")
print(pizzas[2:])

print(f" \nThe last three pizzas in the list are:")
print(pizzas[-3:])

my_pizzas = ['pepperoni', 'margherita', 'veggie', 'meaty', 'bbq chicken']
friend_pizzas = my_pizzas[:]

my_pizzas.append('spicy bbq')
friend_pizzas.append('assorted meat')

print("My favorite pizzas are:")
print(my_pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
