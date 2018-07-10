from .genome import Genome

class Agent(object):

	def __init__(self, config, name='agent'):

		self.genome = Genome(config)
		self.name = name
		self.generation = 0

	def __str__(self):

		base_str = f"{self.name} (G{self.generation})\n"
		return base_str + str(self.genome)

	def randomize(self):

		self.genome.reset('random')
		return self

	def step(self):

		self.genome.mutate()
		self.generation += 1
