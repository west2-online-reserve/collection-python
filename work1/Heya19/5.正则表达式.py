import re

def validate_password(password):
    pattern = r"^[A-Za-z0-9]{6,18}$"
    return bool(re.match(pattern, password))

# 测试代码
if __name__ == "__main__":
    while True:
        password = input("请输入密码进行测试（或输入'exit'退出）：")
        if password.lower() == 'exit':
            break
        if validate_password(password):
            print("密码有效!")
        else:
            print("密码无效!")
