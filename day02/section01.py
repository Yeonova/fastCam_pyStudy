# 파이썬 기초 코딩
# print 구문의 이해

# 기본출력 
print('Hello Python')
print("Hello Python")
print("""Hello Python""")
print('''Hello Python''')

print()

# -----Separator 옵션 사용------
print('T', 'E', 'S','T', sep='') #  sep= 공백을 문자열로 연결시켜주는 역할 
# 출력값 => TEST

print('2025', '02', '05', sep='-')
# 출력값 => 2025-02-05

print('hongwon5683','goggle.com', sep='@')
# 출력값 => hongwon5683@naver.com


# -----end 옵션 사용-----
print('Welcom To', end=' ') # end=   다음문장과 연결
print('the black parade', end=' ')
print('piano notes')

print()

#-----format 사용 [], {}, ()-----
# 1)
print('{} and {}'.format('You','Me'))
# 출력값 => You and Me

# 2)
print("{0} and {1} and {0}".format('Yoki','Nada'))
# 출력값 => Yoki and Nada and Yoki

print("{0} and {1} and {2}".format('Yoki','Nada','Me'))
# 출력값 => Yoki and Nada and Me

print("{a} are {b}".format(a='You', b='Yeowon'))
# 출력값 => You are Yeowon

#3)
# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" %('Sung',3))  

print("Test1: %5d, Price: %4.2f"  % (776, 6548.123))
print("Test1: {0:5d}, Price: {1: 4.2f}".format(776, 6352.118))
print("Test1: {a:5d}, Price: {b: 4.2f}".format(a=7764, b=2155.345))

print()

#-----Escape Code 사용법-----

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""
#  출력값 => 'you' 
print("'you'") 
print('\'you\'') 
print('"you"')
print("""'you'""")

# 출력값 => \you\
print('\\you\\\n')

# \t 로인해 들여쓰기
# 출력값 =>                         test
print('\t\t\ttest')