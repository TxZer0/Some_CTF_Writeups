result = 0x3B9ACA00 + 16 * 0x499602D2

# Giới hạn trong phạm vi 32-bit
result = result % (2**32)

# Nếu giá trị lớn hơn 2^31, trừ đi 2^32 để chuyển đổi sang số nguyên âm
if result >= 2**31:
    result -= 2**32

print(result) 

