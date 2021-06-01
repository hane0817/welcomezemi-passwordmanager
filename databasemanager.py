import psycopg2


def connect():
    try:
        connection = pyscopg2.connect(
            user='shuhei1', password='shuhei1', host='127.0.0.1', database='passwordmanager')
        return connection

    except (Exception, psycopg2.Error) as error:
        print(error)


def store_password():
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts(password, email, username, url, app_name) VALUES(%s, %s,%s,%s,%s)"""
        record_to_insert = (password, user_mail, username, url, app_name)

    except (Exception, psycopg2.Error) as error:
        print(error)

        def store_password():
    try:

    except (Exception, psycopg2.Error) as error:
        print(error)
