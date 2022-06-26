# print(52,273,"Hello") 너무 기본적이예요~


# 문자열

# 이스케이프 문자로(\t) 탭 사용하기!
# print("이름\t나이\t지역")
print("name\tage\tregion")
print("Jeon\t35\tIncheon")
print("")

# 이스케이프 문자로(\n) 여러줄 문자열 만들기!
print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세\n무궁화 삼천리 화려강산 대한사람\n대한으로 길이 보전하세")

# 줄 바꿈 없이 문자열 만들기
print("""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강사
대한사람 대한으로 길이 보전하세
""","\n")

# 문자열 반복 연산자(곱하기)
print("안녕하세요 "*3,"\n")

# 문자열 선택 연산자 - 인덱싱[]
print("문자열 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4],"\n")

# 문자열 범위 선택 연산자(슬라이싱)
print("JeonSeokhwan")
print("JeonSeokhwan"[0:4])
print("JeonSeokhwan"[4:],"\n")
# 문자열 뒤에서 선택하기
print("# 문자열 뒤에서 선택하기")
print("JeonSeokhwan"[-4:],"\n")

# 문자열 길이 구하기
print("# 문자열 길이 구하기")
myName = "Jeon Seokhwan"
print(myName)
print(len(myName))