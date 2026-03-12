import sqlite3

conn = sqlite3.connect("tools.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tools (
id INTEGER PRIMARY KEY,
name TEXT,
category TEXT,
performance INTEGER
)
""")

tools = [
("Canva AI","presentation",90),
("Gamma AI","presentation",92),
("Midjourney","image",95),
("DALL-E","image",88),
("GitHub Copilot","coding",94),
("ChatGPT","general",93)
]

cursor.executemany(
"INSERT INTO tools (name,category,performance) VALUES (?,?,?)",
tools
)

conn.commit()
conn.close()

print("Tools inserted successfully")