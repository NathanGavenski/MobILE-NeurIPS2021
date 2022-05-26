import numpy as np
import torch
from tqdm import tqdm

if __name__ == "__main__":
    dataset = np.load('./data/expert_data/expert_CartPole-v1.npz', allow_pickle=True)
    
    beggining = np.where(dataset['episode_starts'] == True)[0]
    end = np.array([
        *np.array(beggining - 1)[1:],
        dataset['episode_starts'].shape[0]
    ])

    beggining = beggining[:1000]
    end = end[:1000]

    data = []
    for idx, (b, e) in enumerate(zip(tqdm(beggining), end)):
        index = np.array(list(range(b, e)))
        state = dataset['obs'][index]
        nState = dataset['obs'][index+1]
        actions = dataset['actions'][index]
        rewards = dataset['rewards'][index]
        is_terminal = dataset['episode_starts'][index]
        is_terminal[0], is_terminal[-1] = False, True
        entry = {
            'episode': [
                state,
                actions,
                nState,
                rewards,
                is_terminal
            ],
            'ep_rew': dataset['episode_returns'][idx]
        }
        data.append(entry)
    torch.save(data, './data/expert_data/expert_CartPole-v1.pt')