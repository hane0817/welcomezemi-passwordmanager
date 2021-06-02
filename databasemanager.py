import psycopg2
from cryptography.fernet import Fernet


def connect():
    try:
        connection = psycopg2.connect(
            user='shuhei1', password='shuhei1', host='127.0.0.1', database='password_managers3')
        return connection

    except (Exception, psycopg2.Error) as error:
        print(error)


def store_password(password, user_mail, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_mail, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


def find_password(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """SELECT password FROM accounts WHERE app_name =  '""" + app_name + "'"
        cursor.execute(postgres_insert_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        print('password is: ')
        print(result[0])
        # afterdec = decpass(result[0])
        # print(afterdec)
    except (Exception, psycopg2.Error) as error:
        print(error)


def encpass(plaintext):
    try:
        key = Fernet.generate_key()
        encpass.fernet = Fernet(key)
        encText = encpass.fernet.encrypt(plaintext.encode())
        print(encText)
        return encText
    except (Exception, psycopg2.Error) as error:
        print(error)


# def decpass(encText):
#     try:
#         passw = encpass.fernet.decrypt(encText).decode()
#         return passw
#     except (Exception, psycopg2.Error) as error:
#         print(error)
