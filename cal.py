# 계산기 만들기
def sum(a,b):
    # 덧셈 함수
    return a+b

def sub(a,b):
    # 뺄샘 함수
    return a-b;

def div(a,b):
    # 나눗셈 함수
    return a/b;

def mul(a,b):
    # 곱셈 함수
    return a*b;

if __name__=="__main__":
    print("계산기를 실행합니다.")
    
    # 사용자에게 입력을 받는 input 함수
    # operand1, operand2 라는 변수에 사용자의 입력값을 할당한다.
    operand1 =int(input("숫자를 입력하시오: "));
    operand2 =int(input("숫자를 입력하시오: "));

    print("결과를 출력합니다.")

    # 덧셈 결과를 출력한다.
    print(sum(operand1,operand2))

    # 뺄셈 결과를 출력한다.
    print(sub((operand1,operand2)))

    # 나눗셈 결과를 출력한다.
    print(div((operand1,operand2)))

    # 곱셈 결과를 출력한다.
    print(mul((operand1,operand2)))

    
