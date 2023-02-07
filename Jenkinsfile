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
        }
        stage('Test') {
            steps {
                sh '/usr/bin/python3 test.py'
            }
        }
    }
}
