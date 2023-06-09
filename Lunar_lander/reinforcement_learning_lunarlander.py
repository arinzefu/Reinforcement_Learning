# -*- coding: utf-8 -*-
"""Reinforcement_learning_lunarlander.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wIVjWP4WG4yMX_IggvvRABQE1bK2nKF_

# Reinforcement learning on ai playing lunarlander
"""

!apt install swig cmake

!pip install setuptools==65.5.0

!pip install stable-baselines3[extra]
!pip install box2d-py
!pip install huggingface_sb3
!pip install pyglet

!sudo apt-get update
!pip install gym
!apt install python-opengl
!apt install ffmpeg
!apt install xvfb
!pip3 install pyvirtualdisplay

# Virtual display
from pyvirtualdisplay import Display

virtual_display = Display(visible=0, size=(1400, 900))
virtual_display.start()

import gym
from huggingface_sb3 import load_from_hub, package_to_hub, push_to_hub
from huggingface_hub import notebook_login
from collections import deque
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
import os

env  = gym.make("LunarLander-v2")
#reset this environment
obseravation = env.reset()

for _ in range(10):
    #take random action
    action = env.action_space.sample()
    print("Action taken:", action)

    obseravation, reward, done, info = env.step(action)

    #if the game is done
    if done:
        #Reset the environment
        obseravation= env.reset()
        print("environment reset")

env = make_vec_env("LunarLander-v2", n_envs = 8)

# Create environment
env = gym.make('LunarLander-v2')

model = PPO(
    policy="MlpPolicy",
    env=env,
    learning_rate=0.0001,  # lower learning rate for stability
    n_steps=2048,  # increase n_steps for more efficient training
    batch_size=64,  # increase batch size for more efficient training
    n_epochs=100,
    gamma=0.99,  # adjust gamma to balance immediate vs future rewards
    gae_lambda=0.96,  # adjust lambda to balance bias vs variance in advantage estimation
    clip_range=0.2,  # adjust clip range for policy gradient optimization
    clip_range_vf=None,  # disable clipping for value function optimization
    ent_coef=0.0,  # adjust entropy coefficient to balance exploration vs exploitation
    vf_coef=0.5,  # adjust value function coefficient to balance policy gradient and value function optimization
    max_grad_norm=0.7,  # setting gradient clipping
    verbose=1
)

print(model)

policy_net = model.policy
print(policy_net.parameters())

import time

# Train the agent for 1000000 timesteps
start = time.time()
model.learn(total_timesteps=1000000)
end = time.time()

# Print the total training time
print(f"Total training time: {end - start:.2f} seconds")

# save the model 
model_name = "lunar_lander_model"
model.save(model_name)

# Create a new environment for evaluation
eval_env = gym.make('LunarLander-v2')

# Evaluate the model 
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True )

# Print the results

print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")

notebook_login()
!git config --global credential.helper store

import gym
from OpenGL import GL
from OpenGL.GL import glPushMatrix

from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.env_util import make_vec_env

from huggingface_sb3 import package_to_hub

## TODO: Define a repo_id
## repo_id is the id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name} for instance ThomasSimonini/ppo-LunarLander-v2
repo_id = "arinzefu/lunar_lander_model"

# TODO: Define the name of the environment
env_id = "LunarLander-v2"

# Create the evaluation env
eval_env = DummyVecEnv([lambda: gym.make('LunarLander-v2')])




# TODO: Define the model architecture we used
model_architecture = "PPO"

## TODO: Define the commit message
commit_message = "My LunarLander Model "

# method save, evaluate, generate a model card and record a replay video of your agent before pushing the repo to the hub
package_to_hub(model=model, 
               model_name=model_name,
               model_architecture=model_architecture, 
               env_id=env_id, 
               eval_env=eval_env, 
               repo_id=repo_id, 
               commit_message=commit_message)