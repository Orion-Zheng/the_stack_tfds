#!/bin/bash

#SBATCH -J generate_the_stack_dedup       # Job name
#SBATCH -p normal          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 48:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=your_email_address
#SBATCH --mail-type=all    # Send email at begin and end of job
export PATH="$HOME/.local/bin:$PATH"
cd $SCRATCH/the_stack_tfds/build_scripts && \
	                tfds build the_stack_dedup_dataset_builder.py --manual_dir "$SCRATCH/the_stack_tfds/the-stack-dedup/data" --data_dir "$SCRATCH/the_stack_tfds/the_stack_data"
