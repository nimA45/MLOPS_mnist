pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhubaccount')
	}

	stages {

        stage('build from github') {
            steps {
                echo 'fetch code'
                echo 'build code'
            }
        }
        stage('test from github') {
            steps {
                echo 'running test1'
                echo 'running test2'
            }
        }
        
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

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push nima45/jenkinstp'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
