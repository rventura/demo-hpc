# Demo code for the HPC tutorial

This repository features a simple demo on using High Performance Computing (HPC) techniques for approximating π using Monte Carlo, targeting the Deucalion HPC cluster.

## Requirements

The code targets a Linux machine and requires both Python3 and OpenMPI.

## Installation

All required packages can be installed using a Python virtual environment. Alternatively you can skip the following steps if numpy and mpi4py are already installed system-wide.

To install the required packages on a virtual environment, run
```
./install.sh
```

To use this environment, you need to run
```
source setup.sh
```
in each shell before using the code.

In Deucalion, before `source setup.sh` you need to load both Python and OpenMPI modules using
```
ml Python
ml OpenMPI
```

## Usage

To execute the code in a single node, run
```
python3 mc_pi.py
```

To execute the code on, e.g., 8 nodes, run
```
mpirun -n 8 python3 mc_pi.py
```
NOTE: on Deucalion, this code will not work in the login nodes; do run it, you'll need SLURM (see below).

## Author

Rodrigo Ventura
Email: rodrigo.ventura (at) tecnico.ulisboa.pt

Institute for Systems and Robotics | Lisbon
https://isr.tecnico.ulisboa.pt

Instituto Superior Técnico
University of Lisbon
Portugal

To execute the code using SLURM, e.g. in Deaucalion, submit a batch job using
```
sbatch -p normal-arm job.sh
```


