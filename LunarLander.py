# from collections import default dict # Test this!
import gymnasium as gym
env = gym.make('LunarLander-v3', render_mode='human')
observation, info = env.reset()

episode_over = False
while not episode_over:
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    env.render()

    episode_over = terminated or truncated

env.close()