# 사용자 입력 : input() 함수
print("#사용자 입력 input()함수")
hello = input("인사말을 입력하세요> ")
print(hello)
typeis = type(hello)
print("변수 hello의 자료형은",typeis,"\n\n")

#.. 아 근데 input() 값은 전부 문자형이네..
# -> 그래서 문자열을 숫자로 바꾸기!
print("#input으로 입력해도 숫자 연산이 되게 만들기!")
num1 = int(input("숫자 입력A> "))
num2 = int(input("숫자 입력B> "))
print("num1+num2 =",num1+num2)

numA = 10
numB = 10.25

fnumA = float(numA)
fnumB = float(numB)

print("numA + numB =",numA+numB)
print("(float)numA + (float)numB =",fnumA+fnumB)