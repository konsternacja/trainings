params.linkfile = '/home/konsternacja/Git/trainings/nextflow/scripts/links.txt'
params.fastqdir = '/home/konsternacja/Git/trainings/nextflow/fastq'

params.read1 = '/home/konsternacja/Git/trainings/nextflow/fastq/ERR3335404_1.fastq.gz'
params.read2 = '/home/konsternacja/Git/trainings/nextflow/fastq/ERR3335404_2.fastq.gz'

params.SPADES_OUT = '/home/konsternacja/Git/trainings/nextflow/SPADES_OUTPUT'


process download {

publishDir("${params.fastqdir}", mode: 'copy')

input:
 path linkfile

output:
 path "*", emit: outputfile

script:
"""
cat $linkfile | xargs -i -P 2 wget '{}'
"""

}

process assemble {

publishDir("${params.SPADES_OUT}", mode: 'copy')

input:
 path read1
 path read2

output:
 path "*", emit: spades_output

script:
"""
echo ${read1.simpleName} | cut -d'_' -f1 | xargs -i spades.py --careful -1 $read1 -2 $read2 -o '{}'
""" 

}

workflow {

/*link_ch = Channel.fromPath(params.linkfile)

download(link_ch)
download.out.outputfile.view()
*/
read1_ch = Channel.fromPath(params.read1)
read2_ch = Channel.fromPath(params.read2)

assemble(read1_ch, read2_ch)
assemble.out.spades_output.view()

}
