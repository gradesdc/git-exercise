"""
Git 워크플로우 실습 - 기본 함수 구현하기

이 파일의 TODO 부분을 완성하고, VSCode에서 Git을 사용해
변경사항을 커밋하고 Push 해보세요!
"""


def calculate_sum(a: int, b: int) -> int:
    return a + b


def calculate_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)

def find_max(numbers: list) -> int:
    return max(numbers)


if __name__ == "__main__":
    # 테스트 실행
    print("=== 함수 테스트 ===")

    # calculate_sum 테스트
    result = calculate_sum(3, 5)
    print(f"calculate_sum(3, 5) = {result}")

    # calculate_average 테스트
    result = calculate_average([1, 2, 3, 4, 5])
    print(f"calculate_average([1, 2, 3, 4, 5]) = {result}")

    # find_max 테스트
    result = find_max([1, 5, 3, 9, 2])
    print(f"find_max([1, 5, 3, 9, 2]) = {result}")
