pipeline{
    agent any

    stages{
        stage('Run ml-pipeline'){
            steps{
                bat 'py -m pip instal -r requirements.txt'
                bat 'py ml-pipeline.py'
            }
        }
    }

    post{
        success{echo'Sucess model-validation'}
        failure{echo 'failed check logs'}
    }
}