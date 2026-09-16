# zip() - walking through two list side by side. pairs up items from 2 list by position.

developers = ['antony', 'antech', 'technorant']
ids = [1,2,3]
print(list(zip(developers,ids)))


names = ['Army', 'Brian', 'Cara']
scores = [85,72,90]
for name,score in zip(names,scores):
    print(f'{name} scored {score}')