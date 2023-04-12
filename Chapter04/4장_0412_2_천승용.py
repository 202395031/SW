'''
작성일 : 2023년 4월 11일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 두 개의 숫작를 입력 받아 두 숫자가 모두 짝수이면 "두 숫자가 모두 짝수입니다."를 출력하고,
    모두 홀수이면 "두 숫자가 모두 홀수입니다."를 출력하고
    그렇지 않으면 "짝수와 홀수가 섞여 있습니다."를 출력하는 프로그램을 작성하시오.
'''

# 1. 정수를 입력 받는다.
num1 = int(input("정수를 입력하시오. : "))
num2 = int(input("정수를 입력하시오. : "))

# 2. 만약 입력 받은 정수가 모두 짝수이면
#   1) "두 숫자가 모두 짝수입니다." 출력
if num1 % 2 == 0 and num2 % 2 == 0 :
    print("두 숫자가 모두 짝수입니다.")
    
# 3. 만약 입력 받은 정수가 모두 홀수이면
#   1) "두 숫자가 모두 홀수입니다." 출력
elif num1 % 2 != 0 and num2 % 2 != 0 :
    print("두 숫자가 모두 홀수입니다.")

# 4. 아니면
#   1) "짝수와 홀수가 섞여 있습니다." 출력
else:
    print("짝수와 홀수가 섞여 있습니다.")
