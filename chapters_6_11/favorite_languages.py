favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# language = favorite_languages['sarah'].title()
# print(f"\nSarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

print('****************************')
for name in favorite_languages.keys():
    print(name.title())
