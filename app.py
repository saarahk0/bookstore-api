from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "Title": "Harry Potter", "author": "J.K. Rowling", "price": 500, "in_stock": True},
    {"id": 2, "Title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 700  , "in_stock": False},
    {"id": 3, "Title": "Moby Dick ", "author": "Herman Melville", "price": 1000, "in_stock": True},
]

@app.route('/')
def welcome():
    return "Hi, welcome to my bookstore API!"

@app.route('/search')
def search_books():
    title = request.args.get('title', '').lower()
    print("Searching for title:", title)
    if not title:
        return jsonify({"error": "Please provide a title to search"}), 400
    result = [book for book in books if title in book['title'].lower()]
    return jsonify(result)

# View book details by ID
@app.route('/book/<int:book_id>')
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Add a new book
@app.route('/book', methods=['POST'])
def add_book():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    required_fields = ['title', 'author', 'price', 'in_stock']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400
    
    new_id = max(book['id'] for book in books) + 1 if books else 1
    new_book = {
        "id": new_id,
        "title": data['title'],
        "author": data['author'],
        "price": data['price'],
        "in_stock": data['in_stock']
    }
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)
