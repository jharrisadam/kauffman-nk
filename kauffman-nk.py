def compare(a, b):
    if a < b:
        return 1
    elif a > b:
        return 2
    else:
        return 0

def fitness(n, k):
    if k == 0:
        print(sum(n))
    else:
        total = 0
        test = n + n
        for i in range(0, len(n)):
            for j in range(1, (k+1)):
                temp = compare(n[i], test[i+j])
                total += temp
        print(total)

n = input("enter a list consisting only of 0s and 1s: ")
k = int(input("Please enter an integer between 0 and n-1: "))

fitness(n, k)
