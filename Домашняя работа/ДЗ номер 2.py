# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определи, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
# Задание из темы цикла While

a = int(input())
k = 1
x = []
max = -1234
while a != 0:
    x.append(a)
    a = int(input())
for s in range(len(x)-1):
    x[s] = int(x[s])
    x[s+1] = int(x[s+1])
    if x[s] == x[s+1]:
        k = k+1
        if k > max:
            max = k
    else:
        k = 0
        if k > max:
            max = k
print(max)