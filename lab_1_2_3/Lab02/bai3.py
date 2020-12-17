n = int(input("Nhập số phần tử của List: "))
lst = []
for i in range(n):
    lst.append(int(input()))

print("Mảng trước khi sắp xếp: ",lst)


for i in range(len(lst)):
    for j in range(i):
        if lst[i] < lst[j]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
print("Mảng sau khi sắp xếp: ",lst)
    

