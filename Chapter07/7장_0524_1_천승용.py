'''
작성일 : 2023년 05월 24일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 7장 세트와 딕셔너리
        01. 세트
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
set1 = {'one','two','three'}
print("세트 set1 내용 : ", set1)

set2 = {1,2,3,4,5,4,3,2,1}
print("세트 set2 내용 : ", set2) # 중복된 내용은 지가 알아서 삭제함

set3 = {1,2,3,(1,2,3),4}
print("세트 set3 내용 : ", set3)

set4 = {1,2,3,(1,2,3),4,(2,2,2)}
print("세트 set4 내용 : ", set4)

# set5 = {1,2,3,[1,2,3],4}
# print("세트 set5 내용 : ", set5)  # 리스트는 세트에 포함 할 수 없다.
# 따라서 문자열, 튜플을 세트 자료형으로 사용 가능하지만 리스트는 안된다.

# 세트 메소드
# add(), remove(), discard(), pop(), copy(), clear()

# 추가
set6 = {1,2,3,4,5}
set6.add(6)
print("세트 set6 내용 : ", set6)

# set6에 1~10까지 내용을 추가하시오.

for i in range(1,11):
    set6.add(i)
print("세트 set6 내용(1~10 추가) : ", set6)

# 삭제 remove(), discard(), pop()
set6.discard(1) # 내용 중 에 1을 삭제
set6.remove(3)  # 내용 중 에 3을 삭제
print("세트 set6 내용(1, 3 삭제) : ", set6)

set6.discard(11)    # 내용 중 없는 11을 삭제
# set6.remove(11)   # 내용 중 없는 11을 삭제 시 오류 발생 remove는 없는 내용은 삭제가 불가능하다.
print("세트 set6 내용(11 삭제) : ", set6)

set6.pop()  # 첫번째 요소를 삭제 한다.
print("세트 set6 내용() : ", set6)

# 복사
set7 = {11,22,33,44,55}
set8 = set7.copy()
print("세트 set7 내용 : ", set7)
print("세트 set8 내용(set7 복사) : ", set8)

# 지우기
set7.clear()
print("세트 set7 내용 : ", set7) # set는 안에 아무것도 없으면 출력햇을때 set()라고 뜸
print("세트 set8 내용 : ", set8)

# 세트 연산 메소드
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("세트 set1 내용 : ", set1)
print("세트 set2 내용 : ", set2)
print("set1과 set2의 합집합 : ", set1 | set2)   # | 이거는 합집합
print("set1과 set2의 교집합 : ", set1 & set2)   # & 이거는 교집합
print("set1과 set2의 차집합 : ", set1 - set2)   # - 이거는 차집합
