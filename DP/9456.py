
dy = [1,2,2]
dx = {0:[1,-1],1:[1,-1],2:[0,0]}

# def solution(x,y):


if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    T = int(stdin.readline())
    for _ in range(1):
        n = int(stdin.readline())
        st = [list(map(int,stdin.readline().split())) for _ in range(2)]
        st[0].append(0)
        