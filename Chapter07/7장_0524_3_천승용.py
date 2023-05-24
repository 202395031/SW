'''
작성일 : 2023년 05월 24일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 7장 세트와 딕셔너리
        01. 세트
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
# 랜덤으로 로또 번호 알려주기
# 1. 로또 번호 저장 할 세트 만들기
# 2. 6번 반복하면서
#   1) 1~45 사이의 값을 세트 변수에 추가
# 3. 로또 번호 출력
import random

lotto = set()
# while 이게 조건이 만족할때 반복이니까 ==이게 아니라 != 이걸 써야한다 ==이걸 쓰려면 조건 앞에 not을 붙이면됨
while len(lotto) != 6 : 
    lotto.add(random.randint(1,45))
print("이번주 로또 번호 : ", lotto)

lotto2 = set()
while True :
    lotto2.add(random.randint(1,45))
    if len(lotto2) == 6:
        break
print("이번주 로또 번호 : ", lotto2)
