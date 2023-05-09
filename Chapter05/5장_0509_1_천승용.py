'''
작성일 : 2023년 5월 09일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 정수를 입력 받아 입력 받은 수가 소수인지 아닌지 판단하는 프로그램을 작성하시오.
'''
# 1.정수를 입력받는다.
# 2. 3부터 입력 받은 수까지 반복하면서
    # 1) 만약 수를 입력 받은 수로 나누어 나머지가 0이면
        # (1) 멈춘다
# 3. 만약 입력 받은 수와 num이 같으면
    # 1) 소수입니다. 출력
# 4. 아니면 
    # 소수가 아닙니다. 출력
input_num = int(input("정수를 입력하시오. : "))

for num in range(2, input_num+1):
    if input_num % num == 0:
        break
if num == input_num :
    print("{}은 소수 입니다.".format(input_num))
else :
    print("{}은 소수가 아닙니다.".format(input_num))
 
