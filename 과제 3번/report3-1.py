'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 1부터 1000 사이의 소수를 구하여 리스트에 저장한 후, 소수와 소수의 개수를 출력하는 프로그램을 작성하시오.
'''
# 1. 리스트 하나를 만든다.
# 2. nameerror 때문에 num = 0 지정
# 2. 1000번 반복 하면서
# 3. for 변수로 나누어 나머지가 0이면
        # (1) 멈춘다
# 4. for 변수와 num이 같으면
    # 리스트에 저장하고
# 5. 아니면 
    # 계속 반복
# 리스트 출력
decimal = []
num = 0
for i in range(1, 1001):
    for num in range(2, i+1):
        if i % num == 0:
            break
    if num == i :
        decimal.append(i)
print(decimal)
print("소수의 개수는 : ", len(decimal))
 