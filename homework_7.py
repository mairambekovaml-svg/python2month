import sqlite3
def create_table():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    conn.commit()
    conn.close()
def insert_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("War and Peace", "Leo Tolstoy", 1869, "Novel", 1225, 3),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 4),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 400, 6),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Novel", 671, 2),
        ("The Alchemist", "Paulo Coelho", 1988, "Adventure", 208, 7),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fable", 96, 5),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopia", 311, 3),
        ("Moby Dick", "Herman Melville", 1851, "Adventure", 635, 2),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 4)
    ]
    cursor.executemany("""
    INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)
    """, books)
    conn.commit()
    conn.close()
def get_all_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
if __name__ == "__main__":
    create_table()
    insert_books()
    get_all_books()