n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr_cum,summ = [0],0
for i in arr:
    summ += i
    arr_cum.append(summ)

'''
아래 방식으로 코드를 작성하면 
array를 인덱싱하는 과정에서 시간 초과가 발생한다
'''

# arr_cum = [0]*(n+1)
# for i in range(n):
#     arr_cum[i+1] = arr_cum[i] + arr[i]

for _ in range(m):
    s,e = map(int,input().split())
    print(arr_cum[e]-arr_cum[s-1])