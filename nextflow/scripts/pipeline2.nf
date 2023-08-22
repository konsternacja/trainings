params.linkfile = '/home/konsternacja/Git/trainings/nextflow/scripts/links.txt'
params.fastqdir = '/home/konsternacja/Git/trainings/nextflow/fastq'

params.fastq = '/home/konsternacja/Git/trainings/nextflow/fastq/*.fastq.gz'

params.qc = '/home/konsternacja/Git/trainings/nextflow/qc'

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

process quality_control {

publishDir("${params.qc}", mode: 'copy')

input:
 path fastq

output:
 path "*", emit: qc_output

script:
"""
fastqc $fastq
""" 

}

workflow {

/*link_ch = Channel.fromPath(params.linkfile)

download(link_ch)
download.out.outputfile.view()
*/
fastq_ch = Channel.fromPath(params.fastq)

quality_control(fastq_ch)
quality_control.out.qc_output.view()

}
