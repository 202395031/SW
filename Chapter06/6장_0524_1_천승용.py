'''
작성일 : 2023년 05월 23일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 6장 시퀸스 자료형
        04. 리스트
'''
#튜플 생성
tuple1 = () # 빈 튜플 생성.
tuple2 = ('a',) # 원소가 하나여도 (,)쉼표는 필수
tuple3 = ('a', 'b', 'c')

color = ("red",'orange','white','yellow','green','blue','white')
print("color 내용 : ", color)
print("color의 길이 : ", len(color))
print("white 개수 : ", color.count('white'))
print("green의 위치 : ", color.index('green'))

# 실습 예제 6-7
# 2개의 튜플을 하나의 리스트로 만들기
fruit = ('수박', '딸기', '용과', '샤인머스켓', '망고')
price = (12000, 5000, 8000, 15000, 5500)

# 결과 : [사과, 2000, 배, 4500, ....]
fp_list = []    # 2개의 튜플 내용이 저장 될 리스트 생성.
# fp_tuple = () # 2개의 튜플 내용이 저장 될 튜플 생성.

for i in range(len(fruit)): # range(len(리스트 or 튜플 or 딕셔너리 or 세트)) 는 리스트 등의 안에 있는 내용의 수를 range의 범위로 함
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    # fp_tuple.append(fruit[i]) # 튜플은 변경이 안됨. 추가 안됨. 애초에 append가 안된다.
    
print("과일 목록 : ", fruit)
print("가격 목록 : ", price)
print("과일의 가격 리스트 : ", fp_list)
