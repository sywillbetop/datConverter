'''
파이썬이 지원하는 random 모듈을 사용하여,
1) 한 줄에 5개씩의 정수값을 채워, 100줄을 생성하여 homwork.dat이라고 명명한 파일에 저장하라.
2) 각 줄의 데이터의 합과 평균을 구하여 result.dat에 저장하고, 
3) result.dat에 저장된 결과를 화면에 출력하라.
기타 인터페이스를 예쁘게 출력하는 것은 여러분에 맡깁니다.
'''

import random

def make_homework():
    with open("homework.dat", "w", encoding="utf-8") as f:
        for i in range(100):
            nums = [str(random.randint(1, 100)) for i in range(5)]
            line = " ".join(nums)
            f.write(line + "\n")

def make_result():
    with open("homework.dat", "r") as in_f, open("result.dat", "w") as out_f:
        for line in in_f:
            nums = list(map(int, line.strip().split()))
            total = sum(nums)
            avg = total / len(nums)
            out_f.write(f"{' '.join(map(str, nums))} | 합: {total} | 평균: {avg:.2f}\n")
    
    print_result()

def print_result():
    with open("result.dat", "r") as f:
        print("\033[90m-"*53)
        print(f"| \033[0m{'결과 테이블':>26} \033[90m{'|':>19}")
        print("-"*53)
        print(f"\033[90m| \033[92m{'데이터':>12} \033[90m{'|':>9} \033[96m{'합':>5} \033[90m{'|':>4} \033[95m{'평균':>6} \033[90m{'|':>4}")
        print("\033[90m-"*53)

        for line in f:
            parts = line.strip().split("|")
            data = parts[0].strip()
            total = parts[1].split(":")[1].strip()
            avg = parts[2].split(":")[1].strip()

            print(f"\033[90m| \033[92m{data:<23} \033[90m| \033[96m{total:>9} \033[90m| \033[95m{avg:>11} \033[90m|")
        print("-"*53)

make_homework()
make_result()
