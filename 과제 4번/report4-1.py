'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 사용자로부터 하나의 자연수를 입력받아 각각 2, 3, 7의 배수를 세트로 출력하고, 
2,3,7, 모두의 배수를 세트로 출력하는 프로그램을 작성하시오.
'''
# 1. 변수를 입력받는다.
# 2. 리스트 지정(4개)
# 3.100번 반복하면서
#   1)만약 i 를 2로 나눴을때 나머지가 0이면
#       (1)첫번재 리스트에 저장
#   2)만약 i 를 3로 나눴을때 나머지가 0이면
#       (1)두번째 리스트에 저장
#   3)만약 i 를 7로 나눴을때 나머지가 0이면
#       (1)세번째 리스트에 저장
#   4)만약 i 를 2 나 3 이나 7로 나눴을때 나머지가 0이면
#       (1)네번째 리스트에 저장
# 4. 4개의 리스트를 세트로 변형
# 4. 4개의 세트 출력
multiple1 = []
multiple2 = []
multiple3 = []
multiple4 = []
num = int(input("숫자를 입력하시오 : "))
multiple = {}
for i in range(1, num+1):
    if i % 2 == 0 :
        multiple1.append(i)
        multiple4.append(i)
    if i % 3 == 0 :
        multiple2.append(i)
        multiple4.append(i)
    if i % 7 == 0 :
        multiple3.append(i)
        multiple4.append(i)
multiple_set_1 = set(multiple1)
multiple_set_2 = set(multiple2)
multiple_set_3 = set(multiple3)
multiple_set_4 = set(multiple4)

print("2의 배수 : ", multiple_set_1)
print("3의 배수 : ", multiple_set_2)
print("7의 배수 : ", multiple_set_3)
print("2,3,7의 배수 : ", multiple_set_4)