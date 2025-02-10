파이썬 기본 내용 

map = map(int,input().sprint()) 입력 받은값을 하나씩 쪼개서 int로 변겨해서 변수값의 각각 저장

파이썬에서 String str롤 작성

배열
list = [0,0,0,0,0] 이런형식으로 표현

배열로 표현 한는방법

list(map(int,input ()sprint()))  이렇게 하면 위의 배열에 예쁘게 담긴다

반복문 (for문) for _ in range();

ex) 100번 반복 (0~99) 까지 반복
for _ in range(100); 이렇게 하면 100번 반복한다
print(hi)

ex) 변수명
for number in range(100); // 이렇게 하면 number에 있는값을 100번찍는다
print(number);

ex) 특정 부분까지 반복 (95~99) 까지 반복
for number in range(95,100); // 이렇게 하면 number에 있는값을 100번찍는다
print(number);

ex) 넘버가 10보다 작으면 반복 ,넘버가 10이거나 ,10을 초과하면 끝낸다
number =0
while number<10:
print(number)
number+number +1