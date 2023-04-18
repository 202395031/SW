'''
작성일 : 2023년 4월 11일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 한 과목이 점수를 입력 받아 점수에 따라 학점을 부여하는 프로그램을 작성하시오.
'''
# 1. 정수를 입력받는다.
score = int(input("점수를 입력하시오. : "))

# 2. 점수가 90점이상 100점 이하일때
#   1) "A학점입니다." 출력
if score >= 90 and score <= 100 :
    print("{}점으로 A입니다.".format(score))

# 3. 점수가 80점이상 89점 이하일때
#   1) "B학점입니다." 출력
elif score >= 80 and score <= 89 :
    print("{}점으로 B입니다.".format(score))

# 4. 점수가 70점이상 79점 이하일때
#   1) "C학점입니다." 출력
elif score >= 70 and score <= 79 :
    print("{}점으로 C입니다.".format(score))

# 5. 점수가 60점이상 69점 이하일때
#   1) "D학점입니다." 출력
elif score >= 60 and score <= 69 :
    print("{}점으로 D입니다.".format(score))
    
# 6. 아니면
#   1) "F학점입니다." 출력
elif score >= 0 and score <= 59 :
    print("{}점으로 F입니다.".format(score))

# 7. 입력(100을 초과한 숫자, 0 미만의 숫자) 했을 경우
else :
    print("숫자를 잘못 입력하셨습니다.")