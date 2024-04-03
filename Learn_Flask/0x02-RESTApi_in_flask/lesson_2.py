from flask import Flask, request, jsonify

app = Flask(__name__)

Books = [
    {
        "id": "1",
        "author": "Michael Owell",
        "language": "English",
        "Title": "Animal Farm"
    },
    {
        "id": "2",
        "author": "NOBLE MAN",
        "language": "French",
        "Title": "The male culture"
    },
    {
        "id": "3",
        "author": "The Spider",
        "language": "Noble language",
        "Title": "the Noble ways"
    },
    {
        "id": "4",
        "author": "Jorge luis Borges",
        "language": "Spanish",
        "Title": ""
    },
    {
        "id": "5",
        "author": "Emily Brunt",
        "language": "English",
        "Title": "Wuthering Heights"
    }
]

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(Books) > 0:
            return jsonify(Books)
        else:
            'Nothing Found', 404
            
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['Title']
        iD = Books[-1]['id'] + 1
        
        new_object = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            "title": new_title             
        }
        Books.append(new_object)
        return jsonify(Books), 201
    

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in Books:
            if book['id'] == id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in Books:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                }
                return jsonify(updated_book)
    if request.method == 'DELETE':
        for index, book in enumerate(Books):
            if book['id'] == id:
                Books.pop(index)
                return jsonify(Books)

    
if __name__ == "__main__":
    app.run()