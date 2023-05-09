'''
작성일 : 2023년 5월 03일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 1부터 1000까지의 정수 중 사용자가 입력한 숫자의배수만을 더하여 출력하는 프로그램을 작성하시오.
'''
# 1. 정수를 입력 받는다. (배수 = input_num)
# 2. 입력 받은 정수가 1부터 (num)
# 3. 합계는 0
# 4. 수가 10까지 반복하면서 (num)
#   a 수를 1증가시킨다.
#   1) 만약에 수가 입력받은 수의 배수이면 :
#       ① 합계를 계산한다.
#       b 수를 1증가시킨다.
#   2) 아니면(배수가 아니면)
#       b 수를 1증가시킨다.
#       ① 다시 처음으로 돌아간다.
#   e 수를 1증가시킨다.
# 5. 합계를 출력한다.
input_num = int(input("정수를 입력하시오. : "))
sum = 0
num = 0
while num <= 10:
    num = num + 1
    if num % input_num == 0:
        sum = sum + num
    else :
        continue
print("{}의 배수의 합 : {}".format(input_num,sum))

print("================================")

sum = 0
num = 1
while num <= 10:
    if num % input_num == 0:
        sum = sum + num
        num = num + 1
    else :
        num = num + 1
        continue
print("{}의 배수의 합 : {}".format(input_num,sum))

print("=for 반복문 ===============================")

sum = 0
 
for num in range(1, 11):
    if num % input_num == 0:
        sum = sum + num
    else :
        continue
print("{}의 배수의 합 : {}".format(input_num,sum))
