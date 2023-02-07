pipeline {
    agent any
    
    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t mlopsmnist .'
            }
        }
        stage('run and test') {
            steps {
                sh 'docker run -p 5000:5000 mlopsmnist'
            }
        }
    }
}
