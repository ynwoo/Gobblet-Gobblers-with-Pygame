import numpy as np
import time
import utils

class Environment:
    def __init__(self, cfg):
        self.cfg = cfg
        # game window 창의 크기 값 설정
        self.width = cfg.window_size[0]
        self.height = cfg.window_size[1]

        # p1: 1, p2: -1, empty: 0
        self.board_r = np.zeros(27)
        self.board_v = np.zeros(9)

        # done: 게임이 끝났는지 여부, reward: 승자(1 or -1 or 0)
        self.done = False
        self.reward = 0
        self.turn = 1
        
        # 작은 말2개, 중간 말2개, 큰 말 2개씩
        self.p1_piece = [1, 1, 1, 1, 1, 1]
        self.p2_piece = [1, 1, 1, 1, 1, 1]

    def move(self, player1, player2, player):
        self.turn = player
        if player == 1:
            pos = player1.select_action(self, player)
        else:
            pos = player2.select_action(self, player)

        if isinstance(pos, int):  # 숫자라면
            self.board_r[pos] = player
        else:  # 문자라면 -> 움직이는 액션이다
            pos = pos.split('to')  # pos[0]가 지울 장소, pos[1]이 생길 장소

            # 원래 있던 자리에 있는 말을 지우고, 옮길 자리에 추가
            self.board_r[int(pos[0])] = 0
            self.board_r[int(pos[1])] = player

        self.end_check()
        self.turn*=-1
        return self.reward, self.done

    def get_action(self, player):
        observation = []
        if player == 1:
            if self.p1_piece[0] + self.p1_piece[1] != 0:
                for i in range(9):
                    if self.board_r[i] == 0:
                        observation.append(i)

            if self.p1_piece[2] + self.p1_piece[3] != 0:
                for i in range(9, 18):
                    if self.board_r[i] == 0:
                        observation.append(i)

            if self.p1_piece[4] + self.p1_piece[5] != 0:
                for i in range(18, 27):
                    if self.board_r[i] == 0:
                        observation.append(i)

        else:  # player == 2
            if self.p2_piece[0] + self.p2_piece[1] != 0:
                for i in range(9):
                    if self.board_r[i] == 0:
                        observation.append(i)
            if self.p2_piece[2] + self.p2_piece[3]:
                for i in range(9, 18):
                    if self.board_r[i] == 0:
                        observation.append(i)
            if self.p2_piece[4] + self.p2_piece[5] != 0:
                for i in range(18, 27):
                    if self.board_r[i] == 0:
                        observation.append(i)

        #  중간말이 놓인 위치에는 작은 말을 놓을 수 없다.(제거 작업)
        for i in range(9, 18):
            if self.board_r[i] != 0 and self.board_r[i - 9] == 0:
                if i - 9 in observation:
                    observation.remove(i - 9)

        for i in range(18, 27):
            # 큰 말이 놓인 위치에는 중간말과 작은 말을 놓을 수 없다.
            if self.board_r[i] != 0 and self.board_r[i - 9] == 0:
                if i - 9 in observation:
                    observation.remove(i - 9)
            if self.board_r[i] != 0 and self.board_r[i - 18] == 0:
                if i - 18 in observation:
                    observation.remove(i - 18)

        observation.sort()

        # 이동 가능한 경우의 수 추가
        for i in range(9):
            if self.board_r[i] == player and self.board_r[i + 9] == 0 and self.board_r[i + 18] == 0:
                for j in range(9):
                    if self.board_r[j] == 0 and self.board_r[j + 9] == 0 and self.board_r[j + 18] == 0:
                        observation.append("%sto%s" % (str(i), str(j)))

        for i in range(9, 18):
            if self.board_r[i] == player and self.board_r[i + 9] == 0:
                for j in range(9, 18):
                    if self.board_r[j] == 0 and self.board_r[j + 9] == 0:
                        observation.append("%sto%s" % (str(i), str(j)))

        for i in range(18, 27):
            if self.board_r[i] == player:
                # 옮길 수 있는 위치 탐색
                for j in range(18, 27):
                    # 빈 공간이면
                    if self.board_r[j] == 0:
                        observation.append("%sto%s" % (str(i), str(j)))

        return observation

    # 게임이 종료됐는지 판단
    def end_check(self):
        self.board_v = utils.copy_real2vision(self.board_r)
        # 0 1 2
        # 3 4 5
        # 6 7 8
        # 승패 조건은 가로, 세로, 대각선이 -1이나 1로 동일할 때
        # 승패 조건 생성
        end_condition = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        # 이긴사람의 수 카운트 -> 두명 다 라인을 완성할 경우 비기므로
        p1_cnt = 0
        p2_cnt = 0
        # 승리 판별
        for line in end_condition:
            if self.board_v[line[0]] == self.board_v[line[1]] and \
                    self.board_v[line[1]] == self.board_v[line[2]] and \
                    self.board_v[line[0]] == 1:
                self.done = True
                self.reward = 1
                p1_cnt += 1
            elif self.board_v[line[0]] == self.board_v[line[1]] and \
                    self.board_v[line[1]] == self.board_v[line[2]] and \
                    self.board_v[line[0]] == -1:  # 플레이어2 승리
                # 종료됐다면 누가 이겼는지 표시
                self.done = True
                self.reward = -1
                p2_cnt += 1

        # 비긴 상태. 양쪽 모두 승리 조건을 동시에 만족하는 경우.
        if p1_cnt >= 1 and p2_cnt >= 1:
            self.done = True
            self.reward = 0
        return

    def reset_game(self):
        time.sleep(self.cfg.reset_sleep_time)
        self.board_r = np.zeros(27)
        self.board_v = np.zeros(9)
        self.done = False
        self.reward = 0
        self.turn = 1
        self.p1_piece = [1, 1, 1, 1, 1, 1]
        self.p2_piece = [1, 1, 1, 1, 1, 1]
