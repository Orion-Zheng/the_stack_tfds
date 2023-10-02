#!/bin/bash
#SBATCH -J download_the_stack        # Job name
#SBATCH -p normal          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 48:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=your_email_address
#SBATCH --mail-type=all    # Send email at begin and end of job
git clone https://YOUR_HF_USERNAME:YOUR_HF_ACCESS_TOKEN@huggingface.co/datasets/bigcode/the-stack-dedup
