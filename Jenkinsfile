pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }
    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t mlopsmnist .'
            }
        }
        stage('Run tests') {
            steps {
                sh 'docker run mlopsmnist python -m unittest discover tests/'
            }
        }
        stage('Deploy to local environment') {
            steps {
                sh 'docker run -p 5000:5000 your-image-name'
            }
        }
    }
}
