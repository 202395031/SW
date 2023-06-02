'''
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 'score.txt' 파일에 있는 3명의 학생의 국어, 수학, 영어 성적 자료를 읽어 학생별 총점과 평균을 구하고
국어, 수학, 영어 과목의 전체 평균을 구한 후에 화면과 'report.txt' 파일에 출력하는 프로그램을 작성하시오.
'''
# 0. score.txt를 만든다. (오류 방지용)
# 1. score.txt를 연다 읽기로
# 2. total 빈리스트를 만든다.
# 3. kor, math, eng 변수를 만들다. 값은 0으로
# 4. 무한 반복하면서
#   1)list에 score.txt의 내용을 담는다.
#   2)list의 내용을 이름과 숫자로 나눠서 저장한다.
#   3)만약 list 가 ""이거면 break
#   4)score_list만틈 반복하면서
#       (1) 만약 i 가 score_list[0]이면
#           1.score.list에서 변수 i 의 값을 삭제한다.
#   5)sum = 0
#   6)score_list만틈 반복하면서
#       (1)sum = sum + int(i)
#       (2)만약 변수 i 가 score_list[0]이면
#           1. 변수 kor = kor + int(i)를한다.
#       (2)아니고 만약 변수 i 가 score_list[1]이면
#           1. 변수 math = math + int(i)를한다.
#       (2)아니면
#           1. 변수  eng = eng + int(i)를한다.
#   7) 학생이름, 총점, 평균 순으로 출력한다.
# 5. kor 에 / 4를 한값을 출력한다.
# 5. math 에 / 4를 한값을 출력한다.
# 5. eng 에 / 4를 한값을 출력한다.
with open('score.txt', 'w') as f :
    list = [
"김말동 99 83 78\n",
"이말동 88 79 95\n",
"정말동 77 90 81\n",
"한말동 87 90 100\n"
]
    f.writelines(list)
with open('score.txt', 'r') as f :
    total = []
    kor = 0
    math = 0 
    eng = 0
    while True :
        list = f.readline()
        score_list = list.split() 
        name_list = list.split()
        if list == '':  
            break
        for i in score_list:
            if i == score_list[0]:
                score_list.remove(i)
        sum = 0
        for i in score_list:
            sum = sum + int(i)
            if i == score_list[0]:
                kor = kor + int(i)
            elif i == score_list[1]:
                math = math + int(i)
            else :
                eng = eng + int(i)
        print("{} 총점 : {} 평균 : {:.5f}".format(name_list[0], sum, sum/3))
    print("국어전체평균: {:.5f}".format(kor/4))
    print("수학전체평균: {:.5f}".format(math/4))
    print("영어전체평균: {:.5f}".format(eng/4))