#1-1
sum1 = 0
i = 0
while i <= 999:
    i += 1
    if i % 3 == 0:
        sum1 = sum1 + i

print(sum1)

#1-2
a = 11
while a > 0:
    a = a -1
    print('*' * a)

#1-3 
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
i = 0
sum2 = 0
while i < 9:
    i = i + 1
    if A[i] >= 50:
        sum2 = sum2 + A[i]

print(sum2)



#2-1
List = range(1, 101)
for k in List:
    print(k)

#2-2
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in A:
    sum = sum + i
   
print(sum / len(A))

#2-3
numbers = [1, 2, 3, 4, 5]
result= [n * 2 for n in numbers if n % 2 != 0]

print(result)