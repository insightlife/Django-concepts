from Include.database_connection import Database

def creat_table():
    with Database('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('create table if not exists book(name text,author text,read integer)')

def add_book(name,author):
    with Database('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute(f'insert into book values("{name}","{author}",8)')

def read_book():
    with Database('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('select * from book')
        book=cursor.fetchall()

def fliter():
    with Database('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('update book set name="suman" where read==8')
def drop():
    with Database('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DROP bo')

creat_table()
read_book()
fliter()
