from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory storage (no DB needed → keeps pipeline simple)
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "available": True},
    {"id": 2, "title": "The DevOps Handbook", "author": "Gene Kim", "available": True},
    {"id": 3, "title": "Python Crash Course", "author": "Eric Matthes", "available": False},
]
next_id = 4


# ---------- Page 1: Home ----------
@app.route('/')
def home():
    total = len(books)
    available = sum(1 for b in books if b["available"])
    issued = total - available
    return render_template('index.html',
                           total=total,
                           available=available,
                           issued=issued)


# ---------- Page 2: Add Book ----------
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    global next_id
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        if title and author:
            books.append({
                "id": next_id,
                "title": title,
                "author": author,
                "available": True
            })
            next_id += 1
        return redirect('/books')
    return render_template('add_book.html')


# ---------- Page 3: View Books ----------
@app.route('/books')
def view_books():
    return render_template('view_books.html', books=books)


# ---------- Extra actions (still part of page 3) ----------
@app.route('/issue/<int:book_id>')
def issue_book(book_id):
    for b in books:
        if b["id"] == book_id:
            b["available"] = False
            break
    return redirect('/books')


@app.route('/return/<int:book_id>')
def return_book(book_id):
    for b in books:
        if b["id"] == book_id:
            b["available"] = True
            break
    return redirect('/books')


@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return redirect('/books')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)