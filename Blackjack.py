# from collections import default dict # Test this!
import gymnasium as gym
env = gym.make('Blackjack-v1', sab=True)
observation, info = env.reset()
print("Initial observaiton:", observation)

done = False
while not done:
    action = env.action_space.sample()
    observation, reward, done, truncated, info = env.step(action)
    print(f"Action: {action}, Observation: {observation}, Reward: {reward}, Done: {done}")

env.close()