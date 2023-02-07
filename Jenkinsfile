pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install flask'
            }
        }
        stage('Run and Test') {
            steps {
                sh 'python my_app.py &'
                sh 'sleep 5'
                sh 'python test.py'
            }
        }
    }
}
