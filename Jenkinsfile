pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python --version'
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'grihabor/pytest' 
                }
            }
            steps {
                sh 'pytest --verbose --junit-xml test-reports/results.xml test_summ.py' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}
