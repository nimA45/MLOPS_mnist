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
                sh 'docker run -it --name mnistmlops --rm -p 5000:5000 mnistmlops'
            }
        }
    }
}
