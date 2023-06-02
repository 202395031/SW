'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 1~100사이의 난수를 발생시켜 'num.txt' 파일을 생성하고, 생성된 'num.txt'파일을 읽어 각 학생의 평균을
'avg.txt.'파일에 출력하는 프로그램을 작성하시오. 
'''
# 1. import random
# 2. num.txt 를 w로 열고
    # 1). 5번 반복
    #   (1)5번반복
    #       1. 난수를 num.txt에 저장
    #   (2)띄어쓰기를 위해 ''이것도 txt파일에 저장
# 3. num.txt 읽기 모드로 열고
#   1) 5번 반복
#       (1) sum = 0
#       (2) list에 num.txt 텍스트 넣고
#       (3) list.split() 한걸 변수 avg에 저장
#       (4) avg를 len 한 만큼 반복
#           1. sum = sum + int(avg[i])
#       (5)학생평균 출력

import random

with open("num.txt", "w") as f :
    for i in range(5):
        for i in range(5):
            print(random.randint(1,100), end=' ', file=f)
        print("", file=f)
with open("num.txt", "r") as f :
    for i in range(5):
        sum = 0
        list = f.readline()
        avg = list.split()
        for i in range(len(avg)):
            sum = sum + int(avg[i])
        print("{}번째 학생의 평균 : {}".format(i+1, sum/5))
