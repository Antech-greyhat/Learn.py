
word = input('Input your favorite word:')
print(f'You Entered {word} as your favorite')

palindrome = word[::-1]
print(palindrome)
if word.lower() == palindrome:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')