pipeline {
    agent {
        label 'python'
    }
    
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
        stage('Activate conda') {
            steps {
                sh 'source /Users/nima/miniconda3/bin/activate tensorflow'
            }
        }
        stage('Test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
