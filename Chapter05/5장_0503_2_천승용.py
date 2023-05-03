'''
작성일 : 2023년 5월 03일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 하나의 숫자를 입력받아 팩토리얼을 구하는 프로그램을 작성하시오.
'''
# 1. 변수를 입력받는다.
# 2. total = 1
# 3. 입력받은 수부터
# 4. 입력받은 수가 1이 될때 까지 반복한다.
#   1) total = total * num
#   2) num = num -1

num = int(input("정수를 입력하시오. : "))
total = 1
num_print = num
while num >= 1 :
    total = total * num
    num = num - 1
print("{}!(팩토리얼)은 {}입니다.".format(num_print, total))

for i in range(num, 0 , -1):
    total = total * num
print("{}!(팩토리얼)은 {}입니다.".format(num_print, total))
