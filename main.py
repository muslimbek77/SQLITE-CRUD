import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

#CREATE
# table = """ CREATE TABLE IF NOT EXISTS Students (
#             First_Name CHAR(25) NOT NULL,
#             Last_Name CHAR(25),
#             Phone_number CHAR(13) UNIQUE NOT NULL,
#             Age INT,
#             Address TEXT
#         ); """

# cursor.execute(table)


# text = """INSERT INTO Students 
# (First_name,Last_name,Phone_number,Age,address) VALUES
# ('Azizbek','Mirzaolimov','+998901465737','16','2-Mikrorayon'),
# ('Javohir','Oxunjonov','+998880070032','17','Asaka')
# """
# cursor.execute(text)
# connection.commit()

#READ
text = """SELECT * FROM STUDENTS;"""
cursor.execute(text)
all_students = cursor.fetchall()
print(all_students)
