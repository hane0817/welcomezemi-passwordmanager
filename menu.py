
from databasemanager import store_password, find_password, encpass


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
    print('アプリやサイトの名前')
    app_name = input()
    print('パスワード')
    plaintext = input()
    passw = encpass(plaintext)
    print(passw)

    user_email = input('メールアドレス')
    username = input(
        'ユーザネーム（なければっ空白）')
    if username == None:
        username = ''
    url = input(
        'サイトのURL（なければ空白）')
    store_password(passw, user_email, username, url, app_name)


def find_app():
    print('provide app name:')
    app_name = input()
    find_password(app_name)
