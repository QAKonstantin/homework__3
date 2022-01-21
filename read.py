from csv import DictReader
import json

with open("./Files/users.json", "r") as f:
    users = json.loads(f.read())
    user_mas = []
    for i in range(len(users)):
        user = {}
        user['name'] = users[i]['name']
        user['gender'] = users[i]['gender']
        user['address'] = users[i]['address']
        user['age'] = users[i]['age']
        user['books'] = []
        user_mas.append(user)
        del user

with open('./Files/books.csv', newline='') as f:
    reader = DictReader(f)
    book_mas = []
    for row in reader:
        book_mas.append(row)
    books = []
    for i in range(len(book_mas)):
        book = {}
        book['title'] = book_mas[i]['Title']
        book['author'] = book_mas[i]['Author']
        book['pages'] = int(book_mas[i]['Pages'])
        book['genre'] = book_mas[i]['Genre']
        books.append(book)
        del book

i, j = 0, 0
while i < len(books):
    if j < len(user_mas):
        user_mas[j]['books'].append(books[i])
        j += 1
    else:
        j = 0
    i += 1

with open("result.json", "w") as result_out:
    result_out.write(json.dumps(user_mas, indent=4))
