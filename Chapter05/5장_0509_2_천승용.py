'''
작성일 : 2023년 5월 09일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 5과목의 성적을 입력받아 각 과목의 점수, 총점, 평균을 출력하는 프로그램을 반복문을 이용하여 작성하시오.
'''
# 1. sum = 0
# 2. num = 1
# 3. 1부터 
# 4. 5가 될때까지
#   1) 변수를 입력받는다.
#   2) 만약 입력 받은 변수가 0 ~ 100사이이면    
#       (1)sum = sum + input_num
#       (2)num = num + 1
#   3) 아니면
#       (1)유효한 성적이 아닙니다 출력
#       (2)continue
sum = 0 
num = 1
while num <= 5 :
    input_num = int(input("{}번째 성적 입력 : ".format(num)))
    if 0 <= input_num <= 100:
        print("{} 번째 성적 : {}".format(num, input_num))
        sum = sum + input_num
        num = num + 1
    else:
        print("유효한 성적이 아닙니다.")
        continue
print("총점은 : {}".format(sum))
print("평균은 : {:.2f}".format(sum/5))