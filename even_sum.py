# 2 + 4 + ... + 100 = ?
even_sum = 0
for n in range (2, 101, 2):   # 等差級數
    even_sum += n
print ( even_sum )

# even_sum = 0 
# for n in range (1, 101):
#     if n % 2 == 0:           # 針對偶數加
#         even_sum += n
# print (even_sum)