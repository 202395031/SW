'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 8세 이상이면서 키가 120cm 이상인 어린이는 "고속 롤러코스터 입장 가능",
        8세 이상이면서 키가 120cm 미만인 어린이는 "저속 롤로코스터 입장 가능",
        나이가 8세 미만인 어린이는 "입장할 수 없습니다."를 출력하는 프로그램을 작성하시오.
'''

# 1. 변수를 입력 받는다.
age = int(input("나이를 입력하시오. : "))
h = int(input("키를 입력하시오. : "))

# 2. 만약 나이가 8세이상일때
if age >= 8:

#   1.키가 120이상이면
#       1)"고속 롤러코스터 입장가능합니다." 출력
    if h >= 120:
        print("고속 롤러코스터 입장 가능합니다.")

#   2.아니면
#       1)"저속 롤러코스터 입장가능합니다." 출력
    else :
        print("저속 롤러코스터 입장 가능합니다.")
        
# 3. 아니면
#   1)입장할 수 없습니다. 출력   
else :
    print("입장할 수 없습니다.")

   
if age >= 8 and h >= 120 :
    print("고속 롤러코스터 입장 가능합니다.")
elif age < 8 :
    print("입장할 수 없습니다.")
else : 
    print("저속 롤러코스터 입장 가능합니다.")