'''
작성일 : 2023년 05월 24일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 7장 세트와 딕셔너리
        01. 세트
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
# 실습 예제 7-1
# 랜덤으로 1~100 사이의 값을 10개 생성한 세트 2개를 만들고,
# 합집합, 교집합, 차집합을 출력하시오.
# [알고리즘]
# 1. 비어있는 세트 2개 만들기
# 2. 랜덤으로 2개의 세트에 각각 10개의 값 저장.
#    반복하면서 10개의 값 저장
#       1) 값 저장(추가)
# 3. 2개의 세트 값 출력
#   합집합, 교집합, 차집합 출력
import random

num1 = set()    # set() 함수로 비어있는 세트 생성
num2 = set()

for i in range(10):
    num1.add(random.randint(1,10))
    num2.add(random.randint(1,10))
print("세트 num1 : ", num1)
print("세트 num2 : ", num2)
print("num1과 num2의 합집합 : ", num1 | num2)
print("num1과 num2의 교집합 : ", num1 & num2)
print("num1과 num2의 차집합 : ", num1 - num2)