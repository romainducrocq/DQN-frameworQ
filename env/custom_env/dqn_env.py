# """CHANGE DQN ENV TEMPLATE HERE""" ###################################################################################

from .utils import RES


class DqnEnv:

    def min_max_scale(self, x, feature):
        return (x - self.min_max[feature][0]) / (self.min_max[feature][1] - self.min_max[feature][0])

    def __init__(self):
        self.min_max = {
            "obs": (0., 1.),
            "rew": (0., 1.)
        }

        self.action_space_n = 1
        self.observation_space_n = 1

    def obs(self):
        return [self.min_max_scale(x, "obs") for x in [1.]]

    def rew(self):
        return self.min_max_scale(0, "rew")

    def done(self):
        return False

    def info(self):
        return {}

    def reset(self):
        pass

    def step(self, action):
        pass

    def reset_render(self):
        pass

    def step_render(self):
        pass

########################################################################################################################
