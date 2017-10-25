#!/bin/bash
#SBATCH -A liu-2017-00089-12 
#SBATCH -t 960
list_of_commands=$1
#profiles="profiles.dat"
#list="models.dat"
#cat $argfile | awk '{print $1}' > $profiles
#cat $argfile | awk '{print $2}' > $list

# Run the script by sbatch -n 50 ./parallel_example.sh to run the list_of_commands on 50 cores.
module load parallel/20160722
module load buildenv-intel/2015-1
unset SLURM_NPROCS
servers=`/proj/wallner/slurm_scripts/tasks_per_node.py`
echo $servers
cat $list_of_commands | parallel --eta --ssh=jobsh -S $servers 


