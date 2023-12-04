import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks INTEGER
    )
''')


data_to_insert = [
    (1, 'Tom', 15,100),
    (2, 'Jerry', 19,75),
    (3, 'Spike', 10,83),
]

cursor.executemany('INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)', data_to_insert)
res = cursor.execute('SELECT * from students ')
print("Initial database")
print(res.fetchall())
res  = cursor.execute('DELETE FROM students WHERE id = 2')
print("After deletion")
res = cursor.execute('SELECT * from students ')
print(res.fetchall())
res = cursor.execute('UPDATE  students SET age = 20 where name = "Spike"')
print("After updation")
# print(res.fetchall())
res = cursor.execute('SELECT * from students ')
print(res.fetchall())
conn.commit()
conn.close()