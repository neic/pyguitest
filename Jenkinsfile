pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.6'
                }
            }
            steps {
                sh 'python -m py_compile main.py'
            }
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python3'
                }
            }
            post {
                success {
                    archiveArtifacts 'dist/main'
                }
            }
        }
    }
}
