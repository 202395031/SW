'''
작성일 : 2023년 05월 31일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 8장 파일 입출력
'''
# print() 함수로 파일에 저장. 매개변수 file의 값으로 파일 객체에 저장.
with open("ptext.txt", "w") as f :
    print("컴퓨터공학부", file=f)
    print("202395031", file=f)  # 다음 위치에 쓰기(파일에 출력)
    print("천승용", file=f)
    
# f.open("ptext.txt", "w")
# print("컴퓨터공학부", file=f)
# print("202395031", file=f)  # 다음 위치에 쓰기(파일에 출력)
# print("천승용", file=f)
# f.close()