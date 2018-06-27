
class ModelAgent():

    def __init__(self, architecture=None, genes=None, initalization='random', agent_id=None, **kwargs):

        self.agent_id = agent_id
        self.initalization = initalization

        self.architecture = architecture
        self.genes = genes

        return

    def __str__(self):
        
        print('Agent ID:', self.agent_id)

        if self.genes is not None:
            for gene in self.genes:
                print(gene)
        else:
            print('No genes assigned.')


def run_test():

    return


if __name__ == '__main__':
    run_test()