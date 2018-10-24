# dqn_continuous
# Project 2: Continuous Control with DDPG by Tony Ho

### Report

The implementation of this DDPG algorithm was heavy adapted from the DDPG algorithm used in the Pendulum example.
The hyperparameters were kept very similarly, as well hidden layer design for the actor and critic networks.
This DDPG network is made up of a an Actor network and Critic network, each having two networks, one as a target network and the other as a training network.
Each learning step would do a soft update where the target network would assimulate part of the values of the training network.


Using the pendulum environment has a benchmark for the algorithm, the environment seemed to perform poorly, compared to the expected rewards show in the lesson.
The rewards seem to hit a ceiling and then diverge at around 400 episodes.  I tried implementing the priority replay algorithm found here:
https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/blob/master/experiments/Solve_LunarLander/DuelingDQNPrioritizedReplay.py

The issue still persist, so I tried modifying the noise algorithm and added a noise weight variable to reduce the amount of noise applied as training goes on.
I decided to try this with the Reacher environment and found I was able to complete the environment in 500-800 episodes.

### Hyperparameters

BUFFER_SIZE = int(1e6)  # replay buffer size

BATCH_SIZE = 64         # minibatch size

GAMMA = 0.99            # discount factor

TAU = 1e-3              # for soft update of target parameters

LR_ACTOR = 1e-4         # learning rate of the actor 

LR_CRITIC = 1e-4        # learning rate of the critic

WEIGHT_DECAY = 0.0001   # L2 weight decay


### Plot

![Trained Agent][Figure_1]