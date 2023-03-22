class Row:
    def __init__(self,rownum,before=-1,after=-1):
        self.rownum = rownum
        self.before = before
        self.after = after

def solution(n, k, cmd):
    current,deleted = [Row(rownum=0,after=1)],[]
    for i in range(1,n-1):
        current.append(Row(rownum=i,before=i-1,after=i+1))
    current.append(Row(rownum=n-1,before=n-2))
    answer = ['O']*n
    
    for C in cmd:
        if C == 'Z':
            rownum = deleted.pop()
            answer[rownum] = 'O'
            row = current[rownum]
            before,after = row.before, row.after
                
            if before>=0:
                current[before].after = rownum
            if after>=0:
                current[after].before = rownum
            
        elif C == 'C':
            answer[k] = 'X'
            row = current[k]
            deleted.append(k) #삭제하기
            
            before,after = row.before,row.after
            if before >= 0:
                current[before].after = after
            if after >= 0:
                current[after].before = before
                
            if after == -1: # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
                k = before
            else:
                k = after
        else:
            C,X = C.split(' ')
            X = int(X)
            if C == 'U':
                row = current[k]
                k = row.before
                for _ in range(X-1):
                    k = current[k].before
            elif C == 'D':
                row = current[k]
                k = row.after
                for _ in range(X-1):
                    k = current[k].after
                
    answer = ''.join(answer)
    
    return answer