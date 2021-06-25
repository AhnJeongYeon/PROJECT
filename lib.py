import sqlite3
import pandas as pd
conn = sqlite3.connect("lib.db", isolation_level=None)
conn.execute("PRAGMA foreign_keys = ON")
c = conn.cursor()

c.execute("CREATE TABLE Books(book_id INTEGER PRIMARY KEY, ISBN UNIQUE, title TEXT, author TEXT, publisher TEXT)")
c.execute("CREATE TABLE BooksInStore(bs_id INTEGER PRIMARY KEY, book_id INTEGER, FOREIGN KEY(book_id) REFERENCES Books(book_id))")
c.execute("CREATE TABLE Members(name TEXT, email UNIQUE, phone INTEGER)")
c.execute("CREATE TABLE Rentals(bs_id INTEGER, member_id TEXT, start_date TEXT, end_date TEXT, FOREIGN KEY(member_id) REFERENCES Members(email), FOREIGN KEY(bs_id) REFERENCES BooksInStore(bs_id))")
c.execute("CREATE TABLE Ratings(rating INTEGER, book_id INTEGER, member_id TEXT, FOREIGN KEY(member_id) REFERENCES Members(email), FOREIGN KEY(book_id) REFERENCES Books(book_id))")

# 책 종류 삽입

c.execute("INSERT INTO Books VALUES(1, '12AB', 'hello', 'kim', 'dongyang')")
c.execute("INSERT INTO Books VALUES(2, '13AB', 'No woman', 'huh', 'gyobo')")
c.execute("INSERT INTO Books VALUES(3, '14AB', 'Man''s world', 'park', 'coin')")
c.execute("INSERT INTO Books VALUES(4, '15AB', 'higher place', 'ahn', 'heaven')")
c.execute("INSERT INTO Books VALUES(5, '16AB', 'Lost stars', 'bae', 'real')")
c.execute("INSERT INTO Books VALUES(7, '17AF', 'Coming up ros', 'chi', 'marvel')")

# 소유중인 책

c.execute("INSERT INTO BooksInStore VALUES(101, 1)")
c.execute("INSERT INTO BooksInStore VALUES(111, 2)")
c.execute("INSERT INTO BooksInStore VALUES(121, 3)")
c.execute("INSERT INTO BooksInStore VALUES(131, 4)")
c.execute("INSERT INTO BooksInStore VALUES(141, 5)")
c.execute("INSERT INTO BooksInStore VALUES(151, 6)")

# 회원관리

c.execute("INSERT INTO Members VALUES('jong bum park', '1234@naver.com', 2578)")
c.execute("INSERT INTO Members VALUES('seung hyun kim', '5678@naver.com', 3093)")
c.execute("INSERT INTO Members VALUES('jeong yeon ahn', '9012@naver.com', 8080)")
c.execute("INSERT INTO Members VALUES('jae wan huh', 'ohoh@naver.com', 6059)")

# #도서대여관리

# c.execute("INSERT INTO Rentals VALUES(1, '12AB', 'hello', 'kim', 'dongwon')")

# data_list = [( 7, 7, '1234@naver.com'), ( 8, 8, '1234@naver.com'), ( 9, 9, 'ohoh@naver.com')]
# for i in data_list:
#     query = "INSERT INTO `Ratings` VALUES (?,?,?);"
#     rating = i[0]
#     book_id = i[1]
#     member_id = i[2]
#     c.execute(query,[rating,book_id,member_id])
#     print(rating , book_id , member_id)

# 평가관리

query = "INSERT INTO `Ratings` VALUES (%d, %d, %s);"

input_data = [rating, book_id ,member_id]

c.execute("INSERT INTO Ratings VALUES( 6, 1, '1234@naver.com')")
c.execute("INSERT INTO Ratings VALUES( 5, 2, '1234@naver.com')")
c.execute("INSERT INTO Ratings VALUES( 4, 3, 'ohoh@naver.com')")
c.execute("INSERT INTO Ratings VALUES( 3, 4, '9012@naver.com')")
c.execute("INSERT INTO Ratings VALUES( 2, 5, '5678@naver.com')")
c.execute("INSERT INTO Ratings VALUES( 1, 6, '5678@naver.com')")

# 도서대여

c.execute("INSERT INTO Rentals VALUES(101, '1234@naver.com', '2021-06-01', '2021-06-03')")
c.execute("INSERT INTO Rentals VALUES(111, '1234@naver.com', '2021-06-01', '2021-06-03')")
c.execute("INSERT INTO Rentals VALUES(121, 'ohoh@naver.com', '2021-06-05', '2021-06-07')")
c.execute("INSERT INTO Rentals VALUES(131, '9012@naver.com', '2021-06-04', '2021-06-06')")
c.execute("INSERT INTO Rentals VALUES(141, '5678@naver.com', '2021-06-09', '2021-06-11')")
c.execute("INSERT INTO Rentals VALUES(151, '5678@naver.com', '2021-06-08', '2021-06-10')")











