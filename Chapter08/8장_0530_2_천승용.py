'''
작성일 : 2023년 05월 30일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 8장 파일 입출력
'''
# open() 함수로 파일 쓰기 - 추가모드 a
f = open("text.txt", "a") # 파일 오픈(추가)

f.write("추가 메세지입니다. \n") 

f.close # 파일 종료