'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 1부터 100사이의 정수 난수 10개를 발생시켜 리스트에 저장하고, 각 숫자의 자리수를 키 값으로 하는 딕셔너리를 생성하는 프로그램을 작성하시오.
'''
# 1. import random
# 2. 빈 리스트를 만든다. 
# 3. 빈 딕셔너리를 만든다.
# 4. 1부터 100사이의 정수 난수를 리스트에 저장한다. (10 반복해서)
# 5. num 리스트 개수 만큼 반복
#   1) 만약 i - 10을 했을때 0보다 작으면
#       (1)리스트1에 저장
#   1) 만약 i - 100을 했을때 0보다 작으면
#       (1)리스트 2에 저장
#   1) 아니면
#       (1)리스트 3에 저장
# 6. 리스트 1,2,3을 딕셔너리 key 1,2,3 에 추가
# 7. 딕셔너리 출력
import random
num_dict = {}
num_list = []
num1 = []
num2 = []
num3 = []
for i in range(10):
    num_list.append(random.randint(1,100))
print("생성된 리스트 : ", num_list)
for j in num_list :
    if j - 10 < 0 :
        num1.append(j)
    elif j - 99 <= 0 :
        num2.append(j)
    else :
        num3.append(j)
num_dict[1] = num1
num_dict[2] = num2
num_dict[3] = num3
print("생성된 딕셔너리 : ", num_dict)