from typing import Optional, Union

import numpy as np
import gym
from gym import utils

class CartPoleEnv(gym.Env[np.ndarray, Union[int, np.ndarray]]):
    def __init__(self):
        self.env = gym.make('CartPole-v1')

    def step(self, a):
        return self.env.step(a)

    def _get_obs(self):
        return self.env.state
        

    def get_reward(self, obs, act):
                

    def compute_path_rewards(self, paths):
        

    def get_done(self, obs):
        x, x_dot, theta, theta_dot = obs
        done = bool(
            x < -self.x_threshold
            or x > self.x_threshold
            or theta < -self.theta_threshold_radians
            or theta > self.theta_threshold_radians
        )
        return done

    def truncate_paths(self, paths):
        

    def reset_model(self):
        state = self.env.reset()
        return state

    def get_env_state(self):
        

    def set_env_state(self, state):
        self.

    def viewer_setup(self):
        self.viewer.cam.distance = self.model.stat.extent * 0.5
