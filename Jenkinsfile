pipeline {
    agent any
    
    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t mlopsmnist .'
            }
        }
        stage('Run tests') {
            steps {
                sh 'docker run mlopsmnist python -m test.py'
            }
        }
        stage('Deploy to local environment') {
            steps {
                sh 'docker run -p 5000:5000 mlopsmnist'
            }
        }
    }
}
