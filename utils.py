import numpy as np

# 선택한 행동이 새로 말을 새롭게 놓는 행동이라면 값을 빼주어야함.
def count_processing(available_action, action, environment, player):
    if isinstance(available_action[action], int):
        if player == 1:
            if 0 <= available_action[action] <= 8:
                if environment.p1_piece[0] == 0:
                    environment.p1_piece[1] -= 1
                else:
                    environment.p1_piece[0] -= 1
            elif 9 <= available_action[action] <= 17:
                if environment.p1_piece[2] == 0:
                    environment.p1_piece[3] -= 1
                else:
                    environment.p1_piece[2] -= 1
            else:
                if environment.p1_piece[4] == 0:
                    environment.p1_piece[5] -= 1
                else:
                    environment.p1_piece[4] -= 1
        else:  # player == 2:
            if 0 <= available_action[action] <= 8:
                if environment.p2_piece[0] == 0:
                    environment.p2_piece[0] -= 1
                else:
                    environment.p2_piece[0] -= 1
            elif 9 <= available_action[action] <= 17:
                if environment.p2_piece[2] == 0:
                    environment.p2_piece[3] -= 1
                else:
                    environment.p2_piece[2] -= 1
            else:  # 18 <= action <= 26
                if environment.p2_piece[4] == 0:
                    environment.p2_piece[5] -= 1
                else:
                    environment.p2_piece[4] -= 1

# 승패 판정을 위한 보드 변환 함수
def copy_real2vision(board_r):
    board_v = np.zeros(9)
    for i in range(3):
        for j in range(3):
            if board_r[3 * i + j + 18] == 1:
                board_v[3 * i + j] = 1
            elif board_r[3 * i + j + 18] == -1:
                board_v[3 * i + j] = -1
            elif board_r[3 * i + j + 9] == 1:
                board_v[3 * i + j] = 1
            elif board_r[3 * i + j + 9] == -1:
                board_v[3 * i + j] = -1
            elif board_r[3 * i + j] == 1:
                board_v[3 * i + j] = 1
            elif board_r[3 * i + j] == -1:
                board_v[3 * i + j] = -1
    return board_v