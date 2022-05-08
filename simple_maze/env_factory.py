from maze.core.env.maze_env import MazeEnv
from maze.core.wrappers.maze_gym_env_wrapper import GymMazeEnv
from simple_maze.envs.simple_maze_env_mazerl import SimpleMazeEnv

def make_env(name: str) -> MazeEnv:
    custom_gym_env = SimpleMazeEnv()
    return GymMazeEnv(custom_gym_env)
