# Demo code for the HPC tutorial

This repository features a simple demo on using High Performance Computing (HPC) techniques for approximating π using Monte Carlo, targeting the Deucalion HPC cluster.

**NOTE**: this tutorial assumes the HPCvLAB 2025 project account number for ARM nodes. To use a different account, edit the `job.sh` file at the `--account` option, as well as the `-A` argument of the `srun` command below.

## Requirements

The code targets a Linux machine and requires both Python3 and OpenMPI. In Deucalion you need to load both of this modules.

## Installation

### on a local computer

All required packages can be installed using a Python virtual environment. Alternatively you can skip the following steps if numpy and mpi4py are already installed system-wide.

To create a virtual environment and install the required packages in it, run
```
./install.sh
```

To use this environment, run
```
source setup.sh
```
in each shell before using the code.

### on Deucalion

In what follows, we'll use an ARM partition. Since the login node architecture is x86, the installation must be done on an ARM node, using
```
srun -A f202500002hpcvlabistula -p dev-arm ./install.sh
```

**NOTE**: both `./install.sh` and `source setup.sh` will load the Python and OpenMPI modules, so there is no need to load them manually.

## Usage

### on a local computer

Before running anything, you'll need to load the virtual environment, once in each new shell:
```
source setup.sh
```

To execute the code on a single node, run
```
python3 mc_pi.py
```

To execute the code on, e.g., 8 nodes, run
```
mpirun -n 8 python3 mc_pi.py
```

### on Deucalion

This code should not be run in the login nodes. Instead, you'll need use SLURM:

To execute the code using SLURM, submit a batch job using
```
sbatch -p normal-arm job.sh
```
and then check for its completion using
```
squeue -u $USER
```
Then, open the resulting `slurm-*.out` log file.

You can play with parallelization by changing the number of tasks in `job.sh` to some more aggressive value, e.g.
```
#SBATCH --ntasks=256
```
In the output of `sinfo`, note how many nodes are automatically summoned to do the job,, in the rightmost column.

## Miscellaneous

For speed, `mc_pi.py` generates chunks of samples in vectors, exploiting computational efficiency of numpy. You can find out the best chunk size for your setup by using the included `calibrate_mc.py`program. It will generate chunks of different sizes and measures computation time. You should use the chunk size with smallest time, of course.

## Author

Rodrigo Ventura\
Email: rodrigo.ventura (at) tecnico.ulisboa.pt\
Linkedin: https://www.linkedin.com/in/rodrigo-ventura/

Institute for Systems and Robotics | Lisbon\
URL: https://isr.tecnico.ulisboa.pt

Instituto Superior Técnico\
University of Lisbon\
Portugal
