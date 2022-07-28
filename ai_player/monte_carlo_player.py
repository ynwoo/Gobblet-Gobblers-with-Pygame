import numpy as np
import copy
import utils


class Monte_Carlo_player:
    def __init__(self):
        self.name = "MC player"
        self.num_playout = 300

    def select_action(self, environment, player):
        # 가능한 행동 조사
        available_action = environment.get_action(player)

        # 상태가치를 저장할 배열 V
        V = np.zeros(len(available_action))

         # 가능한 행동들을 돌면서 V[i]+=1을 해줌
        for i in range(len(available_action)):
            # 플레이 아웃을 1000번 반복
            for j in range(self.num_playout):
                # 지금 상태를 복사해서 플레이 아웃에 사용
                temp_env = copy.deepcopy(environment)
                utils.count_processing(available_action, i, temp_env, player)
                self.playout(temp_env, available_action[i], player)
                if player == temp_env.reward:
                    V[i] += 1

        # 가장 승률이 높은 행동을 저장
        action = np.argmax(V)
        utils.count_processing(available_action, action, environment, player)
        return available_action[action]
    
    # 플레이 아웃 재귀함수
    # 게임이 종료상태 (승 또는 패 또는 비김)가 될때까지 행동을 임의로 선택하는 것을 반복
    # 플레이어는 계속 바뀌기 때문에 (-)를 곱해서 -1, 1, -1 이 되게 함.

    def playout(self, temp_env, action, player):
        # 보드에 플레이어의 선택을 표시(만약 새로운 말을 놓는 거라면)
        if isinstance(action, int):  # 숫자라면
            temp_env.board_r[action] = player
        else:  # 문자라면 -> 움직이는 액션이다
            action = action.split('to')  # action[0]: 지울 장소, action[1]: 생길 장소

            # 원래 있던 자리에 있는 말을 지우고, (real 보드에만 지우면 된다) 옮길 자리에 추가한다(마찬가지로 real 보드에만 추가하면 된다.)
            temp_env.board_r[int(action[0])] = 0
            temp_env.board_r[int(action[1])] = player

        temp_env.end_check()
        # 게임 종료 체크
        if temp_env.done:
            # print("done")
            return
        else:
            # 플레이어 교체
            player = -player
            # 가능한 행동 조사
            available_action = temp_env.get_action(player)
            
            # 무작위로 행동을 선택
            action = np.random.randint(len(available_action))
            utils.count_processing(available_action, action, temp_env, player)
            
            self.playout(temp_env, available_action[action], player)