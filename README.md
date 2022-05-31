# CA1-NetPyNE-model

## Description
NetPyNE (www.netpyne.org) version of a model of CA1 microcircuits. (Cutsuridis et al.)

Original model and publication: https://modeldb.yale.edu/234233 

## Setup and execution

To run a single simulation: Requires NEURON with Python. 

1. Type `nrnivmodl mod`. This should create a directory called either i686 or x86_64, depending on your computer's architecture. 
2. To run type: `python init.py`


To run batches: Requires MPI properly installed and NEURON configured to use MPI. 

1. Type `nrnivmodl mod`. This should create a directory called either i686 or x86_64, depending on your computer's architecture. 
2. To run type: mpiexec -np [num_cores] nrniv -python -mpi batch.py
Where [num_cores] should be replaced with the number of processors you want to use. The minimum required is 2, since one will be used to schedule the jobs (master node)

## Overview of file structure:

* /init.py: Main executable; calls functions from other modules. Sets what parameter file to use. When running a batch, NetPyNE will call init.py multiple times and pass a different cfg file for each of the parameter configurations explored.

* /netParams.py: Network parameters

* /cfg.py: Simulation configuration

* /batch.py : Defines the parameters and parameter values to be explored in a batch of simulations, the run configuration (e.g. whether to use MPI+Bulletin Board (for multicore machines) or SLURM/PBS Torque (for HPCs)), and the command to run the batch.


For further information please contact: salvadordura@gmail.com 

