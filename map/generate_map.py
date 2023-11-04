import random

def generate_map(M, N):
    total_cells = M * N
    water_cells = int(0.3 * total_cells)
    cells = [['W' for _ in range(N)] for _ in range(M)]

    for _ in range(water_cells):
        while True:
            i = random.randint(0, M - 1)
            j = random.randint(0, N - 1)
            if cells[i][j] == 'W':
                cells[i][j] = 'L'
                break

    return cells

def print_map(cells):
    for row in cells:
        print(' '.join(row))

def find_shortest_path(cells, start_row, start_col, end_row, end_col):
    visited = [[False for _ in range(len(cells[0]))] for _ in range(len(cells))]
    queue = [(start_row, start_col, 0)]

    while queue:
        i, j, distance = queue.pop(0)
        if i == end_row and j == end_col:
            return distance

        visited[i][j] = True

        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for x, y in neighbors:
            if 0 <= x < len(cells) and 0 <= y < len(cells[0]) and cells[x][y] == 'W' and not visited[x][y]:
                queue.append((x, y, distance + 1))

    return -1

def main():
    M = int(input("Введите количество строк (M): "))
    N = int(input("Введите количество столбцов (N): "))

    cells = generate_map(M, N)
    print("Сгенерированная карта:")
    print_map(cells)

    start_row, start_col = map(int, input("Введите координаты точки A (через пробел): ").split())
    end_row, end_col = map(int, input("Введите координаты точки B (через пробел): ").split())

    if not (0 <= start_row < M and 0 <= start_col < N and 0 <= end_row < M and 0 <= end_col < N):
        print("Ошибка: Координаты должны быть в пределах от (0,0) до ({},{})".format(M-1, N-1))
        return

    distance = find_shortest_path(cells, start_row, start_col, end_row, end_col)

    if distance == -1:
        print("Невозможно добраться из точки A в точку B.")
    else:
        print("Кратчайшее расстояние:", distance)

if __name__ == '__main__':
    main()
