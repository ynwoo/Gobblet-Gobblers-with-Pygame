import sys
import pygame
from pygame.locals import QUIT


class Human_player:
    def __init__(self, FPSCLOCK, FPS, renderer):
        self.name = "Human player"
        self.first_click = True
        self.h = -1

        self.f_col = -1
        self.f_row = -1

        self.s_col = -1
        self.s_row = -1

        self.cnt = 0

        self.FPSCLOCK = FPSCLOCK
        self.FPS = FPS
        self.renderer = renderer

    def select_action(self, environment, player):
        while True:
            self.FPSCLOCK.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # 왼쪽 마우스 클릭이면
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # 마우스 클릭 좌표
                    x, y = pygame.mouse.get_pos()
                    if player == 1:
                        if self.first_click:
                            if y > ((environment.height * 4) / 6):  # 입력 불가능한 부분
                                print("You selected wrong action : 상대방의 말은 선택이 불가능합니다.")
                                continue

                            elif y <= (environment.height / 6):
                                if 0 < x < (environment.width / 3):
                                    if environment.p1_piece[0] + environment.p1_piece[1] == 0:
                                        print("You selected wrong action : 남은 말이 없습니다.")
                                        continue
                                    else:
                                        if 0 < x < (environment.width / 6):  # 왼쪽 작은 말
                                            if environment.p1_piece[0] == 1:
                                                self.h = 0
                                            else:
                                                self.h = 3
                                        else:  # 오른쪽 작은 말
                                            if environment.p1_piece[1] == 1:
                                                self.h = 3
                                            else:
                                                self.h = 0
                                        self.first_click = False
                                        self.cnt += 1
                                        # 말 선택시 네모 사각형 표시
                                        self.renderer.select_box(player, self.h % 3)

                                elif (environment.width / 3) < x < (environment.width * 2 / 3):
                                    if environment.p1_piece[2] + environment.p1_piece[3] == 0:
                                        print("You selected wrong action")
                                        continue
                                    else:
                                        if 0 < x < (environment.width / 2):  # 왼쪽 중간 말
                                            if environment.p1_piece[2] == 1:
                                                self.h = 1
                                            else:
                                                self.h = 4
                                        else:  # 오른쪽 중간 말
                                            if environment.p1_piece[3] == 1:
                                                self.h = 4
                                            else:
                                                self.h = 1
                                        self.first_click = False
                                        self.cnt += 1
                                        self.renderer.select_box(player, self.h % 3)
                                else:
                                    if environment.p1_piece[4] + environment.p1_piece[5] == 0:
                                        print("You selected wrong action")
                                        continue
                                    else:
                                        if 0 < x < (environment.width * 5 / 6):  # 왼쪽 큰 말
                                            if environment.p1_piece[4] == 1:
                                                self.h = 2
                                            else:
                                                self.h = 5
                                        else:  # 오른쪽 큰 말
                                            if environment.p1_piece[5] == 1:
                                                self.h = 5
                                            else:
                                                self.h = 2
                                        self.first_click = False
                                        self.cnt += 1
                                        self.renderer.select_box(player, self.h % 3)

                            else:
                                self.f_col, self.f_row = self.coordinate_change(x, y, environment)
                                if environment.board_v[self.f_row * 3 + self.f_col] == player:
                                    self.first_click = False
                                    self.cnt += 1
                                    self.renderer.select_box2(self.f_col, self.f_row)
                                else:
                                    print("You selected wrong action")

                        else:  # 1p의 두번째 클릭인 경우
                            if y > ((environment.height * 4) / 6) or y <= (environment.height / 6):  # 입력 불가능한 부분
                                print("You selected wrong action")
                                continue
                            else:
                                self.s_col, self.s_row = self.coordinate_change(x, y, environment)
                                self.cnt += 1

                    else:  # player == 2
                        if self.first_click:
                            if y > ((environment.height * 5) / 6) or y <= (environment.height / 6):  # 입력 불가능한 부분
                                print("You selected wrong action")
                                continue

                            elif y > ((environment.height * 4) / 6):
                                if 0 < x < (environment.width / 3):
                                    if environment.p2_piece[0] + environment.p2_piece[1] == 0:
                                        print("You selected wrong action")
                                        continue
                                    else:
                                        if 0 < x < (environment.width / 6):  # 왼쪽 작은 말
                                            if environment.p2_piece[0] == 1:
                                                self.h = 0
                                            else:
                                                self.h = 3
                                        else:  # 오른쪽 작은 말
                                            if environment.p2_piece[1] == 1:
                                                self.h = 3
                                            else:
                                                self.h = 0
                                        self.first_click = False
                                        self.cnt += 1
                                        self.renderer.select_box(player, self.h % 3)
                                elif (environment.width / 3) < x < (environment.width * 2 / 3):
                                    if environment.p2_piece[2] + environment.p2_piece[3] == 0:
                                        print("You selected wrong action")
                                        continue
                                    else:
                                        if 0 < x < (environment.width / 2):  # 왼쪽 중간 말
                                            if environment.p2_piece[2] == 1:
                                                self.h = 1
                                            else:
                                                self.h = 4
                                        else:  # 오른쪽 중간 말
                                            if environment.p2_piece[3] == 1:
                                                self.h = 4
                                            else:
                                                self.h = 1
                                        self.first_click = False
                                        self.cnt += 1
                                        self.renderer.select_box(player, self.h % 3)
                                else:
                                    if environment.p2_piece[4] + environment.p2_piece[5] == 0:
                                        print("You selected wrong action")
                                        continue
                                    else:
                                        if 0 < x < (environment.width * 5 / 6):  # 왼쪽 큰 말
                                            if environment.p2_piece[4] == 1:
                                                self.h = 2
                                            else:
                                                self.h = 5
                                        else:  # 오른쪽 큰 말
                                            if environment.p2_piece[5] == 1:
                                                self.h = 5
                                            else:
                                                self.h = 2
                                        self.first_click = False
                                        self.cnt += 1
                                        self.renderer.select_box(player, self.h % 3)

                            else:
                                self.f_col, self.f_row = self.coordinate_change(x, y, environment)
                                if environment.board_v[self.f_row * 3 + self.f_col] == player:
                                    self.first_click = False
                                    self.cnt += 1
                                    self.renderer.select_box2(self.f_col, self.f_row)
                                else:
                                    print("You selected wrong action")
                        else:  # 2p의 두번째 클릭인 경우
                            if y > ((environment.height * 4) / 6) or y <= (environment.height / 6):  # 입력 불가능한 부분
                                continue
                            else:
                                self.s_col, self.s_row = self.coordinate_change(x, y, environment)
                                self.cnt += 1

                    available_action = environment.get_action(player)
                    if self.cnt != 2:
                        continue
                    action = self.get_action(environment, player)
                    if action in available_action:
                        if isinstance(action, int):
                            if player == 1:
                                if action < 9:
                                    if self.h == 0:
                                        environment.p1_piece[0] -= 1
                                    else:
                                        environment.p1_piece[1] -= 1
                                elif action < 18:
                                    if self.h == 1:
                                        environment.p1_piece[2] -= 1
                                    else:
                                        environment.p1_piece[3] -= 1
                                else:
                                    if self.h == 2:
                                        environment.p1_piece[4] -= 1
                                    else:
                                        environment.p1_piece[5] -= 1

                            else:
                                if action < 9:
                                    if self.h == 0:
                                        environment.p2_piece[0] -= 1
                                    else:
                                        environment.p2_piece[1] -= 1
                                elif action < 18:
                                    if self.h == 1:
                                        environment.p2_piece[2] -= 1
                                    else:
                                        environment.p2_piece[3] -= 1
                                else:
                                    if self.h == 2:
                                        environment.p2_piece[4] -= 1
                                    else:
                                        environment.p2_piece[5] -= 1

                        self.first_click = True
                        self.h = -1
                        self.f_col = -1
                        self.f_row = -1
                        self.s_col = -1
                        self.s_row = -1
                        self.cnt = 0
                        return action
                    else:
                        print("You selected wrong action")
                        self.renderer.rendering(environment)
                        self.first_click = True
                        self.h = -1
                        self.f_col = -1
                        self.f_row = -1
                        self.s_col = -1
                        self.s_row = -1
                        self.cnt = 0

    def get_action(self, environment, player):
        if self.h != -1:  # 새로 놓는 행동이라면
            return (self.h % 3) * 9 + self.s_row * 3 + self.s_col
        else:
            if environment.board_r[self.f_row * 3 + self.f_col + 18] == player:
                return str(self.f_row * 3 + self.f_col + 18) + "to" + str(self.s_row * 3 + self.s_col + 18)
            if environment.board_r[self.f_row * 3 + self.f_col + 9] == player:
                return str(self.f_row * 3 + self.f_col + 9) + "to" + str(self.s_row * 3 + self.s_col + 9)
            return str(self.f_row * 3 + self.f_col) + "to" + str(self.s_row * 3 + self.s_col)

    def coordinate_change(self, x, y, environment):
        if x < environment.width / 3:
            col = 0
        elif x < environment.width / 3 * 2:
            col = 1
        else:
            col = 2

        if environment.height / 3 > y > environment.height / 6:
            row = 0
        elif environment.height / 2 > y > environment.height / 3:
            row = 1
        else:
            row = 2

        return col, row
