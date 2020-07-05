motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles.insert(4, 'kawasaki')
# print(motorcycles)
# motorcycles.insert(0, 'BMW')
# motorcycles.insert(0, 'Harley-Davidson')
# motorcycles.insert(0, 'Triumph')
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)


popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

popped_motorcycle = ['honda', 'yamaha', 'ducati', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
