#!/bin/bash

#SBATCH --job-name=mc_pi
#SBATCH --account=f202500002hpcvlabistula
#SBATCH --ntasks=1

ml Python
ml OpenMPI

source env/bin/activate

mpirun python3 mc_pi.py
