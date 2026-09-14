
# while loop - repeats a block of code until condition is false.
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1 - 5)'))
    if guess != secret_number:
        print('Wrong! guess try again')
print('You got it!')

# python also supports the break and continue statements.
# 1. break statement - is used to stop the execution of a loop.

developer_names = ['jess', 'antony', 'joshua']
for developer in developer_names:
    if developer == 'antony':
        break
    print(developer)
# only the name jess will be printed because when developer name == antony the loop breaks.

# 2. continue statement
for developer in developer_names:
    if developer == 'antony':
        continue
    print(developer)

# names jess and joshua will be printed because the continue statement skips the second iteration of the loop when develope == antony and does not print name and antony to console.
# both for and while loops can be combined with an else clause which is executed only when the loop is not terminated by break stateent.

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'"{word} contains the vowel "{letter}')
            break
else:
    print(f'"{word}" has no vowels')