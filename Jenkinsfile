pipeline {
    agent { dockerfile true }
    stages {
        stage('py_compile') {
            steps {
                sh 'python -m py_compile main.py'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
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
