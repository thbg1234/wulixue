'''
    작성일 : 2023년 9월 20일
    작성자 : 석홍신(202195056)


    설명 : 선택문 if~else
           년도를 입력 받아 윤년인지 아닌지 판단하는 프로그램.
           
           윤년?
           연도를 4로 나누어 떨어지면 윤년이다.
           연도를 4로 나누어 떨어져도, 100으로는 나누어 떨어지지 않아야 한다.
                -> (모두 만족 : and연산자.  &&)
           연도를 400으로 나누어 떨어지는 해는 무조건 윤년이다.
'''

year = int(input("연도를 입력하시오 : "))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) :
    print(year,"년은 윤년입니다.")
else :
    print(year,"년은 윤년이 아닙니다.")