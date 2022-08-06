n = int(input())
memory = [0]*(n+1)


for i in range(2,n+1):
    memory[i] = memory[i-1] + 1
    if i%2 == 0: 
        memory[i] = min(memory[i],memory[i//2] + 1)
    if i%3 == 0: 
        memory[i] = min(memory[i],memory[i//3] + 1)

i = n
valList = [i]

while True:
    if i == 1:
        break
    val = i-1
    if i%2 == 0:
        if memory[i//2] < memory[val]: val = i//2
    if i%3 == 0:
        if memory[i//3] < memory[val]: val = i//3
    i = val
    valList.append(i)

print(memory[n])
for val in valList:
    print(val,end=' ')
