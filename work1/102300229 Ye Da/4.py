import re
def judge(password):
    model=r"^[a-zA-Z0-9]{6,18}$"
    match=re.match(model,password)
    
    if match:
        return True
    else:
        return False
password1 = "Abc!"
password2="abc12345678900000000000000"
password3="abc123"
print(judge(password1))
print(judge(password2))
print(judge(password3))