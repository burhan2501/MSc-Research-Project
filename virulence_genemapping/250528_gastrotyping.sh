#Array jobs on the HPC

#!/bin/bash
#$ -m a
#$ -q researchsmall.q
#$ -M burhan.ahmed@ukhsa.gov.uk
#$ -N Cperfringens_gastrotyping
#$ -o /home/burhan.ahmed/logs
#$ -e /home/burhan.ahmed/logs
#$ -wd /phengs/hpc_projects/routine_gidis/cperfringens/cperf_pipeline_work/Burhan_MSc_Work
#$ -tc 5
#$ -t 1-118

. /etc/bashrc

module purge
module load /phengs/hpc_software/Modules/production/biopython/python2.7/1.61
module load /phengs/hpc_software/Modules/production/bowtie2/2.1.0patch
module load /phengs/hpc_software/Modules/production/clustalw/2.1
module load /phengs/hpc_software/Modules/production/lxml/python2.7/3.2.3
module load /phengs/hpc_software/Modules/production/numpy/python2.7/1.7.1
module load /phengs/hpc_software/Modules/production/phe/common_modules/1-55
module load /phengs/hpc_software/Modules/production/phe/gene_finder/2-9
module load /phengs/hpc_software/Modules/production/pysam/python2.7/0.7.5
module load /phengs/hpc_software/Modules/production/python/2.7.5
module load /phengs/hpc_software/Modules/production/samtools/0.1.18
module load /phengs/hpc_software/Modules/production/yaml/1.1
module load /phengs/hpc_software/Modules/production/phe/gastro_serotyping/1-3




INFILE=$(sed -n ${SGE_TASK_ID}p 2023_isolate_list.txt)
set -x

gastro_serotyping.py -i $INFILE -o $INFILE/gastro_serotyping -w bacterial-fastq-only -gf /phengs/hpc_projects/routine_gidis/cperfringens/cperf_pipeline_work/cperf_pipeline_data_scripts/geneFinder_files


