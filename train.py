from heal.base.agent import Agent
from heal.utils.io import load_config
from os.path import join



if __name__ == '__main__':

    conf = load_config(join('heal', 'augmentation', 'default.yaml'))

    agents = [Agent(conf, name=f"Agent #{i}").randomize() for i in range(1, 2)]
    
    for g in range(0, 5):
        for a in agents:
            print(a)
            a.step()
