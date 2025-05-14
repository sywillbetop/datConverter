'''
1) 1~100 사이의 랜덤 정수 5개로 구성된 100줄 데이터를 생성하여 homework.dat 파일에 저장합니다.
2) 각 줄의 데이터(정수 5개)의 합과 평균을 계산해서 result.dat에 저장합니다.
3) result.dat의 결과를 읽어와 보기 좋게 터미널에 출력합니다.
※ 모든 주요 동작과 파일 입출력, 계산 단계에 대해 팀원이 쉽게 이해할 수 있도록 한글로 설명을 추가하였습니다.
'''

import random

def make_homework():
    """
    1~100 사이의 랜덤 정수 5개를 한 줄에 담아, 총 100줄을 homework.dat 파일에 저장합니다.
    """
    with open("homework.dat", "w", encoding="utf-8") as f:
        for i in range(100): 
            # 1~100까지의 정수 중 5개를 랜덤하게 뽑아서 문자열로 변환
            nums = [str(random.randint(1, 100)) for i in range(5)] 
            # 5개의 숫자를 한 줄로 합쳐서 공백으로 구분
            line = " ".join(nums)
            # 파일에 한 줄씩 저장 (줄바꿈 포함)
            f.write(line + "\n")

def make_result():
    """
    homework.dat 파일을 읽어서 각 줄의 정수들과 합과 평균을 계산합니다.
    계산 결과(각 줄의 5개 숫자, 합, 평균)를 result.dat 파일에 저장합니다.
    이후, 저장된 result.dat 파일을 화면에 출력합니다.
    """
    with open("homework.dat", "r") as in_f, open("result.dat", "w") as out_f:
        for line in in_f:
            # 한 줄의 숫자(문자열)를 공백 기준으로 나눠서 정수형으로 변환
            nums = list(map(int, line.strip().split()))
            # 5개 숫자의 합의 계산
            total = sum(nums)
            # 평균 계산 (소수점 둘째 자리까지)
            avg = total / len(nums)
            # 한 줄의 결과를 '숫자들 | 합: 값 | 평균: 값' 형식으로 저장
            out_f.write(f"{' '.join(map(str, nums))} | 합: {total} | 평균: {avg:.2f}\n")
    
    print_result()

def print_result():
    """
    result.dat 파일을 읽어서, 각 줄의 결과(숫자, 합, 평균)를 터미널에 표 형태로 예쁘게 출력합니다.
    컬러 코드를 사용하여 가독성을 높였습니다.
    """
    with open("result.dat", "r") as f:
        print("\033[90m-"*53) # 표의 상단 구분선
        print(f"| \033[0m{'결과 테이블':>26} \033[90m{'|':>19}") # 표 제목(가운데 정렬)
        print("-"*53)
        # 컬럼명(데이터, 합, 평균) 출력
        print(f"\033[90m| \033[92m{'데이터':>12} \033[90m{'|':>9} \033[96m{'합':>5} \033[90m{'|':>4} \033[95m{'평균':>6} \033[90m{'|':>4}")
        print("\033[90m-"*53)

        for line in f:
            # 한 줄을 '|' 기준으로 분리하여 데이터, 합, 평균 부분 추출
            parts = line.strip().split("|")
            data = parts[0].strip() # 5개의 정수 데이터
            total = parts[1].split(":")[1].strip() # 합 값만 추출
            avg = parts[2].split(":")[1].strip() # 평균 값만 추출

            # 각 데이터를 컬러 및 정렬 포맷으로 출력
            print(f"\033[90m| \033[92m{data:<23} \033[90m| \033[96m{total:>9} \033[90m| \033[95m{avg:>11} \033[90m|")
        print("-"*53) # 표의 하단 구분선 출력

# 전체 실행 ( 데이터 생성 -> 결과 계산/저장 -> 결과 출력)
make_homework()
make_result()
