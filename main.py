import sqlite3
from faker import Faker

# Faker obyektini yaratish
fake = Faker()

# SQLite bazasiga ulanish
conn = sqlite3.connect("problems.db")
cursor = conn.cursor()

# Fake ma'lumotlarni qo'shish
def insert_fake_data():
    # Platforms jadvaliga ma'lumot qo'shish
    platforms = ["LeetCode", "Codeforces", "HackerRank", "GeeksForGeeks"]
    for name in platforms:
        cursor.execute("INSERT INTO platforms (name) VALUES (?)", (name,))

    # Problems jadvaliga ma'lumot qo'shish
    for _ in range(10):  
        url = fake.url()
        platform_id = fake.random_int(min=1, max=len(platforms))
        cursor.execute("INSERT INTO problems (url, platform_id) VALUES (?, ?)", (url, platform_id))

    # Keywords jadvaliga ma'lumot qo'shish
    keywords = ["algorithm", "python", "database", "sorting", "dynamic programming"]
    for name in keywords:
        cursor.execute("INSERT INTO keywords (name) VALUES (?)", (name,))

    # Solutions jadvaliga ma'lumot qo'shish
    for _ in range(10):
        problem_id = fake.random_int(min=1, max=10)
        query = fake.sentence()
        keyword_id = fake.random_int(min=1, max=len(keywords))
        cursor.execute("INSERT INTO solutions (problem_id, query, keyword_id) VALUES (?, ?, ?)", (problem_id, query, keyword_id))

    # O'zgarishlarni saqlash
    conn.commit()

# Fake ma'lumot qo'shish funksiyasini chaqirish
insert_fake_data()

# Ulashni yopish
conn.close()

print("Fake ma'lumotlar bazaga muvaffaqiyatli qo'shildi! ✅")
