'''
작성일 : 2023년 05월 31일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 8장 파일 입출력
'''
# writelines() 메소드
list1 = ['월요일\n','화요일\n','수요일\n','목요일\n','금요일\n','토요일\n','일요일\n']

# for 문으로 읽기
print("== for 문을 이용하여 읽기 ==")
with open("Linetest.txt", "r") as f :
    for line in f:
        print(line)