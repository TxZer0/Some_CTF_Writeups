import gdb

key = ""
chars = "1234567890abcdef"
gdb.execute("break strncmp@plt")
for i in range(100):
    for j in chars:
        # Tạo input
        run_cmd = f"run {key + j + 'a' * (99 - i)}"
        gdb.execute(run_cmd)

        # Lấy giá trị tại $rsi và $rdi
        s1 = gdb.execute("x/s $rsi", to_string=True)
        s2 = gdb.execute("x/s $rdi", to_string=True)

        # So sánh các ký tự tại vị trí 17 + i 
        if s1[17 + i] == s2[17 + i]:
            key += j
            print(f"Khóa hiện tại: {key}")
            break
print(f"Khóa: {key}")



