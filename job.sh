#!/bin/bash

#SBATCH --job-name=mc_pi
#SBATCH --account=f202500002hpcvlabistula
#SBATCH --ntasks=8

source setup.sh
srun python3 mc_pi.py
