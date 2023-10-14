a = "hello,python"
b = "hi, python"
def is_in(full_str, sub_str):
   try:
        full_str.index(sub_str)
        return True
   except ValueError:
        return False

print(is_in(a, "lo"))
print(is_in(b, "lo"))
a = a.replace("lo","fzu")
print(a)
def string_reverse1(text = a):
    return text[::-1]
a = string_reverse1(a)
print(a)