n = int(input("nhập số phần tử trong list: "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("List vừa nhập là: ",lst)
answer = []
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        answer.append(lst[i])

print("Các số lẻ trong List là: ",answer)

