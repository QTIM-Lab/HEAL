import random
import numpy as np


class Genome(object):

    def __init__(self, sequence):

        # Nested dictionary - probably from a YAML file
        self.sequence = sequence
        self.mutation_rate = 0.5
        self.genes = dict()

        for name, config in self.sequence.items():
            g = Gene(name, **config)
            self.insert_gene(name, g)

    def __str__(self):

        return "\n".join(['--'+str(g) for _, g in self.genes.items()])      
    
    def mutate(self):

        for gene in self.genes.values():
            gene.mutate()

    def insert_gene(self, name, gene):
        self.genes[name] = gene

    def get_gene(name):
        return self.genes(name)

    def set_mutation_rate(self, mutation_rate):

        self.mutation_rate = mutation_rate
        for name, gene in self.genes.items():
            gene.set_mutation_rate = self.mutation_rate

    def reset(self, mode='random'):

        for name, gene in self.genes.items():
            gene.reset(mode)


class Gene(object):

    def __init__(self, name, init_value=None, min_value=-10., max_value=10., mutation_rate=0.5, max_decrease=-1., max_increase=1., dtype='real'):

        if init_value is None:
            self.init_value = random.uniform(self.min_value, self.max_value)
        elif min_value < init_value < max_value:
            self.init_value = init_value
        else:
            raise ValueError('Initial value should be between min and max, or None (uniform random)')

        self.value = init_value
        self.min_value, self.max_value = min_value, max_value
        self.mutation_rate = mutation_rate
        self.max_decrease = max_decrease
        self.max_increase = max_increase
        self.dtype = dtype

        if self.dtype not in ['binary', 'real']:
            raise ValueError(f"Invalid data type '{dtype}' for gene {self.name} ('binary' or 'real')")

        self.dtype = dtype
        self.name = name

    def __str__(self):

        return f"{self.name}: {self.value}"

    def reset(self, mode='init'):

        if mode == 'init':
            self.value = self.init_value
        elif mode == 'random':
            if self.dtype == 'real':
                self.value = random.uniform(self.min_value, self.max_value)
            else:
                self.value = random.uniform(0., 1.) > .5
        else:
            raise ValueError("Reset mode should be 'init' or 'random'")

    def mutate(self):

        
        if random.uniform(0., 1.) < self.mutation_rate:  # perform mutation with some probability

            try:
                if self.dtype == 'real':
                    self.value += random.uniform(self.max_decrease, self.max_increase)
                    self.value = np.clip(self.value, self.min_value, self.max_value)
                else:
                    self.value = not self.value
            except ValueError:
                print(f"Invalid value '{self.value}' for {dtype} gene '{self.name}'")
                raise

    def set_mutation_rate(self, mutation_rate):
        self.mutation_rate = mutation_rate


