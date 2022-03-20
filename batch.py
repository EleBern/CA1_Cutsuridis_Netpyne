from netpyne import specs
from netpyne.batch import Batch


def batchRemoveConns():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['remove_EC_Conns'] = [5, 10]
        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='nrn_cfg.py', netParamsFile='netParams.py',)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'removeEC'
        b.saveFolder = 'BatchProva'
        b.method = 'grid'
        b.runCfg = {'type': 'hpc_slurm', 
                        'allocation': 'default', 
                        'walltime': '24:00:00',
                        'nodes': 1,
                        'coresPerNode': 96, 
                        'email': 'eleonorabernasconi97@gmail.com',
                        'folder': '/home/ext_eleonorabernasconi97_gmail_com/m1/sim/',  
                        'script': 'init.py', 
                        'mpiCommand': 'mpirun',
                        'skip': True}


        # Run batch simulations
        b.run()

# Main code
if __name__ == '__main__':
        batchRemoveConns()