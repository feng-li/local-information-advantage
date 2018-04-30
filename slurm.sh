#!/bin/bash -l

#SBATCH -J Stocks
#SBATCH -n 1 # Number of cores
#SBATCH -p MCMC # Partition Used.
#SBATCH -t 10-00:00 # Runtime in D-HH:MM
#SBATCH -o JOB%j.out # File to which STDOUT will be written
#SBATCH -e JOB%j.err # File to which STDERR will be written
#SBATCH --mail-type=FAIL # Valid type values are BEGIN, END, FAIL, REQUEUE, and ALL
#SBATCH --mail-user=feng.li@cufe.edu.cn
#SBATCH --array=1-100

# STOCK=shanghai
# STOCK=shenzhen
# STOCK=chuangyeban
STOCK=zhongxiaoban

srun python3 ~/code/sentiment/main.py ${STOCK} /data4/yqhuang/database_table_list/${STOCK}.csv  $SLURM_ARRAY_TASK_ID

## SEND RESULTS
cat JOB${SLURM_JOB_ID}.out JOB${SLURM_JOB_ID}.err |\
/usr/bin/mail -s "JOB${SLURM_JOB_ID}.${SLURM_JOB_NAME}(${CONFIG_FILE})" feng.li@cufe.edu.cn
