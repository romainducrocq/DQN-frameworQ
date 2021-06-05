# """CHANGE CUSTOM ENV IMPORT HERE""" ##################################################################################
from .custom_env import RES
########################################################################################################################

import gym
from gym import spaces
import numpy as np


class CustomEnvWrapper(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, train=False):
        super(CustomEnvWrapper, self).__init__()

        self.train = train

        self.steps = 0
        self.total_reward = 0.

        # """CHANGE ENV CONSTRUCT HERE""" ##############################################################################
        ################################################################################################################

        # """CHANGE FEATURE SCALING HERE""" ############################################################################
        self.lim_features = {
        }
        ################################################################################################################

        # """CHANGE ACTION AND OBSERVATION SPACE SIZES HERE""" #########################################################
        action_space_n = 1
        observation_space_n = 1
        ################################################################################################################

        if "reward" not in self.lim_features:
            self.lim_features["reward"] = (0., 1.)

        self.action_space = spaces.Discrete(action_space_n)
        self.observation_space = spaces.Box(low=0., high=1., shape=(observation_space_n,), dtype=np.float32)

    def scale(self, x, feature):
        return (x - self.lim_features[feature][0]) / (self.lim_features[feature][1] - self.lim_features[feature][0])

    def _obs(self):
        obs = []

        # """CHANGE OBSERVATION HERE""" ################################################################################
        obs += [1.]
        ################################################################################################################

        return np.array(obs, dtype=np.float32)

    def _rew(self):
        rew = 0.

        # """CHANGE REWARD HERE""" #####################################################################################
        ################################################################################################################

        rew = self.scale(rew, "reward")
        self.total_reward += rew
        return rew

    def _done(self):
        done = False

        # """CHANGE DONE HERE""" #######################################################################################
        ################################################################################################################

        return done

    def _info(self):
        info = {
            "l": self.steps,
            "r": self.total_reward,
            # """CHANGE INFO HERE""" ###################################################################################
            ############################################################################################################
        }
        return info

    def reset(self):
        self.steps = 0
        self.total_reward = 0.

        # """CHANGE RESET HERE""" ######################################################################################
        ################################################################################################################

        if not self.train:
            self.reset_render()

        return self._obs()

    def step(self, action):
        # """CHANGE STEP HERE""" #######################################################################################
        ################################################################################################################

        if not self.train:
            self.step_render()

        self.steps += 1

        return self._obs(), self._rew(), self._done(), self._info()

    def reset_render(self):
        # """CHANGE RESET RENDER HERE""" ###############################################################################
        pass
        ################################################################################################################

    def step_render(self):
        # """CHANGE STEP RENDER HERE""" ################################################################################
        pass
        ################################################################################################################

    def render(self, mode='human'):
        pass
