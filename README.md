# dqn_continuous
# Project 2: Continuous Control with DDPG by Tony Ho

### Project Environment Details

This project is about training an agent to move a two jointed arm so that the end maintains contact with a orbiting ball moving at a random speed.  By keeping contact with the ball, the agent will recieve a reward of +0.1 for each timestep.
After a certain time period, the environment is reset.

For this project, the environment is considered solved when the last 100 episodes average a score of at least 30.0

The observational space is of type continuous with a size of 33  
The action space is of type continuous with a size of 4

### Getting Started

Make sure to install the packages Unity ML-Agents, NumPy, PyTorch (v0.4) and Matlibplot  
Also, install Unity3D with the Linux Build Support option enabled

### Instructions

From the command line, type in 'python ./PROJECT_PATH/reacher.py'  
By default, this file is set to load the trained agent.  You can watch the agent perform the task for 3 episodes and the score is printed in the command line window.
The environment is already included for Windows.  If another environment needs to be used, change the line

env = UnityEnvironment(file_name='./Reacher_Windows_x86_64/Reacher.exe')

to point to your environment.  This environment was downloaded from a link found in the lesson "4. The Environment - Explore" in the Continuous Control topic.
