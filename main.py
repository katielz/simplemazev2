import gym
import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F

# CREATE ENVIRONMENT
env = gym.make('simple_maze:simplemaze-v0')

#General Test Script
'''
numepisodes = 5
env.reset()
for i in range(numepisodes):
    print("EPISODE:", i)
    state = env.reset()
    action_1 = np.random.choice(np.array([0,1,2,3]))
    action_2 = np.random.choice(np.array([0,1,2,3]))
    a = [action_1,action_2]
    grid=env.step(a)
    env.render()
'''

#Actor Critic Implementation

# DEFINE POLICY NETWORK
obs_size = env.observation_space
obs_size = 16
n_actions = env.action_space.n
HIDDEN_SIZE = 256

# LINEAR RELU NEURAL NETWORK
class neural_network(nn.Module):
    def __init__(self):
        super(neural_network, self).__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 4),
            nn.ReLU(),
            torch.nn.Softmax(dim=0)
        )
    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits

# RUNNING NEURAL NETWORK ON ENVIRONMENT
gamma = 0.90
numepisodes = 20
timesteps = 20
policy = neural_network()
print(policy)
env.reset()
for i in range(numepisodes):
    print("EPISODE:", i+1)
    state = env.reset()
    episode_reward = 0
    reward_list=[]
    print("INITIAL STATE")
    env.render()
    for t in range(timesteps):
        print("STEP", t+1)
        state = torch.flatten(torch.Tensor(state))
        action_prob_1 = policy(state)
        action_prob_2 = policy(state)
        action_1 = np.random.choice(np.array([0,1,2,3]), p=action_prob_1.data.numpy())
        action_2 = np.random.choice(np.array([0,1,2,3]), p=action_prob_2.data.numpy())
        a = [action_1,action_2]
        print("actions", a)
        newstate, reward, done, info = env.step(a)
        env.render()
        reward_list.append(reward)
        episode_reward += gamma**t * reward
        state = newstate
        if done==True:
            break
