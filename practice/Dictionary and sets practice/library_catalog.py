from os import read

books = [
    {'title': '1982', 'author': 'George Orwell', 'read': True},
    {'title': 'Dune', 'author': 'Frank Herbert', 'read': False},
    {'title': 'The Hobit', 'author': 'Tolkien', 'read': False}
]

for book in books:
    if book['read'] == True:
        status = 'Read'
    else:
        status = 'Not Read Yet'
    print(f"{book['title']} by {book['author']} ({status})")

def count_unread_books(book_list):
    count = 0
    for book in book_list:
        if book['read'] == False:
            count += 1
    return count
print(f'you have {count_unread_books(books)}  unread books')