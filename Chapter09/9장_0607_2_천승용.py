'''
파일 저장 명 : 8장_0607_2_김경현.py

작성일 : 2023년 6월 7일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 9장 함수와 모듈
'''
import random   # 랜덤

def make_question() :   # 문제를 입력받음
    num1 = random.randint(1, 40)    # num1에 1부터 40까지 랜덤 숫자 입력
    num2 = random.randint(1, 20)    # num2에 1부터 20까지 랜덤 숫자 입력
    op = random.randint(1,3)        # op에 +, -, * 중 랜덤 출력
    
    que = str(num1) # num1 문자열 변환
    
    if op == 1:     # 문자 연산자와 연결
        que = que + '+'
    if op == 2:
            que = que + '-'
    if op == 3:
        que = que + '*'
        
    que = que + str(num2)
        
    return que
    
R_ans = 0   # 정답
W_ans = 0   # 오답

for i in range(5) : # i에 5번 반복
    que = make_question()   
    print(que, end='')
    
    result = int(input('=')) # '=' 출력
    
    if eval(que) == result :
        print('정답입니다.')    # 정답입니다 출력
        R_ans += 1             # R_ans에 1씩 추가
    else :
        print('오답입니다.')    # 오답입니다 출력
        W_ans += 1             # W_ans에 1씩 추가
        
print('정답 : ', R_ans, '오답 : ', W_ans)   # 정답은 R_ans 오답은 W_ans 출력

if W_ans == 5 : # 만약 5문제를 다 맞춘다면
    print('당신은 천재 입니다.') # 당신은 천재 입니다 출력
        
    


