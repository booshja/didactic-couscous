from flask import Flask, redirect, abort

app = Flask(__name__)

books = [
  {
    "id": "1",
    "title": "In Search of Lost Time",
    "author": "Marcel Proust",
    "quantity": 2
  },
  {
    "id": "2",
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "quantity": 5
  },
  {
    "id": "3",
    "title": "War and Peace",
    "author": "Leo Tolstoy",
    "quantity": 6
  },
]


@app.route("/books")
def getBooks():
    """
    docstring here
    """
    return
