A,B,C,D,E,F = map(int,input().split()) #map을 사용하는 이유는 글이나 숫자가 한줄로 되어있는걸 한번에 받아오기위해서 사용 

for x in (-10000, 10001):
    for Y in (-10000, 10001):
        if A*x + B*Y == C:
            if D*x + E*Y == F:
                 print(x,Y) # 위의 if 문 두개를 통과한 x,y 값을 찍어준다 
                 break 
