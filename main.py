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
# ('Azizbek','Mirzaolimov','+9989011465737','16','2-Mikrorayon'),
# ('Javohir','Oxunjonov','+9988800270032','17','Asaka')
# """
# cursor.execute(text)
# connection.commit()

# #READ
# text = """SELECT * FROM STUDENTS;"""
# cursor.execute(text)
# all_students = cursor.fetchall()
# print(all_students)

# #UPDATE
# text = """UPDATE Students
# SET address = 'Andijon, 2-Mikrarayon'
# WHERE Phone_number='+998901465737';"""
# cursor.execute(text)
# connection.commit()

# text = """DELETE FROM Students WHERE phone_number='+9989011465737' or phone_number='+9988800270032';"""
# cursor.execute(text)
# connection.commit()

text = """DROP TABLE Students;"""
cursor.execute(text)
connection.commit()

#READ
text = """SELECT * FROM STUDENTS;"""
cursor.execute(text)
all_students = cursor.fetchall()
print(all_students)

connection.close()