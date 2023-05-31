'''
작성일 : 2023년 05월 31일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 8장 파일 입출력
'''
# 5명의 학생 성적 저장 파일 만들기 실습 예제 8-2
# write() 메소드와 readline() 메소드를 이용하여
# 학생 이름과 3과목의 성적을 리스트로 생성하여 파일에 저장.
# 입력 예 ) 홍길동 100 95 77
print("== 학생 정보 읽어오기 ==")
with open("student.txt", "r") as f :
    while True :
        std = f.readline()
        print(std, end='')
        
        if std == '':
            break
print()
print("== 학생 정보 읽어오기2 ==")
with open("student.txt", "r") as f :
    while True :
        std = f.readline()
        studentList = std.split()   #split() 는 빈칸을 기준ㅇ로 리스트 객체로 반환시킴
        print(studentList)
        
        if std == '':
            break
