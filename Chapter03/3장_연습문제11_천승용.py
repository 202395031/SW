'''
작성일 : 2023년 3월 29일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 연습문제 11
        반지름이 23인 원의 넓이를 구하시오.
'''
# 1. 반지름 23을 r변수에 저장한다.
r = 23

# 2. 원주율 3.14를 pi변수에 저장한다.
pi = 3.14

# 3. 원의 넓이를 계산한다.
#    원의 넓이를 계산하여 area 변수에 저장한다.
area = r * r * pi # area - (r ** 2) * pi

# 4.원의 넓이를 출력한다.
print("반지름이 {}인 원의 넓이는 {}입니다.".format(r, area))