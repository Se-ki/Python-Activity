num_iter = int(input("Enter a number: "))

num_list = []

for i in range(num_iter):
    for j in range(0, 5):
        j+=1
        num_list.append(j)
print(num_list)