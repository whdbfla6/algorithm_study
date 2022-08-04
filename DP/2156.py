def solution(n,val):
    for i in range(3,n+1):
        memory.append(max(memory[i-2],memory[i-3]+val[i-1])+val[i])
    

if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    n = int(stdin.readline())
    val = [int(stdin.readline()) for _ in range(n)]
    val.insert(0,0)
    
    memory = [val[0],val[1],val[1]+val[2]]
    solution(n,val)
    print(max(memory))



