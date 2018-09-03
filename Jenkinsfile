pipeline {
    agent { dockerfile true }
    stages {
        stage('py_compile') {
            steps {
                sh 'python -m py_compile main.py'
            }
        }
        stage('Formatting') {
            steps {
                sh 'black --check --diff .'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --verbose --junit-xml test-reports/results.xml test.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('pyinstaller') {
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
