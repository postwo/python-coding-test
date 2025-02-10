# A가 정답으로 생각할 수 있는 모든 수를 넣어보기

# 그리고 B가 도전한 내용에 맞는지 확인하기 


n = int(input()) # 4번의 기회

hint = [list(map(int,input().split())) for _ in range(4)]

# [123,1,1], [356,1,0] ....

# 정답 후보를 저장할 리스트
answer = 0

# 숫자를 생성하여 힌트와 비교하는 부분
for a in range(1, 10):  # 100의 자리수
    for b in range(10):  # 10의 자리수
        for c in range(10):  # 1의 자리수

            # 각 자리 수가 중복되지 않도록 확인
            if a == b or b == c or c == a:
                continue

            # 모든 힌트와 현재 숫자를 비교하여 힌트 조건을 만족하는지 확인
            cnt = 0
            for arr in hint:
                number = arr[0]  # 예: 123
                ball = arr[1]  # 볼 개수
                strike = arr[2]  # 스트라이크 개수

                # 숫자를 각 자리수로 분리 (예: 123 → n1 = 1, n2 = 2, n3 = 3)
                n1 = number // 100  # 100의 자리
                n2 = (number // 10) % 10  # 10의 자리
                n3 = number % 10  # 1의 자리

                # 스트라이크와 볼 개수 측정
                ball_count = 0
                strike_count = 0

                # 스트라이크 확인 (같은 위치에 같은 숫자)
                if a == n1:
                    strike_count += 1
                if b == n2:
                    strike_count += 1
                if c == n3:
                    strike_count += 1

                # 볼 확인 (다른 위치에 존재하는 숫자)
                if a == n2 or a == n3:
                    ball_count += 1
                if b == n1 or b == n3:
                    ball_count += 1
                if c == n1 or c == n2:
                    ball_count += 1

                # 힌트와 현재 숫자의 스트라이크 & 볼 개수가 일치하는지 확인
                if ball == ball_count and strike == strike_count:
                    cnt += 1

            # 모든 힌트를 만족하면 정답 후보에 추가
            if cnt == n:
                answer += 1

print(answer)
    
