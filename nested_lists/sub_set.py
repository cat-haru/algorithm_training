"""
2차원 행열이 주어질 때, 특정 지점에서 일정 크기의 부분행렬을 구할 필요가 있을 때

TODO 일단은 소스코드 정리는... 필요할 때 하기로 하고 유닛테스트도 나중에 따로 분리하는걸로...
TODO cProfile을 사용해서 풀이 방법 별 성능 비교해보기
"""

tiles = [
    ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'],
    ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'],
    ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29'],
    ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39'],
    ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49'],
    ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],
    ['60', '61', '62', '63', '64', '65', '66', '67', '68', '69'],
    ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79'],
    ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89'],
    ['90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
]

# 정방행렬일 때
n = len(tiles)

# 정방행렬이 아닐 때
max_row = len(tiles[0])
max_col = len(tiles)

# 부분행렬(정방행렬)의 크기 
k=2

def case1():
    """
    가장 단순하고 무식하게 모든 좌표를 순회하면서
    부분행렬을 탐색 후 출력하는 방법

    외부의 for 2중첩은 원행렬의 좌표 순회용
    내부의 for 2중첩은 부분행렬 추출을 위한 순회용
    """
    for row_num in range(n-k+1):
        for col_num in range(n-k+1):
            sub_tiles = list()

            for x in range(k):
                for y in range(k):
                    sub_tiles.append(tiles[row_num + x][col_num + y])

            print(f'[{row_num}, {col_num}] 좌표에서 부분행렬 -> {sub_tiles}\n')


def case2():

    for row_num in range(max_row-k+1):
        partial_tiles = tiles[row_num:row_num+k]

        for col_num in range(max_col-k+1):
            sub_tiles = [r[col_num:col_num+k] for r in partial_tiles]
            print(f'[{row_num}, {col_num}] 좌표에서 부분행렬 -> {sub_tiles}\n')

            # case1과 동일하게 1차원으로 flatten할 필요가 있으면
            # from itertools import chain
            # [v for v in chain(*sub_tiles)]
            # 처리를 더 해주면 되는데... 그러면 결국 4중첩...🤔


# TODO 원래 행렬을 flatten하여 풀어보기!
