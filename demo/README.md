### Bin scripts:  

`cd bin/`  

- Build software requirements: `bash make.sh`.  
- Train: `bash train.sh`.  
- Observe: `bash observe.sh`.  
- Visualize: `bash visualize.sh`.  
- Play: `bash play.sh`.  

### Build a custom environment

This framework is designed to wrap custom environments for applying DQN algorithms.  
All sections to be modified are indicated by comments. Are to be modified only:  
- The environment model package: `env/custom_env/`.  
- The environment controller wrapper file: `env/custom_env_wrapper.py`.  
- The environment view wrapper file: `env/view.py`.  
- The DQN hyperparameter configuration file: `dqn/config/dqn_config.py`.  

### 1. Model

Create the custom environment model.  

**package `env/custom_env/`**  
1. create the environment model classes. E.g: car.py, track.py.  
2. create additional resources. E.g: utils.py, img/.  

**file `env/custom_env/utils.py`**  
1. `(W, H)` -> _(int, int)_: (optional) set the window resolution.  
2. define the global constants and functions.  

**file `env/custom_env/__init__.py`**  
1. `import`, `add`: define the package namespace.  

### 2. Controller

Wrap the environment controller in gym.  

**file `env/custom_env_wrapper.py`**, **class `CustomEnvWrapper`**   
1. `import`: import the environment model.  
2. `__init__()`:  
    - 2.1: construct the environment objects.  
    - 2.2: `lim_features` -> _dict_: set the feature scaling (min, max).  
    - 2.3: `action_space_n` -> _int_: set the action space size.  
    - 2.4: `observation_space_n`: -> _int_: set the observation space size.  
3. `_obs()` -> _np.ndarray<np.float32>_: define the observation function, scaled in [0, 1].  
4. `_rew()` -> _float_: define the step reward function, scaled in [0, 1].  
5. `_done()` -> _bool_: define the end function.  
6. `_info()` -> _dict_: (optional) add log infos.  
7. `reset()` -> _np.ndarray_: define the initial state.  
8. `step(action)` -> _(np.ndarray, float, bool, dict)_: define the transition dynamic for one timestep.  
9. `reset_render()`: (optional) add reset instructions for the view only.  
10. `step_render()`: (optional) add step instructions for the view only.  

### 3. View

#### 3.1 View with pyglet

Wrap the environment view in pyglet.  

**file `env/view.py`**, **class `PygletView`**   
1. `PYGLET` -> _bool_: set to True.  
2. `import`: import the environment utils global constants.  
3. `__init__()`:  
    - 3.1: `(width, height)`, `background_color` -> \<int>: initialize the pyglet parameters.  
    - 3.2: define the view setup.  
4. `await_frame_skip()`: define the wait time for frame skipping.  
5. `get_play_action()` -> _int_: define the played action getter.  
6. `on_draw(dt)`: define the view loop, with refresh rate dt.  

#### 3.2 View with custom interface

Wrap the environment view in a custom interface.  

**file `env/view.py`**, **class `CustomView`**   
1. `PYGLET` -> _bool_: set to False.  
2. `__init__()`: define the view setup.  
3. `await_frame_skip()`: define the wait time for frame skipping.  
4. `get_play_action()` -> _int_: define the played action getter.  
5. `on_draw(dt)`: define the view loop, with refresh rate dt.  
6. `clear()`: define the view clearing function.  
7. create additional resources.  

### 4. Hyperparameter tuning

Tune the hyperparameters and the network configuration.  

**file `dqn/config/dqn_config.py`**   
1. `HYPER_PARAMS` -> _dict_: set the hyperparameters.  
2. `network_config(input_dim)` -> _(torch.nn.Sequential, function, function, int)_:  
    - 2.1 `net` -> _torch.nn.Sequential_: define the neural network.  
    - 2.2 `optim_func` -> _function_: define the optimizer function.  
    - 2.3 `loss_func` -> _function_: define the loss function.  
    - 2.4 `fc_out_dim` -> _int_: set the output dimension passed to the dueling layer.  

****

### Run the programs

0. venv
```
VIRTUAL ENVIRONMENT

source venv/bin/activate

deactivate
```

1. play.py
```
PLAY

python3 play.py
```

2. tensorboard
```
VISUALIZE

tensorboard --logdir ./logs/

http://localhost:6006/
```

3. observe.py
```
OBSERVE

python3 observe.py [-h] -dir DIR [-max_steps MAX_STEPS] [-gpu GPU]

optional arguments:
  -h, --help            show this help message and exit
  -dir DIR              Directory
  -max_steps MAX_STEPS  Max episode steps
  -gpu GPU              GPU #
```

4. train.py
```
TRAIN

python3 train.py [-h] [-gpu GPU] [-n_env N_ENV] [-lr LR] [-gamma GAMMA]
                 [-eps_start EPS_START] [-eps_min EPS_MIN] [-eps_dec EPS_DEC]
                 [-eps_dec_exp EPS_DEC_EXP] [-bs BS] [-min_mem MIN_MEM]
                 [-max_mem MAX_MEM] [-target_update_freq TARGET_UPDATE_FREQ]
                 [-target_soft_update TARGET_SOFT_UPDATE]
                 [-target_soft_update_tau TARGET_SOFT_UPDATE_TAU]
                 [-save_freq SAVE_FREQ] [-log_freq LOG_FREQ]
                 [-save_dir SAVE_DIR] [-log_dir LOG_DIR] [-load LOAD]
                 [-repeat REPEAT] [-max_episode_steps MAX_EPISODE_STEPS]
                 [-max_total_steps MAX_TOTAL_STEPS] [-algo ALGO]

optional arguments:
  -h, --help            show this help message and exit
  -gpu GPU              GPU #
  -n_env N_ENV          Multi-processing environments
  -lr LR                Learning rate
  -gamma GAMMA          Discount factor
  -eps_start EPS_START  Epsilon start
  -eps_min EPS_MIN      Epsilon min
  -eps_dec EPS_DEC      Epsilon decay
  -eps_dec_exp EPS_DEC_EXP
                        Epsilon exponential decay
  -bs BS                Batch size
  -min_mem MIN_MEM      Replay memory buffer min size
  -max_mem MAX_MEM      Replay memory buffer max size
  -target_update_freq TARGET_UPDATE_FREQ
                        Target network update frequency
  -target_soft_update TARGET_SOFT_UPDATE
                        Target network soft update
  -target_soft_update_tau TARGET_SOFT_UPDATE_TAU
                        Target network soft update tau rate
  -save_freq SAVE_FREQ  Save frequency
  -log_freq LOG_FREQ    Log frequency
  -save_dir SAVE_DIR    Save directory
  -log_dir LOG_DIR      Log directory
  -load LOAD            Load model
  -repeat REPEAT        Steps repeat action
  -max_episode_steps MAX_EPISODE_STEPS
                        Episode step limit
  -max_total_steps MAX_TOTAL_STEPS
                        Max total training steps
  -algo ALGO            DQNAgent DoubleDQNAgent DuelingDoubleDQNAgent
                        PerDuelingDoubleDQNAgent
```
