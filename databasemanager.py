import psycopg2


def connect():
    try:
        connection = psycopg2.connect(
            user='jintonic', password='jintonic', host='127.0.0.1', database='password_manager')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)


def store_password(password, user_mail, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts(password, email, username, url, app_name) VALUES(%s, %s,%s,%s,%s)"""
        record_to_insert = (password, user_mail, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


# def find_password():
#     try:

#     except (Exception, psycopg2.Error) as error:
#         print(error)
