# 100만보다 작고 2이상의 약수를 가지고 있다면 , 틀린 비밀번호

TC =int(input()) #테스트 케이스 개수(TC)를 입력

for _ in range(TC):
    number = int(input()) #ex) 10000367000099 각 테스트 케이스마다 확인할 숫자를 입력

    for i in range(2, 1_000_001): # 100만 까지 돌려주기 위해 1을 더 넣어준거다 
       if number% i == 0: #2부터 100만까지 숫자를 나눠서 약수를 찾는다 = 100만 이하의 약수가 존재한다  # print(10 % 3)  # 10을 3으로 나눈 나머지 -> 1
         print("NO")
         break
       if i == 1_000_000 : # 100만 이하의 약수가 존재하지 않는다 
         print("YES")