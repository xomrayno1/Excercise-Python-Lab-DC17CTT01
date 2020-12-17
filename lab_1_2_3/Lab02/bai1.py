n = int(input("Nhập số phần tử của list: "))
lst = []
for i in range(n):
    lst.append(int(input()))
min_value = lst[0]
for i in lst:
    if i < min_value:
        min_value = i
print("Sô nhỏ nhất trong list là:  ",  min_value)