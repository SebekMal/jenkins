pipeline {
    agent any

    stages {
        stage('Configure venv'){
            steps{
                sh '''
                python3 -m venv venv
                source /venv/bin/activate
                pip install -r requirements.txt
                pip install .

                '''
                }
            }

        stage('Test venv'){
            steps{
                sh '''
                source /venv/bin/activate
                pytest

                '''
                }
            }
        stage('Build distribution file '){
            steps{
                sh '''
                source /venv/bin/activate
                python setup.py sdist

                '''
                }
            }
        stage('Clean '){
            steps{
                sh 'rm -rf venv'
                }
            }
        }
}