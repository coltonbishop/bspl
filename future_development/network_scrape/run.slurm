#!/bin/bash
#SBATCH --job-name=collect_data    # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=20G         # memory per cpu-core
#SBATCH --time=24:00:00         # total run time limit (HH:MM:SS)

python3 -u network.py
