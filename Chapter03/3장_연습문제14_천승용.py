'''
작성일 : 2023년 3월 29일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 연습문제 14
        5과목의 점수를 입력 받아 총점과 
        평균을 구하는 프로그램을 작성하시오.
'''
kor = int(input("국어 점수를 입력하시오 : "))
math = int(input("수학 점수를 입력하시오 : "))
soc = int(input("사회 점수를 입력하시오 : "))
sci = int(input("과학 점수를 입력하시오 : "))
eng = int(input("영어 점수를 입력하시오 : "))

total = kor + math + soc + sci + eng
avg = total / 5

print("국어 : {}점 수학 : {}점 사회 : {}점 과학 : {}점 영어 :{}점".format(kor, math, soc, sci, eng))
print("총점은 {}점이고 평균은 {:.2f}점 입니다.".format(total, avg))
