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
    """
    숫자 리스트에서 최대값을 반환합니다.

    Args:
        numbers: 숫자가 담긴 리스트

    Returns:
        리스트 내 최대값

    Example:
        >>> find_max([1, 5, 3, 9, 2])
        9
        >>> find_max([-1, -5, -3])
        -1
    """
    # TODO: 리스트에서 최대값을 찾아 반환하는 코드를 작성하세요
    pass


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
