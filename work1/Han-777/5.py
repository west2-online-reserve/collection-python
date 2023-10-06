# 写一个正则表达式，用于验证用户密码，长度在6~18 之间，只能包含英文和数字
import re


def check_password(pwd):
    res = re.search(r"^[a-zA-Z0-9]{6,18}$", pwd)
    return True if res else False


if __name__ == '__main__':
    password = input("please input the password:")
    print(check_password(password))
