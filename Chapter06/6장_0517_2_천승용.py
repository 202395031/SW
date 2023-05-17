'''
작성일 : 2023년 5월 17일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 6장 시퀀스 자료형
       03. 문자열
'''
# 1. 문자열 생성
name = '천승용'
name2 = '''
천
승
용''' # ''' 이거는 문자열을 여러줄로 생성 할 수 있음
print("name : ", name)
print("name2 : ", name2)

# 빈 문자열 생성
text1 = ''
print("text1의 길이 : ", len(text1))
text2 = str()
print("text2의 길이 : ", len(text2))

# 정수를 문자열로 생성
text3 = str(1234)
print("text3 : ", text3)
print("text3의 자료형 : ", type(text3))

# 리스트를 문자열로 생성
text4 = str([1,2,3]) # 이렇게 만들면 리스트 자체가 문자열이됨
print("text4의 자료형 : ", type(text4))
# 리스트 자체를 문자열로 인식 하여 '[' 출력됨. 튜플도 똑같음
print("text4dml 0번지 값 : ", text4[0])

# 2. 문자열 메소드
# 대소문자 변환
text1 = 'i like python'
print("text1 내용의 첫 문자를 대문자로 변환 : ", text1.capitalize())
print("text1 내용의 모든 단언의 첫 문자를 대문자로 변환 : ", text1.title())
text2 = text1.upper() # 대문자 변환
print('text1의 내용의 모든 단어를 대문자로 변환 : ', text2)
text3 = text2.lower() # 소문자 변환
print('text2의 내용의 모든 단어를 소문자로 변환 : ', text3)

# 문자열 정렬
print(text3.center(30, '*'))

# 문자 찾기
print("text3에 'a'가 몇 개 있나요? : ", text3.count('a'))
print("text3에 'i'가 몇 개 있나요? : ", text3.count('i'))
print("text3의 인덱스 5부터 10까지 중에서 'i'가 몇 개 있나요? : ", text3.count('a', 5, 10))
print("text3의 인덱스 5이후에 'o'가 몇 개 있나요? : ", text3.count('o', 5))

# 문자열 내의 위치 - index(), find(), startswith(), endswith()
print("text3에 'k'의 인덱스 위치는 ? : ", text3.index('k'))
print("text3에 'k'의 인덱스 위치는 ? : ", text3.find('k'))

# 시작 지점 부터 찾아줌 
print("text3에 'python'의 인덱스 위치는 ? : ", text3.index('python'))
print("text3에 'python'의 인덱스 위치는 ? : ", text3.find('python'))

# 없으면 오류
# print("text3에 'python1'의 인덱스 위치는 ? : ", text3.index('python1'))
# 없으면 -1을 반환(출력) 시킨다.
print("text3에 'python1'의 인덱스 위치는 ? : ", text3.find('python1'))

print("text3가 'i like' 로 시작하는가 ? : ", text3.startswith('i like'))
print("text3이 'abc'로 끝나는가? : ", text3.endswith('abc'))

# 문자열 결합 - join()
# 리스트 생성
list1 = ['1', '2', '3', '4', '5']
print("list1 내용에 '-' 기호를 결합 : ", '-'.join(list1))

list2 = [1,2,3,4,5]
# 오류 발생. 정수와 문자는 연결이 안됨. 
# join()의 대상은 반드시 문자열이어야 함.
# print("list2 내용에 '-' 기호를 결합 : ", '-'.join(list2))

# 딕셔너리 생성 - 키:값(key:value)
dict1 = {'apple':'사과', 'grape':'포도', 'peach':'복숭아'}
# 키(key)에 해당하는 문자열에 join
print("dict1 내용에 '-' 기호를 결합 : ", '-'.join(dict1))

# 문자열 분리 - split() 원하는 단어나 기호등 다른거로도 분리됨
text1 = 'I like Python Language'
# 문자열을 스페이스로 분리하여 리스트로 반환
list1 = text1.split()   
print("text1 내용을 스페이스로 분리하여 list 생성 : ", list1)

text2 = 'I-like-Python-Language'
print("text1 내용을 '-'를 기준으로 분리하여 list로 반환 : ", text2.split('-'))
