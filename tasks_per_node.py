#!/usr/bin/python
import os
import hostlist
#print os.environ
#print os.environ["SLURM_TASKS_PER_NODE"]
#print os.environ["SLURM_JOB_NODELIST"]
#tasks_per_node=os.environ["SLURM_TASKS_PER_NODE"].split(',')
hosts = hostlist.expand_hostlist(os.environ["SLURM_JOB_NODELIST"])
tasks_per_node=hostlist.parse_slurm_tasks_per_node(os.environ["SLURM_TASKS_PER_NODE"])
#print hosts
#print tasks_per_node
task_host=[]
for t,h in zip(tasks_per_node,hosts):
    tasks=t+1
    task_host.append(str(tasks)+'/'+h)

print ",".join(task_host)

