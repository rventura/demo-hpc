# Demo code for the HPC tutorial

This repository features a simple demo on using High Performance Computing (HPC) techniques for approximating π using Monte Carlo, targeting the Deucalion HPC cluster.

## Requirements

The code targets a Linux machine and requires both Python3 and OpenMPI. In Deucalion you need to load both of this modules.

## Installation

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

*NOTE*: In Deucalion, both `./install.sh` and `source setup.sh` will load the Python and OpenMPI modules, so there is no need to load them manually.

## Usage

To execute the code on a single node, run
```
python3 mc_pi.py
```

To execute the code on, e.g., 8 nodes, run
```
mpirun -n 8 python3 mc_pi.py
```
*NOTE*: on Deucalion, this code will not work in the login nodes; to run it, you'll need use SLURM (see below).

To execute the code using SLURM, e.g. in Deaucalion, submit a batch job using
```
sbatch -p normal-arm job.sh
```
and then check for completion using `squeue -u $USER` and then open the resulting `slurm-*.out` log file.

## Author

Rodrigo Ventura\
Email: rodrigo.ventura (at) tecnico.ulisboa.pt\
Linkedin: https://www.linkedin.com/in/rodrigo-ventura/

Institute for Systems and Robotics | Lisbon\
URL: https://isr.tecnico.ulisboa.pt

Instituto Superior Técnico\
University of Lisbon\
Portugal
