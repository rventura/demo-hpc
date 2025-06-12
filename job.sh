#!/bin/bash

#SBATCH --job-name=mc_pi
#SBATCH --account=f202500002hpcvlabistula
#SBATCH --ntasks=1024

ml Python
ml OpenMPI

source setup.sh
mpirun python3 mc_pi.py
