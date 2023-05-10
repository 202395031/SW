'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 2단부터 9단까지 구구단을 출력하시오.
        단, 구구단의 결과가 짝수인 경우만 출력하시오. while 과 for 둘다 작성
'''
# for
# 1. 2부터 9가 될때 까지
#   1) == {} 단 == 출력
#   2) 1부터 9가 될때까지
#       (1) 만약 jul * kan % 2 == 0 이면
#           1. jul * kan = 값 출력

for jul in range(2, 10):
    print("== {} 단 ==".format(jul))
    for kan in range(1, 9):
        if jul * kan % 2 == 0:
            print("{} x {} = {}".format(jul, kan, jul*kan))


print("==============================")
# while
# 1. jul = 2
# 2. 2부터 
# 3. 9가 될때 까지
#   1) == {} 단 == 출력
#   2) kan = 1
#   3) 1부터 
#   4) 9가 될때까지
#       (1) 만약 jul * kan % 2 == 0 이면
#           1. jul * kan = 값 출력
#   4) kan = kan + 1
# 3. jul = jul + 1
jul = 2
while jul <= 9:
    print("== {} 단 ==".format(jul))    
    kan = 1
    while kan <= 9:
        if jul * kan % 2 == 0:
            print("{} x {} = {}".format(jul, kan, jul*kan))
        kan = kan + 1
    jul = jul + 1
