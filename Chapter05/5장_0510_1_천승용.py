'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 사용자로부터 하나의 정수를 입력 받아 다음과 같이 * 을 출력하는 프로그램을 작성하시오.
'''
 
# 1. 변수를 입력 받는다.
# 2. 1부터 입력받은 변수까지
#   1) for 안에 변수 까지
#       (1)* 출력 (end='')
#   2) 줄바꿈
num = int(input("정수를 입력하시오. : "))
for jul in range(num+1):
    for kan in range(jul):
        print("★", end=' ')
    print("")
    