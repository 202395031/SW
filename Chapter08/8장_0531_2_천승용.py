'''
작성일 : 2023년 05월 31일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 8장 파일 입출력
'''
# writelines() 메소드
list1 = ['월요일\n','화요일\n','수요일\n','목요일\n','금요일\n','토요일\n','일요일\n']

# readline() 메소드를 사용하여 무한 반복문으로 읽기
print("== 무한 반복문을 이용하여 읽기 ==")
with open("Linetest.txt", "r") as f :
    while True :
        line = f.readline()
        print(line, end='') # end 째 때문에 이게 \n 잇엇을때 출력결과가 붙어서 나옴 
        
        if line == '':
            break