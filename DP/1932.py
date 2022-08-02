def solution(l):
    if l < 0 :
        return
    solution(l-1)
    for i in range(1,len(dic[l+1])-1):
        dic[l+1][i] = max(dic[l+1][i]+dic[l][i],dic[l+1][i]+dic[l][i-1])

if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    n = int(stdin.readline())
    dic = dict()

    for i in range(n):
        dic[i] = list(map(int,stdin.readline().split()))
        dic[i].insert(0,0)
        dic[i].append(0)

    solution(n-2)
    print(max(dic[n-1]))

