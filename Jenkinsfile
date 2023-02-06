pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t your-image-name .'
            }
        }
        stage('Run tests') {
            steps {
                sh 'docker run your-image-name python -m unittest discover tests/'
            }
        }
        stage('Deploy to local environment') {
            steps {
                sh 'docker run -p 5000:5000 your-image-name'
            }
        }
    }
}
