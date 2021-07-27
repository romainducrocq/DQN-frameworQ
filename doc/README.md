### Bin scripts:  

`cd bin/`  

- Build software requirements: `bash make.sh`.  
- Train: `bash train.sh`.  
- Observe: `bash observe.sh`.  
- Visualize: `bash visualize.sh`.  
- Play: `bash play.sh`.  

### Build a customized environment

This framework is designed to wrap customized environments for applying DQN algorithms.  
All sections to be modified are indicated by comments. Is to be modified only:  
- The environment package `env/`:  
	- The environment model package: `env/custom_env/`.  
	- The environment view wrapper file: `env/view.py`.  
	- The environment controller wrapper file: `env/dqn_env.py`.  
	- The hyperparameter configuration file: `env/dqn_config.py`.  

The `dqn/` package and the main scripts `train.py`, `observe.py`, `play.py` are ready to use.  
They do not require any modifications.  

For implementation examples, see `custom_envs_w_frameworQ.txt`.  

### 1. Model

Create the customized environment model.  

**package `env/custom_env/`**  
1. create the environment model classes.  
2. create additional resources.  

**file `env/custom_env/utils.py`**  
1. `(W, H)` -> _(int, int)_: (optional) set the window resolution.  
2. define the global constants and functions.  

**file `env/custom_env/__init__.py`**  
1. `import`, `add`: define the package namespace.  

### 2. Controller

Wrap the environment controller in DQN logic.  

**file `env/dqn_env.py`**, **class `DqnEnv`**   
1. `import`: import the environment model.  
2. `__init__()`:  
    - 2.1: construct the environment objects.  
    - 2.2: `min_max` -> _dict_: set the feature scaling (min, max).  
    - 2.3: `action_space_n` -> _int_: set the action space size.  
    - 2.4: `observation_space_n`: -> _int | tuple_: set the observation space size.  
3. `obs()` -> _list | numpy.ndarray_: define the observation function, scaled in [0, 1].  
4. `rew()` -> _float_: define the step reward function, scaled in [0, 1].  
5. `done()` -> _bool_: define the end flag function.  
6. `info()` -> _dict_: (optional) add log infos.  
7. `reset()`: define the initial state.  
8. `step(action)`: define the transition dynamic for one timestep.  
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
4. `on_draw()`: define the view loop.  
5. `get_play_action()` -> _int_: define the play action getter.  

#### 3.2 View with custom interface

Wrap the environment view in a custom interface.  

**file `env/view.py`**, **class `CustomView`**   
1. `PYGLET` -> _bool_: set to False.  
2. `DT` -> _float_: set the clock schedule interval.
3. `__init__()`: (optional) define the view setup. 
4. `clear()`: (optional) define the view clearing function.   
5. `on_draw()`: (optional) define the view loop.  
6. `get_play_action()` -> _int_: define the play action getter.  
7. (optional) create additional resources.  

#### 3.3 No view

Disable the environment view.  

1. `PYGLET` -> _bool_: set to False.  

### 4. Hyperparameter tuning

Tune the hyperparameters and the network configuration.  

**file `env/dqn_config.py`**   
1. `HYPER_PARAMS` -> _dict_: set the hyperparameters.  
2. `network_config(input_dim)` -> _(torch.nn.Sequential, int, function, function)_:  
    - 2.1 `net` -> _torch.nn.Sequential_: define the neural network.  
    - 2.2 `fc_out_dim` -> _int_: set the output dimension passed to the dueling layer.  
    - 2.3 `optim_func` -> _function_: define the optimizer function.  
    - 2.4 `loss_func` -> _function_: define the loss function.  

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

python3 play.py [-h] [-max_s MAX_S] [-max_e MAX_E] [-log LOG] [-log_s LOG_S]
                [-player PLAYER]

optional arguments:
  -h, --help        show this help message and exit
  -max_s MAX_S      Max steps per episode if > 0, else inf
  -max_e MAX_E      Max episodes if > 0, else inf
  -log LOG          Log csv to ./logs/test/
  -log_s LOG_S      Log step if > 0, else episode
  -log_dir LOG_DIR  Log directory
  -player PLAYER    Player
```

2. tensorboard
```
VISUALIZE

tensorboard --logdir ./logs/train/

http://localhost:6006/
```

3. observe.py
```
OBSERVE

python3 observe.py [-h] -d D [-gpu GPU] [-max_s MAX_S] [-max_e MAX_E]
                   [-log LOG] [-log_s LOG_S]

optional arguments:
  -h, --help        show this help message and exit
  -d D              Directory
  -gpu GPU          GPU #
  -max_s MAX_S      Max steps per episode if > 0, else inf
  -max_e MAX_E      Max episodes if > 0, else inf
  -log LOG          Log csv to ./logs/test/
  -log_s LOG_S      Log step if > 0, else episode
  -log_dir LOG_DIR  Log directory
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
  -h, --help                                      show this help message and exit
  -gpu GPU                                        GPU #
  -n_env N_ENV                                    Multi-processing environments
  -lr LR                                          Learning rate
  -gamma GAMMA                                    Discount factor
  -eps_start EPS_START                            Epsilon start
  -eps_min EPS_MIN                                Epsilon min
  -eps_dec EPS_DEC                                Epsilon decay
  -eps_dec_exp EPS_DEC_EXP                        Epsilon exponential decay
  -bs BS                                          Batch size
  -min_mem MIN_MEM                                Replay memory buffer min size
  -max_mem MAX_MEM                                Replay memory buffer max size
  -target_update_freq TARGET_UPDATE_FREQ          Target network update frequency
  -target_soft_update TARGET_SOFT_UPDATE          Target network soft update
  -target_soft_update_tau TARGET_SOFT_UPDATE_TAU  Target network soft update tau rate
  -save_freq SAVE_FREQ                            Save frequency
  -log_freq LOG_FREQ                              Log frequency
  -save_dir SAVE_DIR                              Save directory
  -log_dir LOG_DIR                                Log directory
  -load LOAD                                      Load model
  -repeat REPEAT                                  Steps repeat action
  -max_episode_steps MAX_EPISODE_STEPS            Episode step limit
  -max_total_steps MAX_TOTAL_STEPS                Max total training steps
  -algo ALGO                                      DQNAgent 
                                                  DoubleDQNAgent 
                                                  DuelingDoubleDQNAgent
                                                  PerDuelingDoubleDQNAgent
```
