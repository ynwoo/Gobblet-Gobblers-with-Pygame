from tkinter import Menu
import pygame
import time
import sys

class Button:
    def __init__(self, screen, img_in, x, y, width, height, img_act, x_act, y_act, action, menu = None, env = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act,(x_act, y_act))
            if click[0]:
                time.sleep(1)
                action(env)
                menu[0] = False
        else:
            screen.blit(img_in, (x,y))

class Renderer:
    def __init__(self, font, screen, cfg, env, FPSCLOCK, FPS):
        # font setting
        self.font = font
        self.cfg = cfg
        self.width = cfg.window_size[0]
        self.height = cfg.window_size[1]

        # load image
        self.initiating_window = pygame.image.load("rsc/cover.png")
        self.p1_image = pygame.image.load("rsc/red.png")
        self.p2_image = pygame.image.load("rsc/blue.png")
        self.empty_img = pygame.image.load("rsc/NULL.png")
        self.empty_img2 = pygame.image.load("rsc/NULL2.png")

        self.startImg = pygame.image.load("rsc/starticon.png")
        self.quitImg = pygame.image.load("rsc/quiticon.png")
        self.click_startImg = pygame.image.load("rsc/clickedStartIcon.png")
        self.click_quitImg = pygame.image.load("rsc/clickedQuitIcon.png")
        # scale image
        self.initiating_window = pygame.transform.scale(self.initiating_window, (self.width, self.height + 100))

        self.p1_big = pygame.transform.scale(self.p1_image, (65, 65))
        self.p1_mid = pygame.transform.scale(self.p1_image, (45, 45))
        self.p1_small = pygame.transform.scale(self.p1_image, (20, 20))

        self.p2_big = pygame.transform.scale(self.p2_image, (65, 65))
        self.p2_mid = pygame.transform.scale(self.p2_image, (45, 45))
        self.p2_small = pygame.transform.scale(self.p2_image, (20, 20))

        self.empty_img = pygame.transform.scale(self.empty_img, (75, 75))
        self.empty_img2 = pygame.transform.scale(self.empty_img2, (65, 65))

        self.screen = screen
        self.FPSCLOCK = FPSCLOCK
        self.FPS = FPS
        self.new_game_window(env)

    def quitgame(self, tmp=None):
        pygame.quit()
        sys.exit()

    def new_game_window(self, env):
        menu = [True]
        self.screen.blit(self.initiating_window, (0, 0))
        while menu[0]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            startButton = Button(self.screen, self.startImg, 172,480,60,20,self.click_startImg,165,478,self.rendering, menu, env)
            if not menu[0]:
                break
            quitButton = Button(self.screen, self.quitImg, 180,530,60,20,self.click_quitImg,175,528,self.quitgame)
            pygame.display.update()
            self.FPSCLOCK.tick(self.FPS)
        
    
    def rendering(self, env):
        self.screen.fill((176, 136, 94))
        self.screen.fill((210, 180, 140), (0, 0, self.width, 100))
        self.screen.fill((210, 180, 140), (0, 400, self.width, 500))

        # 세로줄 그리기
        # pygame.draw.line(화면, 색, 시작위치, 끝위치, 굵기)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width / 3, 0), (self.width / 3,
                                                                             self.height - (self.height / 6)), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width / 3 * 2, 0), (self.width / 3 * 2,
                                                                                 self.height - (self.height / 6)), 5)

        # 가로줄 그리기
        pygame.draw.line(self.screen, (0, 0, 0), (0, 0), (self.width, 0), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height / 6), (self.width, self.height / 6), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height / 3), (self.width, self.height / 3), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height / 2), (self.width, self.height / 2), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height / 3 * 2), (self.width, self.height / 3 * 2), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height / 6 * 5), (self.width, self.height / 6 * 5), 5)

        if env.p1_piece[0] == 1:
            self.screen.blit(self.p1_small, (30, 40))
        if env.p1_piece[1] == 1:
            self.screen.blit(self.p1_small, (80, 40))
        if env.p1_piece[2] == 1:
            self.screen.blit(self.p1_mid, (150, 27.5))
        if env.p1_piece[3] == 1:
            self.screen.blit(self.p1_mid, (205, 27.5))
        if env.p1_piece[4] == 1:
            self.screen.blit(self.p1_big, (270, 17.5))
        if env.p1_piece[5] == 1:
            self.screen.blit(self.p1_big, (334, 17.5))

        if env.p2_piece[0] == 1:
            self.screen.blit(self.p2_small, (30, 40 + 400))
        if env.p2_piece[1] == 1:
            self.screen.blit(self.p2_small, (80, 40 + 400))
        if env.p2_piece[2] == 1:
            self.screen.blit(self.p2_mid, (150, 27.5 + 400))
        if env.p2_piece[3] == 1:
            self.screen.blit(self.p2_mid, (205, 27.5 + 400))
        if env.p2_piece[4] == 1:
            self.screen.blit(self.p2_big, (270, 17.5 + 400))
        if env.p2_piece[5] == 1:
            self.screen.blit(self.p2_big, (334, 17.5 + 400))
        
        # 놓여있는 말 표시
        self.board2screen(env)

        # 상태창 표시
        self.draw_status(env)
    
    def board2screen(self, env):
        array = env.board_r.reshape(3, 3, 3)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if array[i][j][k] == 1:
                        if j == 0:
                            posx = self.height * 3 / 12
                        if j == 1:
                            posx = self.height * 5 / 12
                        if j == 2:
                            posx = self.height * 7 / 12

                        if k == 0:
                            posy = self.width / 6
                        if k == 1:
                            posy = self.width / 2
                        if k == 2:
                            posy = self.width / 6 * 5

                        if i == 0:
                            self.screen.blit(self.p1_small, (posy - 10, posx - 10))
                        elif i == 1:
                            self.screen.blit(self.p1_mid, (posy - 20, posx - 20))
                        else:  # which_icon == 2
                            self.screen.blit(self.p1_big, (posy - 30, posx - 30))

                    elif array[i][j][k] == -1:
                        if j == 0:
                            posx = self.height * 3 / 12
                        if j == 1:
                            posx = self.height * 5 / 12
                        if j == 2:
                            posx = self.height * 7 / 12

                        if k == 0:
                            posy = self.width / 6
                        if k == 1:
                            posy = self.width / 2
                        if k == 2:
                            posy = self.width / 6 * 5

                        if i == 0:
                            self.screen.blit(self.p2_small, (posy - 10, posx - 10))
                        elif i == 1:
                            self.screen.blit(self.p2_mid, (posy - 20, posx - 20))
                        else:
                            self.screen.blit(self.p2_big, (posy - 30, posx - 30))
    
    def draw_status(self, env):
        player = env.turn
        if env.done:
            if env.reward == 1:
                message = "Red won !"
            elif env.reward == -1:
                message = "Blue won !"
            else:
                message = "Game Draw !"
        else:
            if player == 1:
                message = "Red's Turn"
            else:
                message = "Blue's Turn"

        # 텍스트의 너비 및 색
        text = self.font.render(message, True, self.cfg.WHITE)

        # 메세지 복사
        # 메인 디스플레이 하단에 작은 블록 생성
        self.screen.fill(self.cfg.BLACK, (0, self.height - 100, self.width, self.height))
        text_rect = text.get_rect(center=(self.width / 2, 600 - 50))
        self.screen.blit(text, text_rect)
        pygame.display.update()
    
    def select_box(self, player, h):
        w3 = self.width / 3
        h6 = self.height / 6
        YELLOW = self.cfg.YELLOW
        BOLD = self.cfg.BOLD
        if player == 1:
            pygame.draw.line(self.screen, YELLOW,
            (h * w3, 0), ((h + 1) * w3, 0), BOLD)
            pygame.draw.line(self.screen, YELLOW,
            (h * w3, h6), ((h + 1) * w3, h6), BOLD)
            pygame.draw.line(self.screen, YELLOW,
            (h * w3, 0),(h * w3, h6), BOLD)
            pygame.draw.line(self.screen, YELLOW,
            ((h + 1) * w3, 0), ((h + 1) * w3, h6), BOLD)

        else:
            pygame.draw.line(self.screen, YELLOW,
            (h * w3, 4*h6), ((h + 1) * w3, 4*h6), 5)
            pygame.draw.line(self.screen, YELLOW,
            (h * w3, 5*h6),((h + 1) * w3, 5*h6), 5)
            pygame.draw.line(self.screen, YELLOW,
            (h * w3, 4*h6),(h * w3, 5*h6), 5)
            pygame.draw.line(self.screen, YELLOW,
            ((h + 1) * w3, 4*h6),((h + 1) * w3, 5*h6), 5)
        pygame.display.update()
    
    def select_box2(self, col, row):
        w3 = self.width / 3
        h6 = self.height / 6
        YELLOW = self.cfg.YELLOW
        BOLD = self.cfg.BOLD
        pygame.draw.line(self.screen, YELLOW,
        (col * w3, h6 * (row + 1)), ((col + 1) * w3, h6 * (row + 1)), BOLD)
        pygame.draw.line(self.screen, YELLOW,
        (col * w3, h6 * (row + 2)), ((col + 1) * w3, h6 * (row + 2)), BOLD)
        pygame.draw.line(self.screen, YELLOW,
        (col * w3, h6 * (row + 1)), (col * w3, h6 * (row + 2)), BOLD)
        pygame.draw.line(self.screen, YELLOW,
        ((col + 1) * w3, h6 * (row + 1)), ((col + 1) * w3, h6 * (row + 2)), BOLD)
        pygame.display.update()