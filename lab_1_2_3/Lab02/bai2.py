n = int(input("Nhập số phần tử của list: "))
lst = []
for i in range(n):
    lst.append(int(input()))
sum = 0
for i in lst:
    sum += i
print ("Tổng tất cả các số trong list là: " ,sum)
