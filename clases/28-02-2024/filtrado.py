

a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])

print(filtered_array)

con_filter = [i for i in a if i >= 1000]
print(con_filter)
