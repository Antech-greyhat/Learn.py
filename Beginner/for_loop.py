# loops are used to repeat a block of code.
# 1. for loop - repeat a block of code for every item in a collection.
# for loop is used to iterate over a sequence and execute a block of code once for each item in that sequence.

languages = ('rust', 'java', 'python')

for language in languages:
    print(language)
#rust
#java
#python
# you can also use for loop to iterate through other iterables like strings.
for char in 'code':
    print(char) #c
                #o
                #d
                #e
# you can also nest for loops in python.
categories = ['fruit', 'vegetables']
foods = ['apples', 'carrot', 'banana']
for category in categories:
    for food in foods:
        print(category, food)