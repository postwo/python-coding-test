candy = int(input()) #6 개를 받을거다 

answer = 0
for A in range(0,candy+1): # 0~6개 +1을 해주는 이유는 0부터 돌기 떄문에 추가 
    for B in range(0,candy+1): # 0~6개
        for C in range(0,candy+1): # 0~6개
            if A+B+C == candy: # 입력 받은 사탕의 개수 만큼
                if A >= B+2: # a가 b보다 항상 2가크게 하기위해 +2를 추가 
                    if A !=0 and B != 0 and C !=0:
                        if C%2 == 0:
                            answer =+ 1 # 각 조건이 일치할때마다 +1씩 증가 
print(answer)