def result():
    with open("rev_this", "r") as rev_file:
        rev_content = rev_file.read()
    
    flag_content = []
    for j in range(8, 23):
        if j % 2 == 0: 
            flag_content.append(chr(ord(rev_content[j]) - 5))
        else:  
            flag_content.append(chr(ord(rev_content[j]) + 2))  
    return ''.join(flag_content)

print("picoCTF{" + result()+"}")
