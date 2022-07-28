import pygame
from environment import Environment
from config import Config
from renderer import Renderer
from human_player import Human_player
# from ai_player.random_player import Random_player
# from ai_player.monte_carlo_player import Monte_Carlo_player


def main():
    cfg = Config()

    pygame.init()
    screen = pygame.display.set_mode(cfg.window_size)
    font = pygame.font.SysFont(cfg.font, cfg.font_size)
    FPSCLOCK = pygame.time.Clock()
    FPS = cfg.FPS
    pygame.display.set_caption(cfg.caption_name)

    # 환경구성
    env = Environment(cfg)
    # 렌더링
    renderer = Renderer(font, screen, cfg, env, FPSCLOCK, FPS)

    # 인간 플레이어
    p1 = Human_player(FPSCLOCK, FPS, renderer)
    p2 = Human_player(FPSCLOCK, FPS, renderer)
    
    # 랜덤 플레이어
    # p1 = Random_player()
    # p2 = Random_player()

    # MC 플레이어
    # p1 = Monte_Carlo_player()
    # p2 = Monte_Carlo_player()

    # 스코어 보드
    p1_score = 0
    p2_score = 0
    draw_score = 0

    i = 0
    while True:
        reward, done = env.move(p1, p2, (-1)**i)  # 1,-1,1,-1...
        renderer.rendering(env)
        i += 1
        if done:
            if reward == 1:
                print("winner is p1({})".format(p1.name))
                p1_score += 1
            elif reward == -1:
                print("winner is p2({})".format(p2.name))
                p2_score += 1
            else:
                print("draw")
                draw_score += 1

            print("p1({}) = {} p2({}) = {} draw = {}".format(p1.name, p1_score, p2.name, p2_score, draw_score))

            env.reset_game()
            renderer.new_game_window(env)
            i = 0


if __name__ == '__main__':
    main()
