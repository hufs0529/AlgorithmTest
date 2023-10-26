def find_consecutive_increases(matrix):
    results = []

    for row in matrix:
        consecutive_count = 1  # 연속적으로 증가하는 요소의 개수를 추적하기 위한 변수
        max_consecutive_count = 1  # 최대 연속적으로 증가하는 요소의 개수를 추적하기 위한 변수

        for i in range(1, len(row)):
            if row[i] > row[i - 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1

            if consecutive_count > max_consecutive_count:
                max_consecutive_count = consecutive_count

        results.append(max_consecutive_count)

    return results

# 예시 2차원 배열
matrix = [
    [1, 2, 3, 4, 5],
    [1, 1, 2, 3, 4],
    [1, 1, 1, 2, 3],
    [1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1]
]

consecutive_increases = find_consecutive_increases(matrix)

for i, count in enumerate(consecutive_increases):
    print(f"행 {i + 1}: 가장 긴 연속적인 증가 요소 수 = {count}")
