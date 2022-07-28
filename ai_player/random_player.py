import numpy as np
import utils
import time

class Random_player:
    def __init__(self):
        self.name = "Random player"

    def select_action(self, environment, player, renderer):
        # 가능한 행동 조사
        available_action = environment.get_action(player)
        # 가능한 행동 중 하나를 무작위로 선택
        action = np.random.randint(len(available_action))
        utils.count_processing(available_action, action, environment, player)

        return available_action[action]
