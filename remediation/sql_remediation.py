
import sqlite3

# Create a small test database in memory
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("CREATE TABLE products (id INTEGER, name TEXT)")

cursor.executemany(
    "INSERT INTO products VALUES (?, ?)",
    [
        (1, "Apple Juice"),
        (2, "Banana Juice"),
        (3, "Orange Juice")
    ]
)

def vulnerable_search(search_term):
    query = f"SELECT * FROM products WHERE name = '{search_term}'"
    try:
        return cursor.execute(query).fetchall()
    except sqlite3.Error as error:
        return f"SQL Error: {error}"

def secure_search(search_term):
    query = "SELECT * FROM products WHERE name = ?"
    return cursor.execute(query, (search_term,)).fetchall()

test_input = "' OR 1=1--"

print("Vulnerable query result:")
print(vulnerable_search(test_input))

print("\nSecure query result:")
print(secure_search(test_input))

connection.close()
