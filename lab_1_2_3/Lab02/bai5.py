n = int(input("Nhập số phần tử trong list: "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("List vừa nhập là: ", lst)
answer = []
for i in lst:
    if i % 5 == 0:
        answer.append(i)
if len(answer) == 0:
        answer = [0]
print("Các số chia hết cho 5 là: ", answer)