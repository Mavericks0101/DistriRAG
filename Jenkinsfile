pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -e ".[dev]"'
            }
        }

        stage('Test') {
            steps {
                sh 'make lint'
                sh 'make test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Dummy deploy stage: no deployment configured.'
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline finished.'
        }
    }
}
