
from databasemanager import store_password


def menu():
    print("-"*30)
    print(("-") + "Menu" + ("-"*13))
    print("1.新しいパスワードを作る")
    print("2.パスワードをメールで検索する")
    print("3.パスワードをアプリ・サイトで検索する")
    print("Q.終了する")
    print("-"*30)
    return input(":")


def create():
    print('Please proivide the name of the site or app you want to generate a password for')
    app_name = input()
    print('Please provide a \'sample\' password for this site')
    passw = input()
    print('-'*30)
    print('')
    print('')
    print('-' * 30)
    user_email = input('Please provide a user email for this app or site')
    username = input(
        'Please provide a username for this app or site (if applicable)')
    if username == None:
        username = ''
    url = input(
        'Please paste the url to the site that you are creating the password for')
    store_password(passw, user_email, username, url, app_name)
