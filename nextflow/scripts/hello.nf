process helloWorld {
"""
echo 'Hello World' > /home/konsternacja/Git/trainings/nextflow/file.txt
"""
}

workflow{

helloWorld()

}
