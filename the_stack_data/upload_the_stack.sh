#!/bin/bash
#SBATCH -N 1 
#SBATCH -n 1
#SBATCH --time=48:00:00
#SBATCH --job-name=upload_the_stack
#SBATCH --partition=normal
# load PATH
source ~/.bashrc
# scp files in multi-process manner
gsutil -m cp -r $SCRATCH/the_stack_tfds/the_stack_data/the_stack_dedup gs://fuzhao/
