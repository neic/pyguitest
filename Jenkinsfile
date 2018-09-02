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
                    image 'kennethreitz/pipenv'
                }
            }
            steps {
                sh 'pipenv install --deploy'
                sh 'pipenv install pyinstaller'
                sh 'pyinstaller --onefile main.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/main'
                }
            }
        }
    }
}
