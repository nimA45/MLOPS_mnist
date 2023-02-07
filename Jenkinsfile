pipeline {
    agent any
    
    stages {
        stage('Build') {

			steps {
				sh 'docker build -t nima45/jenkinstp .'
			}
		}
        stage('Run Docker image') {
            steps {
                sh 'docker run -d nima45/jenkinstp'
            }
        }
    }
}
