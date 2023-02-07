pipeline {
    agent any
    
    stages {
        stage('Build') {

			steps {
				sh 'docker build -t mnistmlops .'
			}
		}
        stage('Run Docker image') {
            steps {
                sh 'docker run -p 5000:5000 -d mnistmlops'
            }
        stage('Run Docker image') {
            steps {
                sh 'docker run -p 5000:5000 -d mnistmlops test.py'
            }
        }
    }
}
