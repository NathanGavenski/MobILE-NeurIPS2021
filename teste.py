import torch

if __name__ == '__main__':
    x = torch.load('data/expert_data/expert_CartPole-v1.pt')
    for i in range(10):
        print(x[i]['ep_rew'])