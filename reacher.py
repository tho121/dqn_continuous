from unityagents import UnityEnvironment

import gym
import random
import torch
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

from agent import Agent

env = UnityEnvironment(file_name='./Reacher_Windows_x86_64/Reacher.exe')

# get the default brain
brain_name = env.brain_names[0]
brain = env.brains[brain_name]

# reset the environment
env_info = env.reset(train_mode=True)[brain_name]

# number of agents
num_agents = len(env_info.agents)
print('Number of agents:', num_agents)

# size of each action
action_size = brain.vector_action_space_size
print('Size of each action:', action_size)

# examine the state space 
states = env_info.vector_observations
state_size = states.shape[1]
 
states = env_info.vector_observations                  # get the current state (for each agent)
scores = np.zeros(num_agents)                          # initialize the score (for each agent)

from agent import Agent

agent = Agent(state_size=state_size, action_size=action_size)

def ddpg(continuing=False, n_episodes=1000, max_t=3000, print_every=100):

    if continuing:
        agent.actor_local.load_state_dict(torch.load('checkpoint_actor.pth'))
        agent.critic_local.load_state_dict(torch.load('checkpoint_critic.pth'))

    scores_deque = deque(maxlen=print_every)
    scores = []

    for i_episode in range(1, n_episodes+1):
        env_info = env.reset(train_mode=True)[brain_name]  
        state = env_info.vector_observations
        agent.reset()
        score = 0

        noise_weight = max(0.01, 1.0 - (i_episode/(n_episodes * 0.9)))

        for t in range(max_t):
            action = agent.act(state, add_noise=True, noise_weight=noise_weight)

            env_info = env.step(action)[brain_name]
            next_state = env_info.vector_observations
            reward = env_info.rewards[0]
            done = env_info.local_done[0]
            agent.step(state, action, reward, next_state, done)
            state = next_state
            score += reward

            if done:
                break

        scores_deque.append(score)
        scores.append(score)

        print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)), end="")

        if i_episode % print_every == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
            torch.save(agent.actor_local.state_dict(), 'checkpoint_actor.pth')
            torch.save(agent.critic_local.state_dict(), 'checkpoint_critic.pth')

            if np.mean(scores_deque) >= 30.0:
                print("Environment Solved at episode " + i_episode)
            
    return scores

def test(n_episodes=300, max_t=1000, print_every=100):

    agent.actor_local.load_state_dict(torch.load('checkpoint_actor.pth'))
    agent.critic_local.load_state_dict(torch.load('checkpoint_critic.pth'))

    scores_deque = deque(maxlen=print_every)
    scores = []

    for i_episode in range(1, n_episodes+1):
        env_info = env.reset(train_mode=False)[brain_name]  
        state = env_info.vector_observations
        agent.reset()
        score = 0

        for t in range(max_t):
            action = agent.act(state)

            env_info = env.step(action)[brain_name]
            next_state = env_info.vector_observations
            reward = env_info.rewards[0]
            done = env_info.local_done[0]

            state = next_state
            score += reward

            if done:
                break

        scores_deque.append(score)
        scores.append(score)

        print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)), end="")
        if i_episode % print_every == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
            
    return scores

scores = ddpg(continuing=False, n_episodes=1000)
#scores = test(n_episodes=3)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(np.arange(1, len(scores)+1), scores)
plt.ylabel('Score')
plt.xlabel('Episode #')
plt.savefig('figure1.png')
plt.show()



print("done")
