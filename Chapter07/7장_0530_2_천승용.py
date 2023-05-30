'''
작성일 : 2023년 05월 30일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 7장 세트와 딕셔너리
        02. 딕셔너리

예제 7-3
5명의 학번과 이름을 입력하여 딕셔너리에 저장한다.
키 : 학번, 값 : 이름
학번을 입력 받아 해당 학생의 이름을 출력한다.
입력 받은 학번이 없으면 "입력한 학생이 존재하지 않습니다." 출력한다
학번을 입력할때 사용자가 0을 입력하면 프로그램을 종료한다.
'''
# 1. 빈 딕셔너리 생성
# 2. 5번 반복하면서
#   1) 학번 입력받기
#   2) 이름 입력받기
#   3) 딕셔너리에 추가
# 3. 저장된 학생 정보를 출력한다.
# 4. 학번에 0이 입력될때 까지 (무한반복 하면서)
#   1) 검색할 학생의 학번을 입력받는다.
#   2) 만약 검색할 학생의 이름이 딕셔너리에 없으면
#       ① 입력한 학생이 존재하지 않습니다 출력
#   3) 아니면
#       ① 검색한 학생의 이름 출력
student = {}
for i in range(5) :
    id = int(input(str(i+1)+"번째 학번을 입력하시오. : "))
    name = input(str(i+1)+"번째 학생의 이름을 입력하시오. : ")
    student[id] = name
print("학생 명부 완성")
print(student)

while id != 0 :
    id = int(input("검색할 학번을 입력하시오.(종료:0) : "))
    if id == 0:
        print("프로그램을 종료합니다.")
    elif id in student :
        print("== 검색할 학생 정보 ==")
        print("학번 : {} 이름 : {}".format(id, student.get(id)))
        print("학번 : {} 이름 : {}".format(id, student[id]))
    else :
        print("검색한 학생이 존재하지 않습니다.")
        
while True : 
    id = int(input("검색을 원하는 학생 학번 입력(종료:0) : "))
    if id == 0:
        print("프로그램을 종료합니다.")
        break
    else : 
        if id in student :
            print("== 검색할 학생 정보 ==")
            print("학번 : {} 이름 : {}".format(id, student.get(id)))
            print("학번 : {} 이름 : {}".format(id, student[id]))
        else :
            print("검색한 학생이 존재하지 않습니다.")
            
   