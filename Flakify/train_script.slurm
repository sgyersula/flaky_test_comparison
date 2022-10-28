#!/bin/bash
#SBATCH -J flakify # job name
#SBATCH -o flakify.out         # output and error file name (%j expands to jobID)
#SBATCH -N 1              # total number of nodes
#SBATCH -n 1
#SBATCH -A Deep-Learning-at-Sca
#SBATCH -p rtx           # queue (partition) -- normal, development, etc.
#SBATCH -t 48:00:00        # run time (hh:mm:ss) - 4 hours


bash Flakify_predictor_cross_validation.sh IDoFT