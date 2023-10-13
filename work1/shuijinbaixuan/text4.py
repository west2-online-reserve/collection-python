input_string = input('')
if 'ol' in input_string:
     modified_string = input_string.replace('ol', 'fzu')

else:
    
    modified_string = input_string

reversed_string = modified_string[::-1]
print("结果字符串:", reversed_string)
