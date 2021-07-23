# """CHANGE CUSTOM ENV IMPORT HERE""" ##################################################################################
from .custom_env import CustomEnv, RES
########################################################################################################################

import gym
from gym import spaces
import numpy as np

import os
from csv import DictWriter


class CustomEnvWrapper(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, m, p=None):
        super(CustomEnvWrapper, self).__init__()

        self.mode = {"train": False, "observe": False, "play": False, m: True}
        self.player = p if self.mode["play"] else None

        self.steps = 0
        self.total_reward = 0.

        # """CHANGE ENV CONSTRUCT HERE""" ##############################################################################
        self.custom_env = CustomEnv()
        ################################################################################################################

        # """CHANGE ACTION AND OBSERVATION SPACE SIZES HERE""" #########################################################
        action_space_n = self.custom_env.action_space_n
        observation_space_n = self.custom_env.observation_space_n
        ################################################################################################################

        self.action_space = spaces.Discrete(action_space_n)
        self.observation_space = spaces.Box(
            low=0., high=1., shape=(observation_space_n,) if type(observation_space_n) is int else observation_space_n,
            dtype=np.float32
        )

        self.log_info_buffer = []

    def _obs(self):
        obs = []

        # """CHANGE OBSERVATION HERE""" ################################################################################
        obs += self.custom_env.obs()
        ################################################################################################################

        return np.array(obs, dtype=np.float32)

    def _rew(self):
        rew = 0.

        # """CHANGE REWARD HERE""" #####################################################################################
        rew += self.custom_env.rew()
        ################################################################################################################

        self.total_reward += rew
        return rew

    def _done(self):
        done = False

        # """CHANGE DONE HERE""" #######################################################################################
        if self.custom_env.done():
            done = True
        ################################################################################################################

        return done

    def _info(self):
        info = {
            "l": self.steps,
            "r": self.total_reward
        }

        if not self.mode["train"]:

            # """CHANGE INFO HERE""" ###################################################################################
            info.update(self.custom_env.info())
            ############################################################################################################

        return info

    def reset(self):
        self.steps = 0
        self.total_reward = 0.

        # """CHANGE RESET HERE""" ######################################################################################
        self.custom_env.reset()
        ################################################################################################################

        if not self.mode["train"]:
            self.reset_render()

        return self._obs()

    def step(self, action):
        # """CHANGE STEP HERE""" #######################################################################################
        self.custom_env.step(action)
        ################################################################################################################

        if not self.mode["train"]:
            self.step_render()

        self.steps += 1

        return self._obs(), self._rew(), self._done(), self._info()

    def reset_render(self):
        # """CHANGE RESET RENDER HERE""" ###############################################################################
        self.custom_env.reset_render()
        ################################################################################################################

    def step_render(self):
        # """CHANGE STEP RENDER HERE""" ################################################################################
        self.custom_env.step_render()
        ################################################################################################################

    def render(self, mode='human'):
        pass

    def log_info_writer(self, info, done, log, log_step, log_path):
        if log and (done or (log_step > 0 and info["l"] % log_step == 0)):
            if "TimeLimit.truncated" not in info:
                info["TimeLimit.truncated"] = False
            info["done"] = done

            self.log_info_buffer.append(info)

            if done:
                file_exists = os.path.isfile(log_path + ".csv")

                with open(log_path + ".csv", 'a') as f:
                    csv_writer = DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=[k for k in info])
                    if not file_exists:
                        csv_writer.writeheader()
                    for log_info in self.log_info_buffer:
                        csv_writer.writerow(log_info)
                    f.close()

                self.log_info_buffer = []
