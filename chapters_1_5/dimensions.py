# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
#
# # tuples does not support re-assignment
# # dimensions[0] = 250
#
# # Defining one tuple
# my_t = (3,)
#
# for dimension in dimensions:
#     print(dimension)
#
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
#
# # The variable pointing to the tuple can be reassigned
# dimensions = (400, 100, 500)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)


buffetts = ('Yam & Egg', 'Eba & Ogbono', 'Jollof Rice', 'Suya', 'Dodo & Ewa')
print(buffetts)
for buffett in buffetts:
    print(buffett)

    # buffetts.append('Jerk Chicken')
    # print(buffetts)

print("Original Buffetts:")
for buffett in buffetts:
    print(buffett)

buffetts = ('Full English', 'Sausage & Msh', 'Sandwich', 'Oat', 'Fish & Chips')
print("\nModified buffetts:")
for buffett in buffetts:
    print(buffett)
