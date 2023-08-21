params.ref='/home/konsternacja/Git/trainings/nextflow/ref/Agy99.fasta'
params.index_dir = '/home/konsternacja/Git/trainings/nextflow/index'


process index {

publishDir("${params.index_dir}", mode: 'copy')

input: 
 path genome 

output:
 path "*"

script: 
"""
bwa index $genome
"""
}

workflow {

ref_ch=Channel.fromPath(params.ref)

index(ref_ch)

}
