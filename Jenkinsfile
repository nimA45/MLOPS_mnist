pipeline {
    agent any
    
    stage('Build') {

			steps {
				sh 'docker build -t nima45/mnistmlops .'
			}
		}
        stage('Run Docker image') {
            steps {
                sh 'docker run -d nima45/mnistmlops'
            }
        }
}
