# 1. enumerate()  - keeps track of the index for an iterable and returns a enumerate.
# it gives you the item and it's list.
languages = ['english', 'spanish', 'french', 'russian']

print(list(enumerate(languages))) # [(0, 'english'), (1, 'spanish'), (2, 'french'), (3, 'russian')]

# using enumerate with for loop

languages = ['english', 'spanish', 'french', 'russian']
for index,language in enumerate(languages):
    print(f'Index: {index} and language: {language}')

# the enumerate() function also accepts an optional start argument that specifies the starting value for the count.
languages = ['spanish', 'english', 'russian', 'swahili']
for index,language in enumerate(languages,1):
    print(f'Index: {index} and Language: {language}')

#2. zip() function - iterate over multiple iterables in parallel. combines lists into pairs of elements and returns an iterator of tuples.
# it combines multiple list side by side.
developers = ['antony', 'daniel', 'derrick', 'joshua']
ids = [1,2,3,4]
print(list(zip(developers,ids)))

# using the zip() function with for loop.

developers = ['antony', 'daniel', 'derrick', 'joshua']
ids = [1,2,3,4]
for name,dev_id in zip(developers,ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')