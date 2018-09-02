pipeline {
    agent { dockerfile true }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile main.py'
            }
        }
        stage('Deliver') {
            steps {
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
