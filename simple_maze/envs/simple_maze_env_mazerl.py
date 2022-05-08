import gym
import numpy as np
from gym.spaces import Discrete, Box
import random
import maze.core.env.structured_env

class Action():
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class SimpleMazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        class Agent():
            def __init__(self):
                super(Agent, self).__init__()
                self.id = id
                self.x_coor = 0
                self.y_coor = 0

            def display(self):
                print("Agent ", self.id)
                print("X Coordinate: ", x_coor)
                print("Y Coordinate: ", y_coor)

        # ACTION SPACE
        self.action_space = gym.spaces.Discrete(4)

        # OBSERVATION SPACE
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(4, 4))

        # CREATE GRID
        self.grid = np.zeros((4, 4))

        self.done = False

    def move_agent(self, a):
        self.done = False
        tempNewPos = []
        for i in range(len(a)):
            x_coor = self.agents[i].x_coor
            y_coor = self.agents[i].y_coor
            self.grid[x_coor, y_coor] = 0
            if a[i] == 0: #UP
                x_coor = x_coor - 1
            elif a[i] == 1: #RIGHT
                y_coor = y_coor + 1
            elif a[i] == 2: #DOWN
                x_coor = x_coor + 1
            else:
                y_coor = y_coor - 1
            tempNewPos.append((x_coor,y_coor))

        dontMoveFlag = False
        for i in range(0, len(tempNewPos)):
            for j in range(i+1, len(tempNewPos)):
                if tempNewPos[i] == tempNewPos[j]:
                    dontMoveFlag = True

        for k in range(len(a)):
            if dontMoveFlag == False:
                try:
                    self.grid[tempNewPos[k][0]][tempNewPos[k][1]] = k + 1
                except:
                    self.done = True
                if tempNewPos[k][1] < 0:
                    self.done = True

                self.agents[k].x_coor, self.agents[k].y_coor = tempNewPos[k]

        return self.grid

    def reward(self):
        reward = 0
        for i in range(len(self.agents)):
            if self.agents[i].y_coor == -1 or self.agents[i].x_coor == 4:
                reward = -5
                break
            else:
                reward = 1
        return reward

    def step(self, a):
        self.current_actorid = 0
        num_agents = 2

        def getactorid():
            return self.current_actorid

        def getoneagentaction():
            actors = [Agent() for i in range(num_agents)]
            currentactor = getactorid()
            action = actors[currentactor].compute_action(self.grid) #state is grid
            self.current_actorid += 1
            if self.current_actorid >= self.num_agents:
                self.current_actorid = 0

        actions_list = []
        for i in range(num_agents):
            action_oneagent = getoneagentaction()
            actions_list.append(action_oneagent)

        self.move_agent(actions_list)
        info={}
        reward = self.reward()
        return self.grid, reward, self.done, info

    def render(self, mode="human"):
        if self.done == False:
            print(self.grid)

    def reset(self):
        class Agent():
            def __init__(self):
                super(Agent, self).__init__()
                self.id = id
                self.x_coor = 0
                self.y_coor = 0

            def display(self):
                print("Agent ", self.id)
                print("X Coordinate: ", x_coor)
                print("Y Coordinate: ", y_coor)

        # ACTION SPACE
        self.action_space = gym.spaces.Discrete(4)

        # OBSERVATION SPACE
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(4, 4))

        # CREATE GRID
        self.grid = np.zeros((4, 4))