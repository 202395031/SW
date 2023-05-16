'''
작성일 : 2023년 5월 16일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 10개의 정수를 입력 ㅂ다아 합을 구하는 프로그램을 작성하시오.
단, 짝수 번재에 입력되는 숫자는 양수를 음수로, 음수는 양수로 바꾸어 합을 구하시오.
'''
# 1. count = 1
# 2. sum = 0
# 3. 1에서
# 4. 10이 될때까지
#   1) 변수를 입력받는다.
#   2) 만약 count가 짝수라면
#       (1) 변수가 양수 일경우
#           1. 양수를 음수로 변환
#       (2) 변수가 음수 일경우
#           1. 음수를 양수로 변환
#   3) sum = sum + 변수
#   4) count = count + 1
# 5. 출력

count = 1
sum = 0
while count <= 10: # 밑에 변수 입력받을때 + 는 연결 연산자
    num = int(input(str(count) + " 번째 정수를 입력하세요 : "))
    if count % 2 == 0:
        if num > 0 :
            num = num * (-1)
        else :
            num = num * (-1)
    count = count + 1
    sum = sum + num
print("10개 정수의 총 합은 {} 입니다".format(sum))

print("==================================")

count = 1
sum = 0
while True : #True는 무한 반복, 이걸 멈추기 위해 break 씀
    num = int(input("{} 번째 정수를 입력하세요 : ".format(count)))
    if count % 2 == 0 :
        num = -num
    # 결합 연산자 += -= /= %= 등이 있다. += 으로 예를 들면 count += 1 은 count = count + 1 과 같다.
    sum += num
    count += 1
    
    if count > 10 :
        break
print("10개 정수의 총 합은 {} 입니다".format(sum))
