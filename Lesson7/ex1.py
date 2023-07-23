from random import randint


# ~0.13c на проверку
def check_queen_position(positions: list):
    board = [['.' for _ in range(8)] for _ in range(8)]
    board[positions[0][0]][positions[0][1]] = 'Q'
    for row, col in positions[1:]:
        if 'Q' in board[row]:
            return False
        elif 'Q' in [i[col] for i in board]:
            return False
        elif 'Q' in [board[i][j] for i in range(8) for j in range(8) if abs(i - row) == abs(j - col)]:
            return False
        board[row][col] = 'Q'
    return positions


# ~0.045с на проверку
# def check_queen_positions(positions: list):
#     for row, col in positions:
#         r, c = row, col
#         while r < 8 or c < 8:
#             if (r + 1, c + 1) in positions:
#                 return False
#             r += 1
#             c += 1
#         r, c = row, col
#         while 0 <= r < 8 or 0 <= c < 8:
#             if (r + 1, c - 1) in positions:
#                 return False
#             r += 1
#             c -= 1
#     return True

# ~0.017с на проверку
def check_queen_positions(positions: list):
    for k in range(len(positions)):
        if any([abs(i - positions[k][0]) == abs(j - positions[k][1]) for i, j in positions[k + 1:]]):
            return False
    return True


# 0.023с Логика от Андрея + мой генератор
# def check_queen_positions(positions: list):
#     queens = [10 * row + col for row, col in positions]
#     for i in range(len(queens)):
#         for j in range(i + 1, len(queens)):
#             if ((queens[j] // 10 > queens[i] // 10 and queens[j] % 10 > queens[i] % 10) or
#                 (queens[i] // 10 > queens[j] // 10 and queens[i] % 10 > queens[j] % 10)) and \
#                     (queens[j] - queens[i]) % 11 == 0:  # проверка на диагональ "вправо-вниз"
#                 return False
#             if ((queens[j] // 10 > queens[i] // 10 and queens[j] % 10 < queens[i] % 10) or
#                 (queens[i] // 10 > queens[j] // 10 and queens[i] % 10 < queens[j] % 10)) and \
#                     (queens[j] - queens[i]) % 9 == 0:  # проверка на диагональ "влево-вниз"
#                 return False
#     return positions


def generate_random_positions():
    positions = []
    while len(positions) < 8:
        rand = randint(0, 7), randint(0, 7)
        if rand not in positions:
            positions.append(rand)
    return positions


def generate_all():
    success = []
    numbers_a = [i for i in range(8)]
    for a in numbers_a:
        numbers_b = numbers_a[:]
        numbers_b.remove(a)
        for b in numbers_b:
            variants = [(0, a), (1, b)]
            if b == a + 1 or b == a - 1:
                continue
            if check_queen_positions(variants):
                numbers_c = numbers_b[:]
                numbers_c.remove(b)
                for c in numbers_c:
                    variants = [(0, a), (1, b), (2, c)]
                    if c == b + 1 or c == b - 1:
                        continue
                    if check_queen_positions(variants):
                        numbers_d = numbers_c[:]
                        numbers_d.remove(c)
                        for d in numbers_d:
                            variants = [(0, a), (1, b), (2, c), (3, d)]
                            if d == c + 1 or d == c - 1:
                                continue
                            if check_queen_positions(variants):
                                numbers_e = numbers_d[:]
                                numbers_e.remove(d)
                                for e in numbers_e:
                                    variants = [(0, a), (1, b), (2, c), (3, d), (4, e)]
                                    if e == d + 1 or e == d - 1:
                                        continue
                                    if check_queen_positions(variants):
                                        numbers_f = numbers_e[:]
                                        numbers_f.remove(e)
                                        for f in numbers_f:
                                            variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f)]
                                            if f == e + 1 or f == e - 1:
                                                continue
                                            if check_queen_positions(variants):
                                                numbers_g = numbers_f[:]
                                                numbers_g.remove(f)
                                                for g in numbers_g:
                                                    variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f), (6, g)]
                                                    if g == f + 1 or g == f - 1:
                                                        continue
                                                    if check_queen_positions(variants):
                                                        numbers_h = numbers_g[:]
                                                        numbers_h.remove(g)
                                                        for h in numbers_h:
                                                            variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f),
                                                                        (6, g), (7, h)]
                                                            if h == g + 1 or h == g - 1:
                                                                continue
                                                            if check_queen_positions(variants):
                                                                success.append(variants)
    return success


for i, res in enumerate(generate_all(), start=1):
    print(f"{i}: {res}")
