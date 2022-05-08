from gym.envs.registration import register

register(
    id='simplemaze-v0',
    entry_point='simple_maze.envs:SimpleMazeEnv',
)