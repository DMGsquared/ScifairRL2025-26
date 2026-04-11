import numpy
import os
import gymnasium as gym
from stable_baselines3 import PPO 
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy


env = gym.make('CartPole-v1', render_mode=None)
print("Made")

episodes = 5
for episode in range(1, 1+episodes):
    state = env.reset()

    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, terminated, truncated, info,  = env.step(action)
        score += float(reward)
        if terminated or truncated:
            done = True
    print(f"Episode: {episode} Score: {score}")

env.close()
os.mkdir("../Logs")
log_path = os.path.join('../', "Logs")
print(log_path)